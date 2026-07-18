# Vercel

A Codex skill for Vercel CLI workflows: project inspection, linking, preview and production deployments, environment variables, domains, logs, rollbacks, and incident diagnosis. It keeps production-changing commands and secret handling behind explicit safety boundaries.

## Install

Install the current CLI:

```bash
npm install --global vercel@latest
vercel login
```

Install this skill:

```bash
git clone https://github.com/msftnadavbh/stuff.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R stuff/skills/vercel "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Start a fresh Codex session, then invoke it with:

```text
$vercel Create a preview deployment, verify it, and inspect error logs.
```

Production deployment remains explicit: validate the preview first, then use `vercel deploy --prod` only when requested.

## Package Contents

- `SKILL.md`: safe Vercel workflow and command selection.
- `agents/openai.yaml`: Codex UI metadata.
- `references/`: deployment, configuration, environment, debugging, and incident guidance.
