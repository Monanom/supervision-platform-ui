---
name: dorami-ui-protocol
description: Use when Codex needs a Dorami-derived component protocol for buttons, tags, modals, drawers, selects, dropdowns, pagination, tables, forms, inputs, tooltips, or popconfirms in static demos, Figma-like UI, or real Vue/Dorami implementation.
---

# Dorami Component System

Skill Version: v0.16.0

Use this skill to avoid inventing basic UI controls. Treat Dorami as a component protocol first, and as a Vue component library only when the target output explicitly needs production Vue/Dorami code.

Source basis:
- Component package: `/Users/afeng/Desktop/lcy-dorami-front-antd-v5-git-ready-clean-20260622.zip`
- Extracted component rule pages: `3.2 按钮`, `6.2 标签`, `7.8 对话框`, `7.10 侧滑抽屉`
- Package name: `@zcy/dorami`
- Production implementation reference: Vue 2, Ant Design Vue-style components, Less styles, prefix class `dorami`
- Theme mechanism reference: Less variables backed by runtime CSS variables in `components/style/themes/css-variables.less`
- Demo dependency rule: static demos do not need to import Vue or run Dorami. They must reproduce the Dorami-derived component protocol with HTML, CSS, and minimal JS.

## Output Modes

Choose one mode before generating UI:

- `static-demo`: default when the user asks for a page, demo, prototype, or visual preview without naming a production stack. Use pure HTML/CSS/JS and reproduce Dorami structure, states, interaction, and theme behavior.
- `figma-like`: use editable visual structure and preserve Dorami-derived component appearance and states.
- `vue-dorami`: use real Vue + `@zcy/dorami` components when the user explicitly asks for Vue, Dorami code, production implementation, or a real project integration.

Do not require a technology stack during design/demo validation. Select the production stack only when converting an approved demo into real implementation.

## Core Division

Use three layers:

1. Dorami component protocol:
- Use for stable base controls: Button, Tag, Modal, Drawer, Select, Dropdown, Pagination, Table, Form, Input, Textarea, Checkbox, Radio, DatePicker, TimePicker, Upload, Tooltip, Popconfirm, Tabs, Menu, DescriptionList, Timeline, and Empty.
- Preserve component shell, semantics, keyboard behavior, popup behavior, disabled/loading states, and base interaction states.
- For Modal and Drawer, the base shell includes mask, panel/container, title region, body region, footer region, close affordance position, scroll behavior, and footer action layout.
- In `static-demo` and `figma-like`, reproduce this protocol without importing Dorami.

2. Product theme layer:
- Use a lightweight three-layer token system:
  - Raw tokens hold original values only, such as `--brand-8`, `--gray-4`, `--radius-sm`, `--height-control-md`, and `--font-number`.
  - Theme tokens hold page semantics, such as `--theme-primary`, `--theme-bg`, `--theme-border`, and `--theme-text`.
  - Component tokens hold Dorami protocol component values, such as `--dcp-button-primary-bg`, `--dcp-table-header-bg`, and `--dcp-modal-shadow`.
- Define tokens in this order when generating CSS or theme constants: Raw first, Theme second, Component third.
- Page and business layout styles should consume Theme tokens. Dorami protocol component styles should consume Component tokens.
- Component styles must not directly consume Raw tokens unless the value has no semantic meaning. Business skills must not invent new `--dcp-*` component tokens; add them to the product theme mapping first.
- Keep `--v6-color-*` variables only as compatibility mappings when a real Dorami or Ant Design Vue integration needs them. Do not make them the primary authoring layer in static demos.
- Product theme may change atomic values such as color, text color, border color, radius, shadow, mask color, focus ring, and control height tokens.
- Product theme must not redefine the base component shell unless the product explicitly defines a different component variant.
- Prefer Theme/Component variables and small product wrapper classes over editing component source.

