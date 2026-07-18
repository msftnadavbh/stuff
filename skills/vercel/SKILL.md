---
name: vercel
description: Use Vercel platform and CLI workflows for frontend and full-stack web deployments. Use when Codex needs to prepare, link, configure, deploy, preview, promote, rollback, debug, or inspect Vercel projects; manage Vercel environment variables, domains, logs, builds, framework settings, vercel.json/vercel.ts configuration, serverless or edge functions, cron jobs, or production incidents on Vercel.
---

# Vercel

## Workflow

Use current Vercel docs for commands or APIs when details matter. Prefer project-local commands and existing package scripts over inventing deployment flow.

1. Inspect the project first: framework, `package.json`, lockfile, `.vercel/`, `vercel.json`, `vercel.ts`, environment files, and existing README/deploy docs.
2. Check whether `vercel` is available with `command -v vercel`. If missing, use `npx vercel@latest <command>` or install only with user approval.
3. Avoid production-changing commands until the user explicitly asks or confirms. Treat `vercel deploy --prod`, `vercel rollback`, domain changes, env var deletion, and project removal as high-impact.
4. Prefer preview deploys for verification: deploy preview, inspect logs, hit health or route checks, then promote or deploy to production only after validation.
5. Never print secrets. When pulling env vars, write to the expected local env file and summarize names/counts only.

## Common Commands

```bash
vercel login
vercel whoami
vercel link
vercel pull
vercel env pull .env.local
vercel env run -- npm run dev
vercel dev
vercel build
vercel deploy
vercel deploy --prod
vercel inspect <deployment-url>
vercel inspect <deployment-url> --logs
vercel logs --deployment <deployment-id-or-url> --level error
vercel logs --environment production --level error --since 5m
vercel curl / --deployment <deployment-url>
vercel list
vercel list --prod
vercel domains add <domain> <project-name>
vercel domains inspect <domain>
vercel rollback
vercel rollback status
```

Use `npx vercel@latest ...` when the global CLI is not installed and a one-off command is enough.

## Deployment Pattern

For a normal CLI deployment:

```bash
vercel link
vercel env pull .env.local
vercel env run -- npm run dev
vercel deploy
vercel curl / --deployment <preview-url>
vercel logs --deployment <preview-deployment-id> --level error
vercel deploy --prod
vercel curl / --deployment <production-url>
vercel logs --environment production --level error --since 5m
```

If a framework has an established local test/build command, run that before `vercel deploy`. For Next.js, prefer the repository's `npm run build`, `pnpm build`, or equivalent unless the project docs say to use `vercel build`.

## Environment Variables

Use Vercel env commands when project settings are the source of truth:

```bash
vercel env pull .env.local
vercel env ls
vercel env add <name> <environment>
vercel env rm <name> <environment>
```

Use `vercel env run -- <command>` when a local command needs Vercel-managed env vars without permanently writing a file. Do not reveal env values in chat or logs.

## Production Safety

Before production actions, state what will change and ask for confirmation unless the user already explicitly requested that exact action.

High-impact actions include:

- `vercel deploy --prod`
- `vercel rollback`
- `vercel domains add`, `remove`, or DNS-affecting domain changes
- `vercel env rm` or overwriting production env vars
- deleting projects, teams, deployments, or aliases

For incidents, first inspect logs and deployments. Roll back only when restoring service is the priority or the user asks for it.

## References

Load these files only when the task needs the detail:

- `references/deploy-workflows.md` for link, pull, preview deploy, production deploy, domains, and verification.
- `references/config-and-env.md` for `vercel.json`, `vercel.ts`, framework/build settings, env vars, crons, rewrites, redirects, and headers.
- `references/debugging-and-incidents.md` for logs, inspect, 500s, rollback, bisect, and production triage.
