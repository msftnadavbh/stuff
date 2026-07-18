# Wise Owl

Wise Owl is a read-only multi-agent second-opinion workflow for reviewing plans, diffs, security boundaries, tests, CI, and production-sensitive changes. It combines Logic Owl, Guardian Owl, Proof Owl, and Prime Owl under a strict evidence-based review contract.

This directory packages the core skill, schemas, validator, and installer logic. Wise Owl also requires its custom Codex agent definitions, so use the complete public distribution for installation.

## Install

```bash
git clone https://github.com/msftnadavbh/wiseowl.git
cd wiseowl
python3 wise-owl-plugin/scripts/install_wise_owl.py --scope user
```

Start a fresh Codex session, then invoke it with:

```text
$wise-owl Review this implementation plan before I start coding.
```

See the canonical [Wise Owl repository](https://github.com/msftnadavbh/wiseowl) for the complete plugin, agent TOMLs, tests, release verification, and current installation options.

## Package Contents

- `SKILL.md`: review modes and orchestration contract.
- `references/`: finding schema and severity rubric.
- `scripts/`: packet validator and installer logic.
- `LICENSE`: MIT license from the canonical Wise Owl project.
