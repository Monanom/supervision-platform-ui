# START HERE FOR AI

Use this file as the first entry when any AI tool reads this package.

## Goal

Generate supervision-platform UI demos that stay close to the local golden demo, not generic admin pages.

Default output mode: `static-demo`.

## Read Order

Read these files in order before generating UI:

1. `golden-demo/README.md`
2. `golden-demo/supervision-warning-supervise-query.html`
3. `knowledge/component-parameters/index.md`
4. Read only the relevant files under `knowledge/component-parameters/` for the components used by the page.
5. `compiler/system-prompt.md`
6. `compiler/golden-demo-checklist.md`
7. `compiler/validation-checklist.md`
8. `knowledge/`
9. `data/`
10. `ai-guides/`

Machine-readable component parameters live in `data/sketch-component-contract.json`. Markdown parameter tables are generated from that JSON and must not be edited independently.

For Codex users, also install or read:

- `codex-skills/dorami-ui-protocol/SKILL.md`
- `codex-skills/supervision-page-builder/SKILL.md`

## Priority

When rules conflict, use this order:

1. User's explicit product requirement.
2. Golden demo final behavior and visual treatment.
3. Human-confirmed values in `data/sketch-component-contract.json`.
4. Auto-extracted Sketch evidence in the same contract.
5. `compiler/golden-demo-checklist.md`.
6. `codex-skills/supervision-page-builder/SKILL.md`.
7. `codex-skills/dorami-ui-protocol/SKILL.md`.
8. Generic UI taste.

## Mandatory Generation Steps

Before writing UI:

1. Output page understanding.
2. Output structure plan.
3. Output component mapping.
4. State which golden-demo rules will be reused.
5. State which structured component parameter files will be reused.

When writing UI:

1. Start from `templates/static-demo/` or mirror the golden demo structure.
2. Keep token names and component class hooks recognizable.
3. Use bundled assets from `assets/`.

After writing UI:

1. Run `compiler/golden-demo-checklist.md`.
2. Run `compiler/validation-checklist.md`.
3. Revise failed items before final delivery.

## Do Not

- Do not generate a marketing page, hero page, command-center screen, or generic SaaS admin.
- Do not invent colors, icons, fonts, shadows, rounded cards, or gradients outside the package.
- Do not use Tag styles for table lifecycle statuses; use dot plus text.
- Do not skip the golden demo comparison.
