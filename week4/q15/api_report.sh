#!/usr/bin/env bash

data=$(curl -fsS http://127.0.0.1:8000/packages.json | ./jq.exe '[.[] | select(.status=="active" and .downloads>=100)] | sort_by(-.downloads, .name)')

cat > summary.md << MARKDOWN
# Package Summary

| name | version | downloads |
|------|---------|-----------|
MARKDOWN

echo "$data" | ./jq.exe -r '.[] | "| \(.name) | \(.version) | \(.downloads) |"' >> summary.md
