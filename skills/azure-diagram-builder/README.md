# Azure Diagram Builder

A Codex skill for designing, rendering, reviewing, costing, and documenting Azure architectures through Arturo Quiroga's [Azure Architecture Diagram Builder](https://github.com/Arturo-Quiroga-MSFT/azure-architecture-diagram-builder) MCP server.

## Capabilities

- Render Azure architecture diagrams as SVG or interactive HTML.
- Review modeled topology against Azure Well-Architected Framework rules.
- Estimate regional Azure costs.
- Import manifests and React Flow scenes.
- Export editable scenes, Bicep, Terraform, manifests, and deployment guides.

The outputs are design-time guidance. The skill does not inspect deployed resources or authorize deployments.

## Install

Install the upstream MCP runtime:

```bash
git clone https://github.com/Arturo-Quiroga-MSFT/azure-architecture-diagram-builder.git ~/.codex/tools/azure-architecture-diagram-builder
cd ~/.codex/tools/azure-architecture-diagram-builder/mcp-server
npm ci
npm run build
codex mcp add azure-diagram-builder -- node "$PWD/dist/index.js"
```

Install the skill from this repository:

```bash
git clone https://github.com/msftnadavbh/stuff.git
mkdir -p ~/.codex/skills
cp -R stuff/skills/azure-diagram-builder ~/.codex/skills/
```

Start a fresh Codex session, then invoke it with:

```text
$azure-diagram-builder Create a secure Azure architecture diagram for my workload.
```

## Package Contents

- `SKILL.md`: triggering rules and workflow.
- `agents/openai.yaml`: Codex UI metadata.
- `references/tools.md`: MCP tool selection and output checks.
