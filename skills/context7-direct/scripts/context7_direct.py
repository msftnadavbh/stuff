#!/usr/bin/env python3
import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    print("Python 3.11+ is required for tomllib.", file=sys.stderr)
    raise


CONFIG_PATH = Path.home() / ".codex" / "config.toml"
DEFAULT_URL = "https://mcp.context7.com/mcp"


def load_context7_config():
    data = tomllib.loads(CONFIG_PATH.read_text())
    servers = data.get("mcp_servers", {})

    for name in ("context7", "ctx7"):
        server = servers.get(name)
        if not isinstance(server, dict):
            continue
        headers = server.get("http_headers") or {}
        return {
            "url": server.get("url") or DEFAULT_URL,
            "api_key": headers.get("CONTEXT7_API_KEY"),
        }

    return {"url": DEFAULT_URL, "api_key": None}


def request_json(url, payload, headers):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            raw = response.read().decode("utf-8", errors="replace")
            response_headers = dict(response.headers.items())
            return response_headers, parse_mcp_response(raw)
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {raw[:1000]}") from exc


def parse_mcp_response(raw):
    text = raw.strip()
    if not text:
        return None

    # Context7 returns text/event-stream for Streamable HTTP.
    data_lines = []
    for line in text.splitlines():
        if line.startswith("data:"):
            data_lines.append(line[5:].strip())
    if data_lines:
        text = "\n".join(data_lines)

    return json.loads(text)


def base_headers(api_key=None, session_id=None):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if api_key:
        headers["CONTEXT7_API_KEY"] = api_key
    if session_id:
        headers["Mcp-Session-Id"] = session_id
    return headers


def get_header(headers, name):
    wanted = name.lower()
    for key, value in headers.items():
        if key.lower() == wanted:
            return value.strip()
    return None


def open_session(url, api_key):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2025-03-26",
            "capabilities": {},
            "clientInfo": {"name": "codex-context7-direct", "version": "1.0.0"},
        },
    }
    headers, _ = request_json(url, payload, base_headers(api_key))
    session_id = get_header(headers, "mcp-session-id")
    if not session_id:
        raise RuntimeError("Context7 initialize response did not include Mcp-Session-Id.")

    notify = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized",
        "params": {},
    }
    request_json(url, notify, base_headers(api_key, session_id))
    return session_id


def call_tool(tool_name, arguments):
    cfg = load_context7_config()
    session_id = open_session(cfg["url"], cfg["api_key"])
    payload = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments},
    }
    _, result = request_json(cfg["url"], payload, base_headers(cfg["api_key"], session_id))
    if "error" in result:
        raise RuntimeError(json.dumps(result["error"], indent=2))
    return result["result"]


def print_content(result):
    content = result.get("content", [])
    if not content:
        print(json.dumps(result, indent=2))
        return

    for item in content:
        if item.get("type") == "text":
            print(item.get("text", ""))
        else:
            print(json.dumps(item, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Direct Context7 MCP fallback for Codex.")
    sub = parser.add_subparsers(dest="command", required=True)

    resolve = sub.add_parser("resolve", help="Resolve a library name to Context7 IDs.")
    resolve.add_argument("library_name")
    resolve.add_argument("query")

    query = sub.add_parser("query", help="Query docs for a Context7 library ID.")
    query.add_argument("library_id")
    query.add_argument("query")

    args = parser.parse_args()

    if args.command == "resolve":
        result = call_tool(
            "resolve-library-id",
            {"libraryName": args.library_name, "query": args.query},
        )
    else:
        result = call_tool(
            "query-docs",
            {"libraryId": args.library_id, "query": args.query},
        )

    print_content(result)


if __name__ == "__main__":
    main()
