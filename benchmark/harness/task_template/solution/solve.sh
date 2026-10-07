#!/bin/bash
set -eu
test ! -e /tests
test ! -e /var/run/docker.sock
mkdir -p /logs/artifacts
cat > /logs/artifacts/result.json <<'JSON'
{"audit": [], "revision_status": "not_supported", "revised_artifacts": [], "owner_decisions": ["Infrastructure smoke test only; no study review performed"], "coverage": {"inspected": [], "not_verified": ["All semantic review"]}}
JSON
