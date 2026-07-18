# Config And Environment

Use this reference when editing Vercel project configuration or environment handling.

## Files To Inspect

- `vercel.json`
- `vercel.ts`
- `.vercel/project.json`
- `package.json`
- framework config such as `next.config.*`, `vite.config.*`, `astro.config.*`, or `svelte.config.*`
- env examples such as `.env.example`, `.env.local.example`, or deployment docs

## Project Configuration

Common settings include:

- `framework`
- `buildCommand`
- `devCommand`
- `installCommand`
- `outputDirectory`
- `functions`
- `rewrites`
- `redirects`
- `headers`
- `crons`

Prefer the repository's current style. If it uses `vercel.ts`, keep type-safe config there. If it uses `vercel.json`, keep JSON valid and include the schema when adding a new file:

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json"
}
```

## Environment Variables

Use Vercel as source of truth when the project is already linked:

```bash
vercel env ls
vercel env pull .env.local
vercel env add <name> <environment>
vercel env rm <name> <environment>
vercel env run -- <command>
```

Environment names are usually `development`, `preview`, or `production`. Do not print secret values. When summarizing, mention variable names and target environments only.

## Rewrites, Redirects, Headers, Crons

Keep routing changes narrow and test with preview deploys. For cron jobs, confirm that the `path` maps to a real route or function and that the schedule matches the user's intended timezone and cadence.

Example cron shape:

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "crons": [
    {
      "path": "/api/cron/my-job",
      "schedule": "0 0 * * *"
    }
  ]
}
```

For cache headers, redirects, and rewrites, verify behavior with `vercel curl` against the preview deployment before production rollout.
