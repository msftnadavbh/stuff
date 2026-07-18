# Deploy Workflows

Use this reference for Vercel CLI deployment tasks.

## Initial Project Setup

```bash
vercel login
vercel whoami
vercel link
vercel pull
vercel env pull .env.local
```

Inspect generated `.vercel/project.json` only for project identity, org/team scope, and project linkage. Do not commit `.vercel/` unless the repository already does and project conventions require it.

## Preview First

```bash
vercel deploy
vercel inspect <preview-url>
vercel curl / --deployment <preview-url>
vercel logs --deployment <preview-deployment-id> --level error
```

Use preview deploys to validate code paths, functions, and routing before production. Capture the preview URL in the final answer when deployment succeeds.

## Production Deploy

Run production deploys only after explicit user intent or confirmation:

```bash
vercel deploy --prod
vercel curl / --deployment <production-url>
vercel logs --environment production --level error --since 5m
```

If a preview was already verified, prefer promoting or deploying the exact same revision where the project workflow supports it.

## Domains

```bash
vercel domains add example.com <project-name>
vercel domains inspect example.com
```

Domain commands can affect public traffic. Confirm the project name, team scope, and domain before changing anything.

## Local Development

```bash
vercel env run -- npm run dev
vercel dev
```

Prefer repository scripts when they exist. Use `vercel dev` when the app depends on Vercel routing, functions, rewrites, or platform behavior that the framework dev server does not emulate.
