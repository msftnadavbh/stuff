# Debugging And Incidents

Use this reference when investigating Vercel failures, production errors, or bad deployments.

## Logs

```bash
vercel logs --environment production --level error --since 5m
vercel logs --environment production --status-code 5xx --since 1h
vercel logs --deployment <deployment-id-or-url> --level error --expand
vercel logs --deployment <deployment-id-or-url> --json --since 1h
```

Avoid dumping large logs into chat. Summarize recurring error messages, affected paths, timestamps, deployment IDs, and likely source files.

## Inspect Deployments

```bash
vercel list --prod
vercel inspect <deployment-url>
vercel inspect <deployment-url> --logs
```

Use `inspect --logs` for build failures and deployment metadata. Correlate deployment commit SHA with local git history before editing code.

## Production 500s

Suggested triage:

```bash
vercel logs --environment production --status-code 5xx --since 30m
vercel list --prod
vercel inspect <bad-deployment-url>
vercel inspect <bad-deployment-url> --logs
```

Then correlate:

```bash
git log --oneline -10
git show <commit-sha> --stat
```

Fix locally, run tests/builds, deploy a preview, and verify:

```bash
vercel deploy
vercel curl /api/failing-route --deployment <preview-url>
vercel logs --deployment <preview-deployment-id> --level error
```

## Rollback

Rollback is a production-changing action. Use it when the user asks for rollback or service restoration is explicitly the priority:

```bash
vercel rollback
vercel rollback status
vercel logs --environment production --status-code 5xx --since 5m
```

If the bad range is unclear and the project supports it, use bisect:

```bash
vercel bisect --good <good-deployment-url> --bad <bad-deployment-url>
vercel bisect --good <good-deployment-url> --bad <bad-deployment-url> --path /api/failing-route
```
