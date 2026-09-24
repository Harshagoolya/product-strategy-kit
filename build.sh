#!/usr/bin/env bash
# Builds the release assets:
#   dist/product-strategy-kit.plugin      - Claude desktop / Cowork plugin
#   dist/product-direction-research.zip   - skill upload for claude.ai (Customize > Skills)
set -euo pipefail
cd "$(dirname "$0")"
rm -rf dist && mkdir -p dist
(cd plugins/product-strategy-kit && zip -qr ../../dist/product-strategy-kit.plugin . -x "*.DS_Store" -x "*__pycache__*")
(cd plugins/product-strategy-kit/skills && zip -qr ../../../dist/product-direction-research.zip product-direction-research -x "*.DS_Store" -x "*__pycache__*")
ls -lh dist