3. Business skill layer:
- Let the active product/business skill decide layout, information density, page shell, business table columns, row actions, and forbidden visual directions.
- Business skills decide the content placed inside component slots, not the basic Modal/Drawer/Button/Select/Pagination shell.
- If a business skill needs a visual difference for a base component, express it as a `--dcp-*` component token or named component variant instead of a one-off handmade component.
- Business skills own page compilation, business semantics, field-to-component mapping, status priority, and output contracts. Do not add supervision-specific business objects, workflows, or page recipes to this Dorami protocol skill.

## Mandatory Workflow

Before generating UI with this skill:

1. Identify the output mode: `static-demo`, `figma-like`, or `vue-dorami`. Default to `static-demo` when no stack is specified.
2. Map requested controls to the Dorami component protocol using `references/component-map.md`; use `references/interaction-coverage-matrix.md` as the coverage checklist.
3. If the request is for a supervision platform page, apply `references/supervision-theme-map.md` and the `supervision-page-builder` business rules.
4. In `static-demo`, do not introduce Vue/Dorami imports. Use protocol-compatible HTML/CSS/JS and `dcp-*` protocol classes for base controls.
5. In `static-demo` or theme constants, output Raw, Theme, and Component tokens in that order.
6. In `vue-dorami`, use real Dorami components and apply the product theme through variables and wrapper classes.

## Existing Static Demo Retrofit

Use this section only when adapting an existing static HTML/CSS/JS demo. Do not use it as a substitute for real component integration in production code.

When a demo already exists:
- Audit how UI is generated before editing. Static demos often have multiple helper families, such as `table()` plus `_tbl()`, `statCard()` plus `_stat()`, `badge()` plus `_bdg()`, or both `dialog()` and custom `_openDlg()` helpers.
- Rewrite shared helpers first. A single old `_tbl()` or `_stat()` can keep many pages visually stale even after the shell and token system are updated.
- Add protocol classes to generated controls: `dcp-button`, `dcp-input`, `dcp-select`, `dcp-table`, `dcp-pagination`, `dcp-modal-*`, `dcp-drawer-*`, `dcp-checkbox`, `dcp-radio`, `dcp-tabs`, `dcp-menu`, `dcp-upload`, `dcp-tooltip`, `dcp-popconfirm`, `dcp-empty`, `dcp-description-list`, and `dcp-timeline`.
- If many page fragments are emitted by string templates, a post-render normalizer may add `dcp-*` classes and product wrapper classes after `innerHTML` assignment. This is allowed for static demos only, as a bridge to preserve business content while standardizing visuals.
- The normalizer should be conservative: add protocol classes, classify primary/danger/text buttons by visible action words, and wrap or mark cards/tables/metrics. It must not delete rows, fields, menus, data, or handlers.
- Keep product-specific wrapper classes separate from component protocol classes. For example, `sp-work-card`, `sp-filter-card`, `sp-metric-card`, and `sp-status` may style supervision surfaces while `dcp-*` keeps the base component protocol recognizable.
- After retrofitting, search for old naked controls such as `<table class="w-full">`, unclassified `<button>`, raw `<select>` / `<input>` without protocol styling, custom modal close text, and inline SVG or emoji controls.

Do not:
- Rely only on broad CSS overrides while legacy helpers still emit old component structure.
- Mix new `dcp-*` controls with old ad hoc button/table/modal shells in the same operation area.
- Do not use a post-render normalizer for `vue-dorami`; use real Dorami components there.

## Component Ownership

Dorami component protocol owns:
- Button structure, hierarchy, attributes, sizes, grouping, primary/default/danger/loading/disabled states.
- Tag structure, color variants, filled/light modes, radius, height, and text alignment.
- Modal and Drawer overlay behavior, mask, close affordance, header/body/footer slots, shell padding, body scroll, footer action layout, close behavior, and no-divider default.
- Select and Dropdown popup placement, option hover/selected/disabled states.
- Pagination item behavior, active state, previous/next controls.
- Table base structure, header/body/empty/pagination integration.
- Form, Input, Textarea, Checkbox, Radio, DatePicker, TimePicker, and Upload validation, labels, placeholders, disabled/focus states, popup/file-list states, and keyboard behavior.
- Tooltip and Popconfirm trigger/popup behavior.
- Tabs, Menu, Empty, DescriptionList, and Timeline base structure and interaction semantics.

