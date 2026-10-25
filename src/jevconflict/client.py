"""Vercel AI Gateway: the decision endpoint (`/v1/evaluate`) and the OpenAI-compatible chat
endpoint, behind one SQLite cache.

Every response is cached with its measured latency, so reruns are free, exactly reproducible,
and still report the latency of the original call.
"""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GATEWAY = "https://ai-gateway.vercel.sh"


def load_env(path: Path = ROOT / ".env") -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"'))


class Cache:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(path, check_same_thread=False)
        self._db.execute("CREATE TABLE IF NOT EXISTS kv (k TEXT PRIMARY KEY, v TEXT)")
        self._lock = threading.Lock()

    @staticmethod
    def key(*parts) -> str:
        return hashlib.sha256(json.dumps(parts, sort_keys=True).encode()).hexdigest()

    def get(self, key: str):
        with self._lock:
            row = self._db.execute("SELECT v FROM kv WHERE k = ?", (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def set(self, key: str, value) -> None:
        with self._lock:
            self._db.execute("INSERT OR REPLACE INTO kv VALUES (?, ?)", (key, json.dumps(value)))
            self._db.commit()


class _Api:
    def __init__(self, model: str, cache: Cache, base_url: str = GATEWAY,
                 api_key_env: str = "AI_GATEWAY_API_KEY", max_retries: int = 6, salt: str = ""):
        import httpx

        load_env()
        key = os.environ.get(api_key_env)
        if not key:
            raise RuntimeError(f"{api_key_env} is not set (put it in .env)")
        self.client = httpx.Client(base_url=base_url, timeout=180,
                                   headers={"Authorization": f"Bearer {key}"})
        # Pin an exact version, never a floating alias: hosted models change under you.
        self.model = model
        self.cache = cache
        self.max_retries = max_retries
        # A non-empty salt stores identical requests under new cache keys, so they are really
        # re-sent (the rerun noise-floor diagnostic). The request itself is unchanged.
        self.salt = salt

    def _post(self, path: str, body: dict) -> dict:
        """Returns the response plus `_latency_s` (successful request only) and `_cached`."""
        key = Cache.key(path, body, self.salt) if self.salt else Cache.key(path, body)
        if (hit := self.cache.get(key)) is not None:
            return hit | {"_cached": True}
        import httpx

        r = None
        for attempt in range(self.max_retries):
            t0 = time.perf_counter()
            try:
                r = self.client.post(path, json=body)
            except httpx.TransportError:  # DNS blips, dropped connections, timeouts
                time.sleep(min(2 ** attempt, 30))
                continue
            latency = time.perf_counter() - t0
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(min(2 ** attempt, 30))
                continue
            if r.status_code >= 400:
                raise RuntimeError(f"{self.model}: HTTP {r.status_code}: {r.text[:300]}")
            data = r.json() | {"_latency_s": latency}
            self.cache.set(key, data)
            return data | {"_cached": False}
        raise RuntimeError(f"{self.model} kept failing: " + (f"HTTP {r.status_code}" if r is not None else "network error"))

    def close(self):
        self.client.close()


class Gateway(_Api):
    """Decision models (Jev and others) on `/v1/evaluate`."""

    def evaluate(self, state: dict, questions: dict) -> dict:
        return self._post("/v1/evaluate", {"model": self.model, "state": state, "questions": questions})


class Chat(_Api):
    """Generative models on the OpenAI-compatible `/v1/chat/completions`."""

    def __init__(self, model: str, cache: Cache, extra: dict | None = None, **kw):
        super().__init__(model, cache, **kw)
        self.extra = extra or {}

    def complete(self, prompt: str) -> dict:
        body = {"model": self.model, "messages": [{"role": "user", "content": prompt}],
                "temperature": 0, **self.extra}
        return self._post("/v1/chat/completions", body)

    @staticmethod
    def text(data: dict) -> str:
        return (data["choices"][0]["message"].get("content") or "").strip()


def billed_cost(data: dict) -> float | None:
    # Decision endpoint: providerMetadata.gateway.cost; chat endpoint: usage.cost.
    cost = (data.get("providerMetadata") or {}).get("gateway", {}).get("cost")
    if cost is None:
        cost = (data.get("usage") or {}).get("cost")
    return float(cost) if cost is not None else None
