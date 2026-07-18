# Playwright CLI

A Codex skill for token-efficient browser automation with Microsoft's [Playwright CLI](https://github.com/microsoft/playwright-cli). It covers accessibility snapshots, ref-based interaction, screenshots, PDFs, console and network inspection, traces, videos, request mocking, and the boundary between live exploration and durable Playwright tests.

## Install

Install the current CLI:

```bash
npm install -g @playwright/cli@latest
playwright-cli --help
```

Install this skill:

```bash
git clone https://github.com/msftnadavbh/stuff.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R stuff/skills/playwright-cli "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Start a fresh Codex session, then invoke it with:

```text
$playwright-cli Open my local app, test the login flow, and report console errors.
```

## Package Contents

- `SKILL.md`: core browser workflow and command routing.
- `agents/openai.yaml`: Codex UI metadata.
- `references/`: focused guides for sessions, traces, videos, tests, storage state, mocking, and generated code.
