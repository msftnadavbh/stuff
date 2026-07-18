# Tool Selection

The upstream MCP runtime is deterministic and design-time only.

| Tool | Use | Verify |
|---|---|---|
| `list_services` | Resolve catalog keys, aliases, categories, and pricing coverage | Non-empty `services` and `categories` |
| `import_architecture` | Normalize a manifest or React Flow scene | Expected service count; report `warnings` |
| `validate_architecture` | Score diagram-visible WAF patterns | Numeric `score` and findings grouped by pillar |
| `harden_architecture` | Apply accepted topology remediations | Before/after scores, `changes`, and `unresolved` |
| `estimate_costs` | Estimate monthly regional costs | Region, term, currency, `pricesAsOf`, and fallback flags |
| `render_diagram` | Produce SVG or interactive HTML | Non-empty markup with matching service labels |
| `generate_manifest` | Produce an az prototype interchange manifest | `schemaVersion` and architecture object |
| `generate_bicep` | Produce Bicep with secure defaults | Bicep text, covered/generic services, findings resolved |
| `generate_terraform` | Produce Terraform using AzureRM | Terraform text, covered/generic services, findings resolved |
| `generate_deployment_guide` | Produce a Bicep or Terraform runbook | Prerequisites, deploy, smoke-test, and teardown sections |
| `export_reactflow_scene` | Produce editable web-app JSON | Node count equals service plus group nodes; edges are present |
| `get_waf_rules` | Query rules by pillar or service | Requested filter and non-empty rules when supported |

## Common Compositions

- Diagram: `list_services` if needed, then `render_diagram`.
- Review: `validate_architecture`, `estimate_costs`, and `render_diagram` from the same canonical input.
- Accepted hardening: `validate_architecture`, `harden_architecture`, then validate and render the returned topology.
- IaC package: validate, optionally harden with approval, then generate Bicep or Terraform and a matching deployment guide.
- Editable handoff: `export_reactflow_scene`; reload later with `import_architecture`.

## Boundaries

- WAF validation sees modeled topology, not runtime settings or operational evidence.
- `harden_architecture` addresses topology patterns; generated IaC addresses only generator-supported configuration defaults.
- Cost data can be incomplete or stale. Preserve returned pricing metadata and fallback indicators.
- Generated IaC and commands require qualified review before use.
