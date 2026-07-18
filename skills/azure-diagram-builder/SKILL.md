---
name: azure-diagram-builder
description: Design, render, import, review, harden, cost, and document Azure architectures with the Azure Architecture Diagram Builder MCP server. Use for Azure architecture diagrams, Azure Well-Architected Framework design reviews, architecture manifest or React Flow imports, SVG or interactive HTML rendering, cost estimates, Bicep or Terraform generation, deployment runbooks, and editable Diagram Builder scene exports. Do not use for live-resource auditing, incident diagnosis, Azure deployment, or resource mutation.
---

# Azure Diagram Builder

Use the `azure-diagram-builder` MCP tools to turn a workload description or saved architecture into deterministic design-time artifacts. Nothing in this skill authorizes Azure deployment or modification.

## Workflow

1. Extract the workload, constraints, Azure services, logical groups, and labeled data flows from the request. Infer ordinary details; ask only when ambiguity materially changes the architecture.
2. Use `list_services` once when service type keys are uncertain. Reuse its result for the rest of the task.
3. Build one canonical object with `services`, `connections`, and `groups`. Use stable service names because connections refer to them.
4. If starting from an exported manifest or React Flow JSON, call `import_architecture` first and surface its warnings.
5. Call only the tools needed for the requested deliverables. Calls that consume the same unchanged canonical object may run in parallel.
6. Verify each returned artifact before saving or presenting it.

Read [references/tools.md](references/tools.md) for tool selection and output checks.

## Model Clearly

- Name services by role, such as `Orders API`, and use exact catalog types, such as `Container Apps`.
- Keep diagrams focused. Prefer 3-7 groups and split very large systems into purpose-specific views.
- Label every connection with what moves across it.
- Use `sync` for request/response, `async` for events or telemetry, and `optional` for fallback paths.
- Use left-to-right layout for wide request flows and top-to-bottom layout for layered or hierarchical systems.

## Preserve Intent

- Validate an existing architecture before proposing changes.
- Never call `harden_architecture` as a silent rewrite. Use it when the user asks for hardening or explicitly accepts a revised topology, and show the before/after changes.
- Treat WAF results as diagram-level signals. They do not prove the configuration or health of deployed resources.
- Treat cost output as an estimate tied to its returned region, term, currency, and pricing date.
- Generate IaC or a deployment guide only when requested. Review generated configuration and placeholders; do not execute deployment commands.

## Deliver Artifacts

- Default to SVG for documentation and chat.
- Use interactive HTML when pan, zoom, and tooltips matter.
- Use React Flow JSON when the user wants continued editing in the Diagram Builder web app.
- Save tool output without rewriting its markup or structured content. Use `.svg`, `.html`, `.json`, `.bicep`, `.tf`, or `.md` as appropriate.
- Summarize what was produced, the WAF limitations, unresolved import or pricing warnings, and artifact paths.

## Runtime Failure

If the MCP tools are unavailable, run `codex mcp get azure-diagram-builder`. If the registered server is enabled, tell the user a fresh Codex session may be required; do not substitute invented tool results.
