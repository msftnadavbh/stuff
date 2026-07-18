---
name: playwright-cli
description: Use Playwright CLI for token-efficient browser automation from the shell. Use when Codex needs to open or inspect local web apps, interact with pages by accessibility snapshot refs, verify frontend changes, capture screenshots or PDFs, inspect console logs and network requests, record traces or videos, run small Playwright page snippets, or choose between agent-driven browser exploration and durable Playwright Test coverage.
---

# Playwright CLI

## Workflow

Use `playwright-cli` when the task needs live browser inspection or interaction. Prefer it over screenshots-first browser control when the accessibility snapshot is enough, because snapshots give compact element refs for reliable actions.

1. Confirm the app or page is reachable. If the task involves a local app, start the existing dev server first and keep the session running until verification is complete.
2. Open a browser with `playwright-cli open <url>` or `playwright-cli open --headed <url>` when headed mode helps.
3. Run `playwright-cli snapshot` before interacting. Use refs from the snapshot for clicks, fills, checks, selections, and element-specific screenshots.
4. Verify after each meaningful action with another `snapshot`, plus `console`, `requests`, screenshots, traces, or videos when relevant.
5. Close the browser with `playwright-cli close` when the task is done.

## Core Commands

```bash
playwright-cli open [url]
playwright-cli goto <url>
playwright-cli snapshot
playwright-cli snapshot --depth=4
playwright-cli snapshot --boxes
playwright-cli snapshot <ref>
playwright-cli click <ref>
playwright-cli dblclick <ref>
playwright-cli fill <ref> <text>
playwright-cli fill <ref> <text> --submit
playwright-cli type <text>
playwright-cli press <key>
playwright-cli check <ref>
playwright-cli uncheck <ref>
playwright-cli select <ref> <value>
playwright-cli hover <ref>
playwright-cli drag <startRef> <endRef>
playwright-cli upload <file>
playwright-cli resize <width> <height>
playwright-cli go-back
playwright-cli go-forward
playwright-cli reload
playwright-cli tab-list
playwright-cli tab-new [url]
playwright-cli tab-select <index>
playwright-cli tab-close [index]
playwright-cli close
```

Use `snapshot --depth=N` to keep large pages manageable. Use `snapshot --boxes` when visual position matters or when diagnosing overlap.

## Verification

Use these commands to collect evidence while debugging or validating UI work:

```bash
playwright-cli screenshot
playwright-cli screenshot <ref>
playwright-cli screenshot --filename=outputs/page.png
playwright-cli pdf --filename=outputs/page.pdf
playwright-cli console
playwright-cli console warning
playwright-cli requests
playwright-cli request <index>
playwright-cli route <pattern>
playwright-cli route-list
playwright-cli unroute [pattern]
playwright-cli tracing-start
playwright-cli tracing-stop
playwright-cli video-start outputs/session.webm
playwright-cli video-chapter "Step name" --description="What changed" --duration=2000
playwright-cli video-stop
playwright-cli show --annotate
playwright-cli generate-locator <ref> --raw
playwright-cli highlight <ref>
playwright-cli highlight --hide
```

Save user-facing screenshots, PDFs, traces, and videos under the current task's `outputs/` directory when one exists. Use temporary files elsewhere only for intermediate debugging.

Use `show --annotate` when the user asks for UI review, design feedback, or clarification about a visible page. It opens the Playwright dashboard so the user can annotate the live page.

## Sessions And State

Use named sessions when multiple browser flows are active or when a task needs persistent state:

```bash
playwright-cli -s=checkout open http://localhost:3000 --persistent
playwright-cli -s=checkout snapshot
playwright-cli -s=checkout state-save work/auth.json
playwright-cli -s=checkout state-load work/auth.json
playwright-cli list
playwright-cli close-all
```

Use storage commands for focused auth or state debugging:

```bash
playwright-cli cookie-list
playwright-cli cookie-get <name>
playwright-cli cookie-set <name> <value>
playwright-cli localstorage-list
playwright-cli localstorage-get <key>
playwright-cli localstorage-set <key> <value>
playwright-cli sessionstorage-list
```

Prefer `close-all` for normal cleanup. Use `kill-all` only for stale browser processes.

## Page Code

Use `run-code` for small Playwright snippets when the CLI action vocabulary is not enough:

```bash
playwright-cli run-code "async page => await page.context().grantPermissions(['geolocation'])"
playwright-cli run-code --filename=work/script.js
```

Keep snippets small and task-specific. For broader repeatable tests, create normal Playwright Test specs instead.

## Install And Fallbacks

If `playwright-cli` is missing, install the current package:

```bash
npm install -g @playwright/cli@latest
```

Then install the upstream agent skills if useful:

```bash
playwright-cli install --skills
```

If the project needs durable regression coverage, use Playwright Test alongside this skill:

```bash
npm install -D @playwright/test@latest
npx playwright install
npx playwright test
npx playwright codegen <url>
npx playwright trace open <trace.zip>
```

Use `playwright-cli` for exploratory agent control and immediate verification. Use `@playwright/test` for committed tests, CI, trace artifacts from tests, and long-lived coverage.

## References

Load these files only when the task needs the extra detail:

- `references/playwright-tests.md` for running, debugging, updating, or healing Playwright tests.
- `references/test-generation.md` and `references/spec-driven-testing.md` for generating tests from browser activity or natural-language specs.
- `references/running-code.md` for advanced `run-code` snippets.
- `references/request-mocking.md` for network route mocking.
- `references/storage-state.md` for cookies, localStorage, sessionStorage, and auth state.
- `references/session-management.md` for named sessions and persistent profiles.
- `references/tracing.md` and `references/video-recording.md` for trace and video artifacts.
- `references/element-attributes.md` for inspecting IDs, classes, test IDs, and locator generation.
