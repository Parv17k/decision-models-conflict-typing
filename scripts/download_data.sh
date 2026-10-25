#!/usr/bin/env bash
# Downloads CONFLICTS (Cattan et al., 2025; Apache-2.0) from Google's repository and checks it is
# the exact file every result in this repository was computed on.
#
#   scripts/download_data.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
URL="https://raw.githubusercontent.com/google-research-datasets/rag_conflicts/main/conflicts.jsonl"
SHA256="14559d5c08fde057d7b46783e3345ee5852d6cf6a750f370dc072a0b957fac54"
OUT="$ROOT/data/conflicts.jsonl"

mkdir -p "$ROOT/data"
curl -sfL -o "$OUT" "$URL"
GOT="$(shasum -a 256 "$OUT" | cut -d' ' -f1)"
if [ "$GOT" != "$SHA256" ]; then
  echo "checksum mismatch: the upstream file changed (got $GOT); results may not reproduce exactly" >&2
  exit 1
fi
echo "data/conflicts.jsonl OK (458 queries, sha256 verified)"
