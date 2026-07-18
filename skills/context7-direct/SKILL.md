---
name: context7-direct
description: Use for Context7 documentation lookup fallback whenever docs for a library, framework, SDK, API, CLI tool, or cloud service are needed and the built-in mcp__context7 tools fail or may be stale. Handles stale OAuth errors by calling Context7 directly from ~/.codex/config.toml without exposing the API key.
---

# Context7 Direct

Use this skill when current library, framework, SDK, API, CLI, or cloud-service documentation is needed and the exposed `mcp__context7` tools are unavailable or return an OAuth error.

## Workflow

1. Try the normal Context7 MCP tools first if they are available.
2. If they fail with auth, routing, stale OAuth, or discovery errors, use the bundled script:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/context7-direct/scripts/context7_direct.py" resolve "Library Name" "Full user question"
python3 "${CODEX_HOME:-$HOME/.codex}/skills/context7-direct/scripts/context7_direct.py" query "/org/project" "Full user question"
```

3. Select the best library ID from `resolve`, then call `query` with that ID.
4. Answer from the returned docs. Mention that the direct Context7 fallback was used only if it matters to the user.

## Notes

- The script reads `CONTEXT7_API_KEY` from `~/.codex/config.toml` under `mcp_servers.context7.http_headers` or `mcp_servers.ctx7.http_headers`.
- The key is never printed.
- The script uses the Streamable HTTP MCP flow: `initialize`, `notifications/initialized`, then `tools/call`.
- If both the built-in tool and this script fail, fall back to official vendor documentation.