Product/business skills own:
- Which action is primary.
- Whether a row has zero or one primary button.
- Business-specific danger wording.
- Table column business meaning and adaptive width policy.
- Page shell, cards, background, density, and content hierarchy.
- Product-specific icon sources through theme/component tokens.
- Business content inside Modal and Drawer slots, such as forms, summaries, attachments, logs, descriptions, and workflow copy.

Token ownership:
- Product theme maps Raw tokens into Theme tokens and Component tokens.
- Business skills use Theme tokens for page surfaces, text, borders, status colors, and layout styling.
- Dorami protocol controls use Component tokens for control-specific backgrounds, borders, heights, radius, shadows, overlays, close controls, and popup states.
- `--brand-*`, `--gray-*`, and other Raw tokens are source values, not the normal layer for component CSS.

## References

- `references/component-map.md`: mapping from common UI requests to Dorami-derived component protocols and stack-specific implementation notes.
- `references/interaction-coverage-matrix.md`: coverage checklist for supervision-platform component interactions.
- `references/supervision-theme-map.md`: supervision platform token mapping and override strategy for Dorami components.

## Conflict Priority

Use this order:

1. Active business skill requirements.
2. Product theme token mapping.
3. Dorami component protocol semantics and interaction.
4. Chosen technology stack implementation details.
5. Generic UI taste.

Never let generic Ant Design or default Dorami visuals override a product-specific design contract.

## Versioning

- `v0.1.0`: Initial Dorami component-system extraction.
- `v0.2.0`: Reframe Dorami as a technology-neutral component protocol with `static-demo`, `figma-like`, and `vue-dorami` output modes.
- `v0.3.0`: Add the `dcp-*` class convention for static-demo component protocol implementations.
- `v0.4.0`: Clarify three-layer ownership: base component shell belongs to Dorami protocol, product theme changes atomic tokens, and business skills only fill component slots.
- `v0.5.0`: Add the lightweight Raw / Theme / Component token system and require generated themes to define tokens in that order.
- `v0.6.0`: Add component rule constraints for Button, Modal, and Drawer from the referenced design-system MHTML pages, excluding color token values.
- `v0.7.0`: Add static-demo retrofit rules for existing HTML/JS demos with legacy helper functions and generated fragments.
- `v0.8.0`: Add Tag to the Dorami component protocol, including `dcp-tag`, filled/light/neutral variants, and importance-based tag usage rules.
- `v0.9.0`: Clarify that business skills decide whether table row actions use filled, outline, or text buttons; Dorami protocol does not default table operations to text links.
- `v0.10.0`: Add standard static-demo Button modifiers such as `primary`, `secondary`, `small`, `medium`, and `large`; avoid ad hoc row-action button classes.
- `v0.11.0`: Add detailed extracted rules for Button, Tag, Modal, and Drawer from the backend component specification pages.
- `v0.12.0`: Add exact Button font-size, minimum-width, icon-text minimum-width, and horizontal padding mappings from the button specification screenshots.
- `v0.13.0`: Add full supervision component interaction coverage, including form controls, tabs, menus, upload, tooltip, popconfirm, empty, description list, and timeline protocols.
- `v0.14.0`: Add detailed Tag usage rules for semantic consistency, visual weight, interactive tags, truncation tooltip, disabled state, and table tag folding.
- `v0.15.0`: Separate table status display into StatusIndicator protocol; table lifecycle statuses must not use Tag visuals by default.
- `v0.16.0`: Clarify that page compilation, supervision business semantics, field mapping, and output contracts belong to the active business skill, not this base component protocol.
