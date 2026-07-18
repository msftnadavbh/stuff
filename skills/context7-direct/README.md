# Context7 Direct

A Codex fallback for querying current library, framework, SDK, API, CLI, and cloud-service documentation directly through Context7 when the normal connector has stale authentication or routing problems.

## Requirements

- Python 3.11 or newer.
- A Context7 MCP entry in `~/.codex/config.toml`.
- `CONTEXT7_API_KEY` stored in that entry's `http_headers` table when the endpoint requires a key.

The helper reads the key locally and never prints it.

## Install

```bash
git clone https://github.com/msftnadavbh/stuff.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R stuff/skills/context7-direct "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Start a fresh Codex session, then invoke `$context7-direct` or let Codex select it when Context7's normal tool path fails.

## Package Contents

- `SKILL.md`: fallback routing and usage instructions.
- `scripts/context7_direct.py`: standard-library MCP client for resolving libraries and querying documentation.
