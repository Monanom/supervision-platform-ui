---
name: supervision-page-builder
description: Generate, critique, or adapt UI screens for the LeCaiYun procurement supervision platform using a strict extracted design contract. Use when the user asks to create监管平台 pages, warning/risk supervision screens, list/detail/dialog/dashboard UI, frontend demos, Figma-like layouts, or visual revisions that must match the supervision platform Sketch/source screenshots and avoid known bad cases.
---

# Supervision Platform UI

Skill Version: v0.64.0

Use this skill to produce UI that looks like the LeCaiYun procurement supervision platform, not a generic SaaS page, marketing page, or decorative dashboard. Treat these rules as a design contract.

Bundled source assets:
- Sketch source: `references/sketch/监管平台.sketch`
- Screenshot set: `references/screenshots/`
- Main source groups: `references/screenshots/list`, `references/screenshots/detail`, `references/screenshots/dialog`, `references/screenshots/dashboard`
- Strong comparison groups: `references/screenshots/best` means preferred direction; `references/screenshots/bad` means avoid
- Functional icon source: `assets/icons/`, extracted from the Dorami LeCai component library icon pack. The original zip is kept at `assets/组件库icon.zip`.
- Alphanumeric font source: `assets/fonts/D-DIN-PRO-*.otf`
- Background asset: `assets/bg.jpg`
- Platform logo asset: `assets/supervision-platform-logo-2x.png`
- Base component protocol skill: `dorami-ui-protocol`

## Portable Resource Contract

This skill must be usable by another person after copying the `skills/supervision-page-builder/` folder into their workspace.

Rules:
- Do not depend on author-machine absolute paths for runtime generation.
- Use bundled relative paths from this skill directory: `assets/`, `references/sketch/`, and `references/screenshots/`.
- If a bundled asset is missing, treat that as a packaging problem and report the missing relative path. Do not silently replace it with generic visuals.
- Desktop or temporary paths may appear only in historical notes outside the generation contract; they must not be required to use the skill.
- When generating static demos, copy or reference assets from this skill package, not from the original author's Desktop.

## Mandatory Workflow

Before generating UI, do this:

1. Identify the requested page type: list, detail, dialog, dashboard, empty state, or mixed workflow.
2. Compile the natural-language request into a page blueprint before writing UI.
3. Output "页面理解" with page type, business object, user role, core goal, key fields, actions, states, and unknown TODOs.
4. Output "结构规划" with the selected page pattern, reading order, page regions, and state coverage.
5. Output "组件映射" with the business field/action/status mapped to the supervision business component and the Dorami base protocol.
6. Output "本次复用的监管平台规范" with concrete rules that will be reused.
7. Output "本次复用的组件交互规则" and list the actual components used, such as Button, Table, Tag, Input, Select, Dropdown, Pagination, Modal, Drawer, Form, Checkbox, Radio, Date/Time Picker, Upload, Tooltip, Popconfirm, Tabs, Menu, DescriptionList, Timeline, or Empty.
8. For base controls, follow the `dorami-ui-protocol` component protocol and check `dorami-ui-protocol/references/interaction-coverage-matrix.md`.
9. Apply the supervision theme and business rules in this skill on top of the component protocol. Do not invent a new visual language.
10. After generation, output "一致性自检" including business, component, token, interaction, anti-pattern, and output checks. If any item fails, revise before presenting the final result.

Never skip the pre-generation reuse statements or the final consistency check.

## Page Compiler Rules

Treat this skill as a lightweight page compiler. Convert the user's request into a stable blueprint before choosing layout or writing code.

Blueprint fields:
- `pageName`: user-facing page name.
- `pageType`: `list`, `detail`, `dialog`, `dashboard`, `empty-state`, or `mixed-workflow`.
- `businessObject`: the main supervision object, such as project, purchaser, supplier, contract, warning, risk, approval, rectification, evidence, or handling record.
- `userRole`: the primary user, such as supervision staff, purchaser, agency, reviewer, or platform operator.
- `businessGoal`: what the page helps the user decide or complete.
- `fields`: all requested fields, preserving original business meaning.
- `actions`: all requested page, row, toolbar, form, modal, or drawer actions.
- `states`: lifecycle, risk, approval, data-sync, permission, loading, empty, error, and disabled states.
- `layoutPattern`: selected pattern from this skill.
- `components`: supervision business components and Dorami base protocols.
- `tokens`: required Theme and Component token groups.
- `outputMode`: `static-demo`, `figma-like`, or `vue-dorami`.
- `todos`: unknowns that must not be invented.

Compiler steps:
1. Parse the request into the blueprint.
2. Preserve every business field, operation, state, route, and mock-data meaning unless the user explicitly asks to change it.
3. Select the closest page pattern: List, Detail, Dialog, Dashboard, Empty State, or Mixed Workflow.
4. Map fields, actions, and statuses to business components before choosing visual layout.
5. Apply the Dorami component protocol only for base control shells and interaction states.
6. Apply supervision Theme and Component tokens through the three-layer Raw / Theme / Component system.
7. Generate the UI, prompt, Figma-like structure, or implementation requested by the user.
8. Run the consistency checklist and revise failed items before final output.

Do not skip the blueprint even for short requests. If the user provides too little information, compile the known fields and put missing business facts in TODO instead of inventing them.

## Business Semantics

Use business semantics to decide what information deserves priority. The page must feel like a supervision workbench, not a generic CRUD admin page.

Common business objects:
- Project, purchase notice, procurement plan, contract, order, supplier, purchaser, agency, supervision unit, warning, risk, clue, approval, rectification, evidence, handling record, attachment, operation log, and data-sync record.

Common business actions:
- Search, reset, view detail, export, batch process, submit, approve, reject, withdraw, initiate warning, initiate supervision, assign handler, mark processed, require rectification, upload evidence, download attachment, view flow, view snapshot, confirm completion, and close case.

Common status dimensions:
- Lifecycle: draft, pending submit, pending review, reviewing, approved, rejected, processing, processed, closed, expired.
- Risk: high risk, medium risk, low risk, general reminder, exception, abnormal, normal.
- Read/notify: unread, read, notified, unnotified, replied.
- Data: synced, sync failed, pending sync, missing, stale.
- Permission/action: available, disabled, loading, saving, failed, retryable.

Priority rules:
- Supervision pages must make status, risk, time, responsibility owner, and handling action easy to scan.
- Warning pages must emphasize risk level, warning source, trigger reason, trigger time, and handling status.
- Approval pages must emphasize current node, approval result, opinion, actor, time, and next action.
- Detail pages must emphasize dossier structure: summary, body information, evidence, related records, and process timeline.
- Dashboards must support a supervision decision; charts and metrics must not become decoration.

## Field, Status, and Action Mapping

Map business meaning before styling:

| Business meaning | Examples | Supervision component | Dorami protocol |
|---|---|---|---|
| Primary identifier | 项目编号、预警编号、合同编号 | IdentifierText / CopyText | Button only for copy action |
| Business title | 项目名称、采购事项、合同名称 | PrimaryText | Tooltip for truncation |
| Organization | 采购人、供应商、代理机构、监管单位 | OrgText | Tooltip when truncated |
| Money | 预算金额、成交金额、合同金额 | AmountText | Text |
| Date or time | 创建时间、触发时间、审核时间 | DateText | Text |
| Risk level | 高风险、中风险、低风险、黄色预警 | RiskTag | Tag |
| Table lifecycle status | 已通知、处理中、已完成、已驳回 | StatusIndicator | StatusIndicator, not Tag |
| Approval status | 待审核、审核中、已通过、已驳回 | StatusIndicator or StatusTag by page weight | StatusIndicator / Tag |
| Evidence or file | 附件、凭证、截图、报告 | FileList / UploadArea | Upload |
| Process record | 操作记录、流转记录、审批记录 | Timeline | Timeline |
| Row operation | 查看、处理、导出、撤回 | RowActionGroup | Button / Dropdown / Popconfirm |
| Batch operation | 批量处理、批量导出、批量下发 | ToolbarActionGroup | Button / Dropdown |

Status display rules:
- Table lifecycle statuses use Status Indicator by default: colored dot plus text, no filled background, no rounded tag container.
- Risk level can use stronger Tag visuals when it is a primary supervision signal.
- Do not show the same status dimension twice for one record.
- Dangerous actions use danger semantics and require Popconfirm or Modal depending on business risk.
- More menus are required when row or toolbar actions exceed the direct-action limit.

## Component Protocol Integration

Use `dorami-ui-protocol` for base component structure, states, and interaction.

Output mode:
- Default to `static-demo` when the user asks for a page, demo, prototype, or visual preview without naming a production stack.
- Use `figma-like` when the user asks for editable visual design or Figma-style output.
- Use `vue-dorami` only when the user explicitly asks for real Vue, Dorami, production project code, or component-library integration.

Division:
- Dorami component protocol owns base controls: Button, Modal, Drawer, Select, Dropdown, Pagination, Table, Form, Input, Textarea, Checkbox, Radio, DatePicker, TimePicker, Upload, Tooltip, Popconfirm, Tabs, Menu, DescriptionList, Timeline, and Empty. This includes the basic Modal/Drawer shell, close affordance position, overlay behavior, footer action layout, popup behavior, and component states.
- Supervision theme uses the Raw / Theme / Component token system from `dorami-ui-protocol`: Raw tokens hold source values, Theme tokens style pages, and Component tokens style Dorami protocol controls.
- Supervision theme tokens adapt atomic values on those controls: color, radius, shadow, mask color, border, focus ring, icon asset, and control height.
- This skill owns supervision business layout, density, page shell, table column policy, row action priority, business content inside Modal/Drawer slots, theme tokens, icon rules, and best/bad constraints.
- Do not redefine the basic Modal/Drawer/Button/Select/Pagination shell inside this business skill. If a base component needs a different look, express it as a `--dcp-*` component token or named protocol variant in the theme mapping.
- For `static-demo`, reproduce the protocol with HTML/CSS/JS and do not require Vue or Dorami imports.
- Static demos must use the Dorami protocol class hooks from `dorami-ui-protocol`, such as `dcp-button`, `dcp-select`, `dcp-table`, `dcp-pagination`, `dcp-modal`, `dcp-checkbox`, `dcp-radio`, `dcp-tabs`, `dcp-menu`, `dcp-upload`, `dcp-empty`, `dcp-description-list`, and `dcp-timeline`.
- For `figma-like`, keep controls editable while matching the protocol.
- For `vue-dorami`, use real Dorami components and apply this skill as product theme/business overrides.

Conflict priority:
1. Supervision business rules in this skill.
2. Supervision theme token mapping.
3. Dorami component protocol semantics and interaction.
4. Chosen technology stack implementation details.
5. Generic UI taste.

Use the supervision theme map from `dorami-ui-protocol/references/supervision-theme-map.md` when generating protocol-based supervision pages.

## Existing Static Demo Retrofit Rules

Use this section only when adapting an existing HTML/CSS/JS demo into a supervision platform static demo. Do not apply these shortcuts to new production code or `vue-dorami` output.

## Legacy Demo Component Protocol Action Guide

Use this four-layer action guide before changing any old demo that has hand-written styles, Tailwind fragments, inline colors, emoji icons, or custom string-rendered controls that bypass the Dorami component protocol.

1. Source layer: rewrite shared render helpers first.
   - Find helpers such as `_tbl`, `table`, `_b`, `badge`, `_bdg`, `filterBar`, `_pagination`, `_titleBar`, `dialog`, `sheetPanel`, and row action renderers before editing individual pages.
   - Make helpers emit protocol hooks directly: `dcp-table`, `dcp-button`, `dcp-input`, `dcp-select`, `dcp-pagination`, `dcp-modal`, `dcp-drawer`, `sp-filter-card`, `sp-work-card`, and `sp-status`.
   - Prefer changing one helper that affects many pages over patching many repeated page strings.

2. Bridge layer: add a static-demo-only normalizer.
   - If pages are produced by many legacy string templates, run a `normalizeRenderedContent()` step immediately after each render.
   - The normalizer must do more than add class names. It should also clear conflicting legacy variants such as text-link table buttons, vertical filter layouts, browser-default checkboxes, Tailwind badge classes, old card/table wrappers, hard-coded text colors, emoji business icons, and underline link styles.
   - Keep this bridge limited to static demo retrofits. For clean new demos or production Vue/Dorami output, author correct protocol components directly.

3. Residual scan layer: search for bypass signals after each retrofit pass.
   - Search for old table/card/control fragments, including `hover:underline`, `inline-flex items-center px-2`, `bg-*-50 text-*-700`, `<table class="w-full">`, `color:#fff`, hard-coded hex colors, `emoji`, unicode arrows, inline/manual SVG controls, and controls without `dcp-*` hooks.
   - Also search for broad selectors that can damage component scale, such as global `input` height/width rules that accidentally affect checkbox or radio controls.
   - Treat each hit as either a required fix or an explicitly documented exception. Do not ignore a hit just because the page looks acceptable in one screenshot.

4. Skill feedback layer: update the retrofit rules by default.
   - After a supervision static-demo retrofit, extract reusable issues and fixes back into this skill unless the user explicitly says not to update the skill.
   - Keep updates scoped to demo retrofit behavior. Do not turn demo-only normalizer shortcuts into production `vue-dorami` rules.
   - Favor concise, checkable rules that another AI agent can execute: what to find, what to convert it into, and how to verify it.

Retrofit principle:
- Preserve business content, mock data, menu structure, page registration, and primary click flows. Change presentation first. Ask before deleting business modules, data, or interactions.
- Do not rely on changing only the app shell. Existing demos often render most pages from JS string templates, so the visual system must cover generated page fragments too.
- After any supervision static-demo update, extract reusable retrofit rules and update this skill by default unless the user explicitly says not to update the skill.
- Start by identifying shared render helpers such as `table`, `_tbl`, `statCard`, `_stat`, `badge`, `_bdg`, `filterBar`, `_pagination`, `_titleBar`, `dialog`, and `sheetPanel`. Rewrite these helpers first so many pages inherit the supervision style.
- If pages are produced by many legacy string templates, add a small post-render normalizer after `container.innerHTML = fn()` that upgrades generated controls and surfaces. The normalizer may add protocol classes such as `dcp-button`, `dcp-select`, `dcp-input`, `dcp-table`, `sp-work-card`, `sp-filter-card`, `sp-metric-card`, and `sp-status`.
- Use the normalizer as a bridge for static demos only. It is acceptable for a demo retrofit because it avoids deleting business content while bringing old fragments under the design contract. For clean new demos, author the correct classes directly.

Required retrofit moves:
- Add or replace the full Raw / Theme / Component token block before page CSS. Keep the token order auditable.
- Use bundled demo assets from this skill package: `assets/bg.jpg`, `assets/icons/`, and `assets/fonts/D-DIN-PRO-*`. Use browser-safe icon aliases such as `arrow-down.svg` and `close.svg` where needed.
- Convert app shell first: 220px gradient side nav, 56px translucent top bar, fixed 1366px minimum width, right content background image starting at the top of the main region.
- Convert generated tables to `dcp-table`: 48px header, 56px standard rows, top-aligned cells, tokenized hover, no heavy card borders.
- Convert generated forms and filters: selectors and inputs get `dcp-select` / `dcp-input`; search/reset buttons get `dcp-button primary` / default; filters sit in the same work surface as table content when practical.
- In static demo filters, do not preserve legacy vertical label-over-control layouts. Normalize each filter item to a horizontal label + control row, keep labels fixed/nowrap, and keep filter input, select, and button heights consistent at 32px.
- When normalizing generated form controls, never let broad input rules apply to `checkbox` or `radio`. Exclude them from text-input selectors, add `dcp-checkbox` / `dcp-radio` separately, and keep checkbox size at the component-library scale such as 16px square. A static-demo retrofit rule like `.lc-content input { min-height: 40px; min-width: 200px; }` is invalid because it enlarges checkboxes.
- For static demo checkboxes, do not leave browser-default checkboxes if they visibly differ from the Dorami protocol. Use `dcp-checkbox` with tokenized border, hover, focus ring, checked background, and checked mark while keeping the 16px square scale.
- Convert generated metrics to `sp-metric-card`: frosted metric surface, number first, label below, D-DIN-PRO for alphanumeric glyphs.
- Convert generated status badges to compact dot-plus-text tags with tokenized success, warning, danger, and info states.
- Convert legacy Tailwind-style badges such as `inline-flex items-center px-2 ... bg-blue-50 text-blue-700` to `sp-status` variants instead of only restyling their colors.
- Table row action buttons in static demos must not remain plain text links or text buttons. Normalize actions such as 查看/详情/档案/打分/观看 into compact default or danger `dcp-button` variants inside tables; reserve text buttons for non-table secondary navigation such as 返回.
- Convert legacy modal/drawer helpers to `dcp-modal-*` and `dcp-drawer-*` shells. Close controls must use the icon-only close affordance.
- Sidebar icons in static demos must be visually unified: use linear-style icon assets and render all sidebar functional icons as white fill/stroke on the dark navigation background. Do not allow source SVG colors, mixed status colors, or multi-color icons in the sidebar. This applies to first-level menu icons, expand/collapse arrows, footer icons, lock/permission icons, and other sidebar affordances. If icons are inserted as `<img>`, use a sidebar-scoped recolor rule such as `filter: brightness(0) invert(1)` plus consistent opacity.
- Replace functional emoji, decorative emoji, inline Lucide/manual SVG icons, unicode arrows used as controls, and old text close marks with `assets/icons/` references or text-only controls. Do not add emoji or arbitrary icons to business table text merely to make cells look richer.
- Audit foreground/background contrast after retrofit. If a container background is light, use `--theme-text`, `--theme-text-secondary`, or the auxiliary gray scale for text; if the background is dark, use white or light text. Do not leave hard-coded white text on translucent white top bars or cards. Aim for W3C AA contrast for normal text (at least 4.5:1) and large text/icons where applicable (at least 3:1).
- Remove or neutralize dark "data screen", big-screen, neon, and decorative dashboard treatments unless the user explicitly asks for a command-center screen. For ordinary supervision demos, dashboards remain light operational workbenches.

Do not:
- Leave two visual systems active where half the pages use old Tailwind card/table/button styles and half use the supervision protocol.
- Use global CSS overrides alone if shared JS helpers still emit old tables, cards, badges, or controls.
- Add one-off hard-coded colors inside page strings when a `--theme-*` or `--dcp-*` token exists.
- Put business helper text or explanatory copy into cells merely to fill space.
- Rely on a normalizer that only adds class names while leaving wrong structures or variants intact. It must also clear legacy text-link button classes, vertical filter layouts, browser-default checkbox styling, and old badge classes when those conflict with the protocol.

Retrofit verification:
- Run a syntax check for the whole script after string-template edits.
- Search for high-risk leftovers: naked `<table class="w-full">`, old brand hex values, dark dashboard wrappers, functional/decorative emoji in business data, inline SVG control icons, unicode arrow controls, text-link buttons in table actions, vertical filter labels, hard-coded white text on light surfaces, Tailwind badge classes, and controls without `dcp-*` classes.
- Inspect at least one page from each major rendering path: the original helper path, the later `_tbl/_stat/_bdg` helper path, a dashboard page, a list page, a detail page, and a modal/drawer flow.

## Design DNA

The supervision platform is a dense government/procurement operations system.

Keep:
- Professional, restrained, operational, trustworthy.
- High information density with clear scanning paths.
- Left navigation plus top bar plus content workbench.
- Frosted white content surfaces over a fixed top background JPG, with Brand-1 as the bottom/fallback background color.
- Tables, filters, status, process records, and business text as the core visual language.
- Blue and indigo as action/focus colors.
- Small-radius cards and controls; most structure is rectangular and efficient.

Avoid:
- Marketing hero sections.
- Large decorative cards unrelated to workflow.
- Oversized headings or empty landing-page composition.
- Heavy colorful aurora backgrounds, decorative glassmorphism, or "AI big screen" styling.
- Over-rounded pills everywhere.
- Illustration-led layouts unless the source page type already uses a small empty-state illustration.

## Extracted Design Tokens

Use these values unless the user's supplied source overrides them.

Layout:
- Minimum total page width: 1366px. Below this width, keep the layout at 1366px and allow horizontal scrolling rather than compressing modules.
- Left navigation: fixed 220px wide; it never grows or shrinks.
- Top bar: 56px high.
- Right content region: fluid width, `calc(100vw - 220px)` above 1366px and about 1146px at the 1366px minimum.
- Standard modules, metric rows, work cards, tables, and detail sections use `width: 100%` inside the right content region. They grow when the page grows and shrink until the 1366px minimum.
- Main page padding inside content: 20px to 24px.
- Common vertical rhythm: 16px, 20px, 24px.
- Filter control height: 32px for filter Select, Input, Date/Time, and Button controls.
- Table header height: 48px.
- Standard table single-line row height: 56px. Multi-line rows expand naturally while keeping the same top/bottom padding.

Three-layer token usage:
- Always define Raw tokens first, Theme tokens second, and Component tokens third. This keeps generated pages easy to audit and avoids extra theme-generation complexity.
- Raw tokens hold source values only: brand palette, gray palette, navigation palette, state colors, radius, control heights, font tokens, and asset URLs.
- Theme tokens are the normal page-authoring layer. Page background, surfaces, text, borders, status colors, focus rings, and business layout styling must use `--theme-*`.
- Component tokens are the normal Dorami protocol component layer. Button, Table, Modal, Drawer, Select, Dropdown, Pagination, Form, and Input visuals must use `--dcp-*`.
- UI code must use Theme or Component tokens rather than hard-coded hex values when a token exists.
- Any new color or repeated size must be added to the token table before use. Do not introduce one-off colors in components.
- Do not consume Raw tokens directly in component CSS when a Theme or Component token exists.

Raw brand palette:
- `--brand-1: #F7F7FF`
- `--brand-2: #EEF0FF`
- `--brand-3: #E3E7FF`
- `--brand-4: #CED4FF`
- `--brand-5: #B0B8FF`
- `--brand-6: #8691FF`
- `--brand-7: #5D6AFF`
- `--brand-8: #4353FF`
- `--brand-9: #2C0DF1`
- `--brand-10: #1B00C7`

Raw blue-gray palette:
- `--gray-1: #F7F8FA`
- `--gray-2: #F2F4F7`
- `--gray-3: #ECEEF2`
- `--gray-4: #E3E6EB`
- `--gray-5: #D8DCE2`
- `--gray-6: #C2C7D1`
- `--gray-7: #A7AEBB`
- `--gray-8: #838B99`
- `--gray-9: #505663`
- `--gray-10: #20242C`

Raw navigation palette:
- `--nav-gradient-start: #181C4F`
- `--nav-gradient-end: #394183`
- Side navigation must use these tokens, not Brand tokens.

Theme color tokens:
- `--theme-primary: var(--brand-8)`
- `--theme-primary-hover: var(--brand-7)`
- `--theme-primary-active: var(--brand-9)`
- `--theme-primary-deep: var(--brand-10)`
- `--theme-bg: var(--brand-1)`
- `--theme-bg-soft: var(--brand-1)`
- `--theme-bg-tint: var(--brand-2)`
- `--theme-bg-image: url("assets/bg.jpg")`
- `--theme-surface: #FFFFFF`
- `--theme-surface-metric-from: rgba(255,255,255,.60)`
- `--theme-surface-metric-to: #FFFFFF`
- `--theme-border: var(--gray-4)`
- `--theme-border-soft: var(--gray-3)`
- `--theme-table-head: var(--gray-1)`
- `--theme-text: var(--gray-10)`
- `--theme-text-secondary: var(--gray-9)`
- `--theme-text-muted: var(--gray-8)`
- `--theme-nav-start: var(--nav-gradient-start)`
- `--theme-nav-end: var(--nav-gradient-end)`
- `--theme-nav-hover: color-mix(in srgb, var(--theme-surface) 8%, transparent)`
- `--theme-nav-active: color-mix(in srgb, var(--theme-surface) 12%, transparent)`
- `--theme-focus-ring: rgba(67,83,255,.10)`
- `--theme-overlay: rgba(32,36,44,.45)`
- `--theme-success: #00B552`
- `--theme-warning: #F0770B`
- `--theme-danger: #DF1F1F`

Usage:
- Deep side navigation uses `linear-gradient(180deg, var(--nav-gradient-start), var(--nav-gradient-end))`.
- Primary actions use `--theme-primary`; hover uses `--theme-primary-hover`; active/pressed uses `--theme-primary-active`.
- Page background uses `--theme-bg-image` from the top of the right-side main region, including behind the top bar. It is no-repeat, cover/100% auto; bottom and fallback background must be `--theme-bg` / Brand-1. Do not start the image below the top bar, and do not recreate this with radial or decorative CSS gradients.
- Data metric card surface uses `linear-gradient(180deg, var(--theme-surface-metric-from), var(--theme-surface-metric-to))`, 1px `--theme-surface` border, `backdrop-filter: blur(6px)`, radius 4px.
- Large list/work card surface uses `--theme-surface`, no visible border, no shadow, radius 8px.
- Table header uses `--theme-table-head`.
- Dividers and controls use `--theme-border` or `--theme-border-soft`.
- Primary text uses `--theme-text`; secondary text uses `--theme-text-secondary`; helper text uses `--theme-text-muted`.
- Dorami protocol component CSS should use the component tokens from `dorami-ui-protocol/references/supervision-theme-map.md`, such as `--dcp-button-primary-bg`, `--dcp-table-header-bg`, `--dcp-modal-shadow`, and `--dcp-select-focus-ring`.

Typography:
- Main font size: 14px. This means typography size, not information density.
- Latin and numeric font token: `--font-alphanumeric: "D-DIN-PRO-Alphanumeric"`.
- Compatibility numeric token: `--font-number: var(--font-alphanumeric)`.
- All English letters and numeric glyphs must use D-DIN-PRO through `--font-alphanumeric` / `--font-number`, including English labels, codes, metric numbers, table IDs, dates, times, counts, percentages, pagination numbers, badge counts, and form values.
- In frontend code, define D-DIN-PRO with `@font-face` from `assets/fonts/` and use `unicode-range` for Latin letters and numeric glyphs so Chinese text continues to use the normal Chinese UI font.
- Recommended global stack: `font-family: var(--font-alphanumeric), "PingFang SC", -apple-system, BlinkMacSystemFont, "Microsoft YaHei", sans-serif;`.
- Available weights: 400 Regular, 500 Medium, 600 SemiBold, 700 Bold, 800 ExtraBold, 900 Heavy.
- Default body: 14px / 20px.
- Table body and form labels: 14px / 20px.
- Secondary/helper text: 12px / 18px.
- Table header text: 14px / 22px, medium weight.
- Page title: 24px / 36px, semibold.
- Section title: 18px / 28px, semibold.
- Metric number: use 24px to 32px for normal cards; only dashboard hero metrics may go larger.
- Do not use display-size type for normal workbench pages.

Shape:
- Large module card radius: 8px.
- Data display small card radius: 4px.
- Input/button radius: 4px to 8px.
- Status pill radius: 4px or small pill only where source uses status tags.
- Avoid 16px+ radius for normal admin cards.
- Normal large cards should not show visible gray borders. List/work cards should be plain white with no shadow.
- Data metric cards may use source-derived frosted fill; do not apply the same frosted treatment to list/work cards.
- Selected or form focus states may use a soft blue glow only when needed; avoid default black browser outlines.

## Icon Asset Contract

All functional icons must come from `assets/icons/`. This applies platform-wide: sidebar arrows, top-bar controls, table actions, form hints, status/feedback icons, dialog/drawer close controls, empty-state icons, and any other icon-like affordance. Do not draw new SVGs, use emoji, use unicode symbols/arrows/question marks, use Lucide/manual icons, use CSS-only icons, or use text characters as pseudo icons.

Use semantic matching:
- Search: `搜索.svg`
- Dropdown / expand down: source asset `箭头-向下.svg`; static-demo browser-safe alias `arrow-down.svg`
- Collapse up: source asset `箭头-向上.svg`; static-demo browser-safe alias `arrow-up.svg`
- Previous / back: `箭头-向左.svg`
- Next / forward: `箭头-向右.svg`
- Add: `新增.svg` or `增加.svg`
- Edit: `编辑.svg`
- Delete / remove: `删除.svg` or `移除.svg`
- Warning / info / success / error / waiting: use the matching `警告.svg`, `信息.svg`, `正确、成功.svg`, `错误、失败.svg`, `等待.svg` or the `线性-*` version.
- Help / explanation / section-title hint: use `线性-疑问.svg`.
- File / image / screenshot / guide / feedback: use `文件.svg`, `图片.svg`, `截图.svg`, `查看截图.svg`, `指南、教程.svg`, `反馈、对话.svg`.

Icon usage:
- Default functional icon size is 16px; compact table/select icons may be 12px; empty states may use 20px or 24px.
- Icons from `assets/icons/` may be recolored through `currentColor`, inline SVG, CSS filter, or CSS mask. Do this when the same functional icon needs a token color.
- For `static-demo` HTML opened through `file://`, use browser-safe ASCII icon aliases when available, such as `arrow-down.svg`, `arrow-up.svg`, and `close.svg`. Keep the Chinese source files as design asset references, but avoid Chinese filenames in demo HTML/CSS URLs.
- Do not rely on CSS `mask: url(svg)` for critical static-demo icons such as sidebar arrows and modal close unless it has been visually verified in the target browser. Prefer `<img>` or `background-image: url(...)`; recolor simple monochrome icons with `filter` when needed.
- Sidebar expand/collapse arrows must use the provided arrow SVGs recolored to white; do not use the asset's default gray fill there.
- Icon containers should be transparent by default unless the source screen explicitly shows a filled icon button, badge, status tag, or selected state. Do not leave residual pale blue circles, chips, badges, button backgrounds, or hover fills behind standalone informational icons.
- If an icon needs a clickable hit area, keep the visual icon from `assets/icons/` and apply hover/focus to the control intentionally. Do not let default button backgrounds, text glyphs, or temporary placeholders remain visible.
- If a needed functional icon is missing, use text-only or mark it as an icon gap. Do not invent a replacement icon.

## Page Shell Rules

Use this shell for standard pages:
- Left side nav is fixed-width, 220px, using `linear-gradient(180deg, var(--nav-gradient-start), var(--nav-gradient-end))`.
- The top-left platform logo uses `assets/supervision-platform-logo-2x.png`, a 48px 2x PNG normally rendered at 24px by 24px beside the system name.
- Top bar is 56px high, 60% white translucent, with 6px background blur. The page background image remains visible behind it. Put organization selector on the left and todo/message/account on the right.
- Apply `--theme-bg-image` to the right-side main/content region itself, not to `body` or the full `.app` shell. Size it with the right region width, such as `background-size: 100% auto`, not `calc(100vw - 220px)`, so shrinking the viewport while the 1366px minimum canvas remains active does not shift the image relative to content.
- Main content starts below top bar and to the right of the nav, filling all remaining width.
- Left navigation and the right content region are independent scroll areas. Scrolling over the left nav must not move the right content; scrolling over the right content must not move the left nav.
- If the left navigation content does not exceed the viewport height, it must not show or simulate scrolling. If it exceeds the viewport height, only the nav list scrolls inside the 220px nav region.
- The right content region owns page/workbench scrolling. Do not put full-page scrolling on `body` when it couples nav and content movement.
- Page title sits near the top of content, usually 24px.
- Business scope tabs may sit beside or under the page title. The outer frame uses the same frosted surface as data metric cards: 60%-to-100% white vertical gradient, 1px inner white stroke, and 6px background blur. It must not have an outer shadow. Use equal internal spacing on all sides; for a 40px outer frame, use a 32px inner tab button and 4px spacing on all sides. The stroke must be inner stroke and must not consume layout space. They use a sliding active indicator, and clicking a tab must update both selected state and the content below.
- Primary work area is one integrated plain white work card that contains both filters and the table/detail content. Do not split filters and table into two separate cards for standard list pages.

Do not:
- Center the whole app like a website.
- Replace side nav with a top-only marketing nav.
- Use only the source-like subtle light-blue background image layer behind content; avoid decorative full-bleed backgrounds unrelated to the Sketch source.
- Make content cards float with large gaps just for visual effect.

## Component Rules

### Navigation

Left navigation:
- Width: 220px.
- Background: vertical gradient from `--nav-gradient-start` to `--nav-gradient-end`; do not derive it from Brand tokens.
- It is its own scroll container only when menu content exceeds viewport height.
- Item height: 40px.
- First-level and second-level items should align cleanly.
- Hover state uses white 8% translucent overlay through `--theme-nav-hover`, with no left indicator.
- Selected state follows the detail-page sidebar style: white 12% translucent overlay through `--theme-nav-active`, white text, medium weight, and a 3px white left indicator with `0 2px 2px 0` radius. Do not use a bright Brand-blue full-row fill for sidebar selection.
- Icons are 16px when used.

Top bar:
- Height: 56px.
- Background: translucent white with `backdrop-filter: blur(6px)` or equivalent.
- Keep account block compact.
- Use separators sparingly.
- Avoid oversized avatars or notification widgets.

Interaction states:
- Every clickable control must have a hover state: side navigation items, buttons, selects/dropdowns, dropdown options, tabs, pagination, table links, and row actions.
- Hover states should be restrained: slight token-based color, background, border, shadow, or opacity changes. Do not use large movement, glow-heavy effects, or decorative animation.
- Disabled controls do not need hover feedback and should keep the disabled cursor.
- Focus states must be visible and tokenized for keyboard users; do not rely on browser-default black outlines.
- Popup components such as Select, Dropdown, Date/Time Picker, Tooltip, Popconfirm, Modal, and Drawer must close with Escape when safe and return focus to the trigger.
- Disabled or permission-blocked actions should be hidden when possible. If visible for explanation, show a Tooltip reason and keep the action non-executable.

### Buttons

Follow the Dorami Button protocol, including the extracted `3.2 按钮` sizing, minimum-width, padding, radius, hierarchy, and state rules. In `static-demo` or `figma-like` output, reproduce the button structure, states, and supervision theme without requiring Vue. In `vue-dorami`, use real Dorami Button.

Use three button heights:
- 28px for table row actions.
- 32px for compact actions.
- 40px for filter/search and main form actions.

Button sizing:
- Button width adapts to text, but very short labels use the Dorami minimum-width rule instead of shrinking only to side padding.
- Minimum width must stay between 1.5x and 3x the button height; use the component protocol preset ladder when no supervision override exists.
- Keep horizontal padding and icon-text spacing on a 4px rhythm.
- Follow the Dorami protocol exact mappings for font size, minimum width, icon-text minimum width, and horizontal padding. For example, 32px buttons use 14px text, 64px text-only minimum width, and 12px left/right padding.

Primary:
- Blue/indigo fill, white text.
- Use only for the main action: search, submit, supervise, confirm.
- In each table row action group, at most one button may use the filled primary style. A row may also have no primary button.
- If multiple row actions could be primary, choose the highest-priority business progression action and render the rest as secondary or danger text buttons.
- Table operation-column actions must use filled or outline Dorami protocol buttons, not text-only/link-style buttons. Use 28px compact buttons for row operations; normal view actions such as `查看` should use an outline secondary button (`dcp-button secondary small` in static demos), while the main progression action may use a filled primary button.

Secondary:
- White or very light fill.
- Gray border and dark text.
- Use for reset, view, cancel, secondary row actions.

Danger text buttons:
- Withdraw, delete, remove, revoke, reject, and similar risk operations use `--theme-danger` for button text.
- Keep the surface white/light and avoid full red filled buttons unless the operation is a destructive primary confirmation.

Button groups:
- Common pair width: about 120px to 160px total.
- Keep primary and secondary visually balanced.
- Do not use large icon-only buttons for core business actions unless the source does.

### Table Operation Buttons

Use this as the table/list action contract: `DS-COMP-TABLE-003`.

Scope:
- Applies to all data tables, list pages, embedded tables inside dialogs/drawers, top table toolbars, row actions, and batch actions.
- Does not apply to form footer submit buttons, navigation actions, or non-table page-level actions.

Core principles:
- Single primary action is mandatory: in the same row or toolbar, use at most one primary button. If there is no clear core action, use only secondary buttons.
- Button hierarchy must match priority, frequency, and risk. High-risk reverse operations such as delete, disable, reject, revoke, withdraw, void, and remove must not use primary styling.
- The same business action must keep the same level, style, and interaction logic across tables.
- Show high-frequency operations first. Put low-frequency actions into a `More` dropdown to reduce row density.

Table action levels:
- Primary: low-risk positive core actions such as add, confirm, approve, edit, or the highest-frequency detail action when business priority makes it the main path.
- Secondary: neutral actions such as view details, export, copy, reset, download, share, refresh, column settings, and ordinary detail entry.
- Danger secondary: high-risk reverse actions such as delete, disable, reject, revoke, withdraw, void, and remove. Use danger text/border, not solid danger fill.

Top toolbar actions:
- Primary may be used for add, import, query, and batch approve/pass.
- Batch delete, batch disable, and batch reject must be danger secondary, never primary.
- Secondary actions include export, refresh, column settings, and reset.
- Keep positive action group and dangerous action group separated by 16px when they appear in the same toolbar.

Row actions:
- Row operation buttons use small table buttons only: 28px in compact mode or 32px in standard mode. Do not enlarge row buttons to create hierarchy.
- Height: 28px / 32px. Horizontal padding: 12px. Radius: 4px. Font size: 12px / 13px for table operation buttons unless the product theme explicitly chooses Dorami's 14px 32px-button default.
- Row action group: primary buttons <= 1; total visible buttons <= 3. Extra actions go into `More`.
- If a row has only one weak action such as view or copy, use secondary button or text link; do not use primary.
- Left-aligned operation column order: primary -> secondary -> danger secondary -> More.
- Right-aligned operation column order: More -> danger secondary -> secondary -> primary.
- Same-level row buttons use 8px horizontal spacing. If wrapping is unavoidable, keep the same 8px vertical spacing.
- `More` menu items are ordered by priority from top to bottom. Dangerous actions sit at the bottom with a divider above them.

Table operation button tokens:
- Primary: background `--theme-primary`, text white, hover `--theme-primary-hover`.
- Secondary: transparent/white background, 1px `--theme-border` or component secondary border, primary/dark hover border, subtle secondary fill on hover.
- Danger secondary: transparent/white background, 1px danger border, danger text, light danger hover background, danger hover border.
- Disabled state: use about 40% opacity and `cursor: not-allowed`.

Interaction:
- Button enabled/disabled/hidden state must follow row data status. For example, voided data disables edit.
- Primary async actions may show loading and lock repeated clicks. Secondary actions usually use toast/global feedback instead of independent loading.
- All danger secondary actions require second confirmation before execution.
- If the user has no permission, prefer hiding the action. If the reason must be explained, show it by Tooltip on hover.
- Primary action may support Enter shortcut when context is safe. Danger actions must not execute directly from shortcuts.

Special cases:
- Batch operations: only positive batch actions may be primary. Batch delete/disable/reject stay danger secondary.
- Empty data state: only keep add/create primary actions when useful; hide other batch operation buttons.
- Multi-status rows: the primary action may change by business status, but the same status must use the same rule everywhere.

Self-check:
- A row or toolbar must not contain two or more primary buttons.
- Delete/revoke/reject/disable must not appear as solid filled primary buttons.
- Do not display more than three direct row buttons; use `More` for overflow.
- A single weak action such as view must not become primary.

### Filters

Filter area:
- Sits above the table inside the same integrated work card.
- Filter Select, Input, Date/Time, and Button controls are 32px high.
- Distance from the card title to the filter row is 16px; distance from the filter row to the table is also 16px.
- Implement filter spacing as external layout spacing, not as padding inside a fixed-height filter control.
- Do not draw a divider line between the filter row and table header in standard list pages.
- Labels are 14px.
- Controls are 200px to 220px wide where possible.
- Date range, select, and text input should align on one baseline.
- Search and reset buttons sit at the end of the row.
- "展开" is a compact text/icon control, not a large button.

Expanded filters:
- Add a second row while keeping the same spacing.
- Do not turn expanded filters into a separate large card.

Select/dropdown controls:
- Follow the Dorami Select/Dropdown protocol. In `static-demo` or `figma-like`, reproduce the trigger, popup, option states, and supervision theme. In `vue-dorami`, use real Dorami Select or Dropdown.
- Use light gray borders in resting state.
- Focus should use a soft blue glow, not a black outline.
- Dropdown menus should appear as white floating panels with subtle gray shadow and 8px radius.
- Dropdown options use 4px vertical spacing between items.
- Top-bar dropdowns must render above the content area; set an explicit stacking layer when implementing code.
- Avoid native-looking black outlined dropdown popovers when creating custom UI mockups.
- Apply the same custom dropdown treatment to top-bar organization selectors and in-page filters.
- Filter selects must sync visible trigger text, internal value, selected menu option, and filtered table result.
- If filters include date/time, use a dedicated Date/Time Picker protocol. Do not fake date ranges as plain text unless the demo explicitly does not show opened picker behavior.
- Search executes with Enter only when focus is inside the filter form and no popup is open.
- Reset restores all filter controls, selected options, table data, pagination page, and metric counts together.
- Expanded filter rows preserve the same control height, label alignment, and keyboard order as the first row.

### Tables and Warning Records

The platform uses dense business records, often with complex rows rather than simple spreadsheet rows.

Table:
- Follow the Dorami Table protocol, then apply the supervision table rules below. In `static-demo` or `figma-like`, reproduce the table structure and states without requiring Vue. In `vue-dorami`, use real Dorami Table.
- Table responsive width is a hard constraint: the table must always follow the parent work-card width as the screen changes.
- Width: 100% of the parent work card; columns adapt within the fluid right content area.
- Table width must stay synchronized with the parent card width; do not let computed column widths exceed or underfill the card.
- Put tables inside a `width: 100%; max-width: 100%; overflow-x: auto;` table container so any unavoidable horizontal overflow stays inside the work card instead of bleeding outside the card or page.
- In flex/grid layouts, table containers, work-card children, and table cell content wrappers must allow shrinking with `min-width: 0` or an equivalent constraint; do not let intrinsic content width force the table wider than its parent.
- In adaptive tables, only the operation/action column may stay fixed when needed. Other columns should use percentage, `fr`, or equivalent proportional tracks so they expand and shrink together with the card.
- Do not fix multiple non-action columns to pixel widths in a way that disables responsive stretching.
- In `static-demo`, if JavaScript is used to sync column widths, calculate from the parent table container/work-card width, not from the current table width. Observe container resizing and recompute; do not write stale fixed pixel widths to non-action columns.
- Time and status columns may use no-wrap text, but their column widths should still participate in proportional table resizing unless the source screen explicitly requires a fixed width.
- Header height: 48px.
- Header background: pale gray-blue.
- Header has no top or bottom divider line.
- Header only rounds the top-left and top-right corners at 4px; bottom corners stay square.
- Column labels are compact and clear.
- Time/date values should use a dedicated table column. Do not place time under business identifiers such as warning number or supervision number.
- Standard table single-line rows are 56px high. Multi-line rows may auto-expand; keep vertical padding consistent rather than manually setting tall rows.
- Table body cells use 14px top and 14px bottom padding.
- Table cell content aligns to the first line/top. Extra text expands downward; do not vertically center multi-line cell content.
- Short fields such as status should stay on one line whenever possible.
- Operation buttons use a fixed operation column and must be filled or outline buttons rather than plain text buttons. Show at most 3 direct row action buttons; extra actions must move into `More`. If wrapping is unavoidable, keep consistent horizontal and vertical gaps.
- Do not add generic helper text inside table cells, such as "当前用户发起", unless it is required business data.
- Row dividers are subtle.
- Table and filter should share one parent work surface in list pages.
- Each large work card has only one visible title. Do not add a second table title inside the same card.
- Remove subtitle/helper copy under card titles unless the source explicitly needs it.
- Loading, empty, filtered-empty, and error states stay inside the table/work-card area and do not replace the whole page shell.
- Row hover is subtle and must not change action button layout or column width.
- If row selection is present, use Checkbox protocol and show an indeterminate header checkbox when only some rows are selected.
- Batch toolbar appears only when selection exists or when the page explicitly has batch actions. It follows `DS-COMP-TABLE-003`.

Warning record row:
- Use the standard 56px single-line row height; complex multi-line rows expand automatically.
- Use columns for warning number, related information, reason, sent time, status, and actions.
- Put risk level/status tags near the warning number.
- Use label-value pairs for business fields.
- Long business text should wrap in controlled columns, not force giant row gaps.
- Operation buttons use compact 28px buttons.

Status:
- Table status is a standalone Status Indicator component, not a Tag. Use a small colored dot plus text, such as `● 已通知`.
- In table status columns, do not use Tag visual styles: no filled background, no border, no rounded container, no tag padding, no close icon, and no `+N` folding.
- Status Indicator is read-only by default: no click feedback, no hover background, and no pointer cursor.
- Status Indicator uses `dcp-status-indicator`, `dcp-status-dot`, and `dcp-status-text` in static demos.
- Tag visual weight follows business importance and the Dorami Tag protocol:
  - Low/default: light fill. Use for list categories, ordinary attributes, and non-table summary labels.
  - Medium: outline. Use for secondary information, weak-emphasis metadata, notes, default/empty-like labels, and auxiliary attributes.
  - High: solid fill. Use only for key statuses, high-priority alerts, core result labels, severe failure, emergency warning, or other rare high-salience cases.
- Process statuses such as 已通知、已读、未读、处理中、已回复、已核实、已撤回 must use Status Indicator in table rows unless the source screen explicitly defines a different component.
- Avoid multiple solid-fill tags in one dense row. Solid-fill tags should stay below 20% of tags in the same visible region.
- If warning level and process status appear together, keep warning level as the stronger tag and render process status as dot plus text or light-fill tag.
- Common Tag height is 20px. Detail/card Tags may use 24px. Tag font size is 12px, horizontal padding is 6px, and radius is 4px.
- For a single data item, the same status dimension may show only one status tag.
- Category tags from the same dimension may show at most three inline; overflow becomes `+N` and reveals all hidden tags on hover/focus.
- Pure display tags have no click feedback or hover style. Closable tags use a right-side close icon and remove directly unless the business flow requires confirmation.
- Long tag text truncates with ellipsis and shows the full text in Tooltip on hover/focus.
- Disabled tags use about 40% opacity, cannot be clicked, and may show a Tooltip reason.
- Table row Status Indicators align left in the status column and must not mix with operation buttons.
- Do not use large badges or decorative alert cards inside table rows.

Metric cards:
- Use for data display only unless the user explicitly asks for clickable filtering.
- Do not add helper text such as "click to filter" by default.
- Do not add a separate section title above metric card rows when the surrounding page title already establishes context.
- Put the number first and the label below it.
- Do not show unit suffixes such as "项" inside metric cards unless the source explicitly displays them.
- Use 4px radius, vertical white 60%-to-100% gradient, 1px white border, and blur radius around 6px.

### Detail Pages

Detail pages should feel like a process dossier.

Use:
- Same shell as list pages.
- A clear page title and back/navigation affordance if needed.
- Section blocks with bordered description lists.
- Label column and content column patterns.
- Description-list rows must keep a consistent row height. Inline links and text-style buttons inside value cells, such as "查看" or business-detail links, must align to the normal text line-height and must not use a taller button height that makes only the link row taller than adjacent rows.
- In static demos, when a Dorami text button is placed inside a description-list value cell, scope its height/padding to the description cell, for example 20px line-height with no extra vertical padding. Do not globally shrink table operation buttons.
- Process, evidence, risk reason, supplier/project information, and handling result as separate sections.
- Empty states should be quiet and local to the relevant area.
- Description-list labels stay stable in width inside the same section. Long values wrap in the value area, not under labels.
- Description-list inline downloads, evidence links, and view actions use text/link protocol and keep hover/focus states.
- Process or flow records use Timeline protocol: actor, time, operation, remark, and attachment rows remain aligned and scroll inside their container when long.
- Timeline attachment actions follow Upload/File-list protocol; download is neutral, remove is danger and requires confirmation if it affects submitted evidence.

Avoid:
- Turning detail content into independent marketing cards.
- Huge hero summaries unless the source detail page uses one.
- Hiding dense business text behind excessive whitespace.

### Dialogs

Dialogs are business handling tools.

Use:
- Dorami Modal/Drawer protocol for the base overlay shell, including the extracted `7.8 对话框` and `7.10 侧滑抽屉` rules for width presets, content padding, close icon, footer actions, body scroll, and click-outside behavior. In `static-demo` or `figma-like`, reproduce the protocol shell and states; in `vue-dorami`, use real Dorami Modal or Drawer.
- Supervision theme tokens for modal/drawer surface, radius, mask, shadow, close icon asset, and footer button height.
- Clear business title.
- Compact business form, description, summary, attachment, or process-log content inside the Modal/Drawer body slot.
- Footer action wording and priority according to the business workflow: secondary cancel before primary confirm when a footer is needed.
- Width chosen by business content: small reason dialogs are narrower; detail/log dialogs can be wider.
- Keep business labels aligned and controls consistent with 32px or 40px input height.
- Confirmation dialogs are for single-step confirmation. Business handling dialogs with reason, attachments, or multi-field forms use Form/Input/Upload protocol inside the modal body.
- Dangerous modal confirmations use danger wording but still keep only one primary confirmation action unless the source spec says otherwise.
- Form dialogs validate required fields before submit, focus the first invalid field, and keep submit button loading while saving.
- Dialog body scrolls when content is long; header, close icon, and footer actions remain stable.
- Drawer detail workflows preserve table/list context behind them. Editing drawers do not close on outside click; read-only drawers may close on outside click when safe.
- Drawer footer actions follow table/form action priority: one primary at most, secondary before primary, low-frequency actions in More.

### Form, Upload, Tooltip, and Popconfirm

Form controls:
- Use Dorami Form/Input/Textarea/Checkbox/Radio/Date/Time/Upload protocols.
- Labels are compact and aligned; required marks are visible but not decorative.
- Errors show both visual state and text. Do not communicate validation only by red border.
- Checkbox/radio stay at component scale and must not inherit text-input width or height.
- Date/time fields use the same date/time format as table columns and detail records.

Upload and attachments:
- Evidence upload uses Upload protocol with file type/size hints when relevant.
- Uploading files show progress/loading and cannot be submitted twice.
- Failed uploads show reason and allow retry/remove when supported.
- Uploaded file rows keep filename, optional size/status, and allowed actions readable.

Tooltip and Popconfirm:
- Tooltip explains permissions, truncated text, or non-essential help only. Do not hide required business data in Tooltip.
- Popconfirm is allowed for simple row risks. Use Modal when the operation needs reason entry, attachment, irreversible business context, or stronger confirmation.
- Dangerous Popconfirm confirm actions use danger semantics and never execute through keyboard shortcut alone.

### Tabs and Business Switchers

Tabs/switchers:
- Business scope tabs follow Dorami Tabs/Switcher protocol and supervision frosted tab styling.
- Click, Enter, or Space changes active state and synchronizes the content below.
- Active tab is indicated by both fill/indicator and text state, not color alone.
- Switching business scope must reset or preserve filters intentionally; do not leave stale table state from the previous tab.

Avoid:
- Decorative modal art.
- Overlarge rounded modal corners.
- Full-screen blur-heavy overlays.
- Turning operation dialogs into cards with promotional styling.
- Rebuilding a custom modal/drawer shell inside a business page when the Dorami component protocol already defines it.

### Dashboard

Dashboard pages may be richer but still operational.

Use:
- Same platform shell.
- KPI cards, charts, and warning analysis cards.
- KPI/chart cards may use frosted white surfaces when they are data display modules; list/work cards remain plain white.
- Blue/green/orange/red chart accents.
- Compact card titles and clear numeric hierarchy.
- Charts should support supervision decisions, not decoration.

Avoid:
- Dark "command center" big-screen visual language unless explicitly requested.
- Neon gradients, 3D charts, decorative maps, or giant animated panels.
- Low-density executive landing pages.

### Empty States

Use quiet empty states:
- Small illustration or icon if needed.
- Short text.
- Optional primary action only when the user can act.
- Keep inside the current content area.

Do not:
- Make empty states dominate the entire page.
- Use cartoon-heavy or consumer-style empty illustrations.

## Best Case Rules

Treat `/best` as the preferred direction, but adapt it to the stricter supervision platform shell.

Extract these principles:
- Use soft blue-gray backgrounds and clean white surfaces.
- Use source-derived frosted white surfaces and subtle blur where the Sketch uses it.
- Keep card hierarchy calm and readable.
- Use blue as a focused action color, not as page-wide decoration.
- Make dense information feel organized through alignment, spacing, and sectioning.
- Prefer crisp functional modules over visual noise.
- Keep data cards and operation cards lightweight.

When a best case conflicts with the supervision platform source, the Sketch/source screenshots win.

## Bad Case Prohibitions

Treat `/bad` as a hard warning set.

Do not generate:
- Washed-out multi-color gradients behind business content unless they are the source-derived fixed top JPG background layer.
- Red/green/pink risk backgrounds spread across large areas.
- Blurred, low-contrast, or glow-heavy panels.
- Large decorative background washes that reduce readability.
- Unstable card spacing and irregular alignment.
- Consumer dashboard styling that weakens official supervision credibility.
- Dense text placed on tinted backgrounds without clear structure.
- Risk cards that look emotionally alarming instead of operationally actionable.

If the generated screen starts to resemble a bad case, revise by:
- Removing decorative gradients.
- Returning to source-derived frosted white surfaces, fixed top JPG background, and Brand-1 bottom background.
- Using small status tags instead of full-panel color fills.
- Tightening alignment, table structure, and label-value grouping.

## Generation Patterns

### List Page Pattern

Use for warning query, supervision task list, data collection list, risk record list:

1. Page shell with left nav and top bar.
2. Page title and optional tabs.
3. Plain white integrated work card without visible gray card border or shadow.
4. Filter row inside the same work card with labels, selects/date ranges, reset/search, optional expand.
5. Table header inside the same work card, without a second table title.
6. Dense warning rows or standard table rows.
7. Pagination at bottom of the same work card.

Required checks:
- Table/card width is fluid within the right content area and stops shrinking at the 1366px total-page minimum.
- Filters and table are integrated in one parent work card.
- One card has one title; subtitles are omitted by default.
- Filters do not become decorative.
- Row actions are compact.
- Status is easy to scan.

### Detail Page Pattern

Use for warning detail, risk verification detail, complaint/question detail:

1. Page shell.
2. Title/back area.
3. Summary section if needed.
4. Business information section.
5. Risk/reason/evidence section.
6. Process log or handling result section.
7. Footer actions only when needed.

Required checks:
- Detail sections are clearly separated.
- Labels and values align.
- Long text remains readable.
- Empty data uses quiet placeholders.

### Dialog Pattern

Use for withdraw, return reason, initiate supervision, feedback, verify completion:

1. Dorami Modal/Drawer protocol shell.
2. Supervision theme tokens applied to the shell.
3. Business title.
4. Compact business form, summary, attachment, process log, or description content.
5. Footer actions only when the workflow needs confirmation or submission.

Required checks:
- Modal/Drawer shell comes from the Dorami component protocol, not a one-off business component.
- Business content is functional, not decorative.
- Primary action is obvious.
- Cancel/secondary action is quiet.
- Inputs use platform height and radius.

### Dashboard Pattern

Use for warning monitoring and analysis:

1. Page shell.
2. Top time/filter selector if needed.
3. KPI cards.
4. Chart cards.
5. Ranking or risk distribution cards.
6. Keep all cards operational.

Required checks:
- Dashboard remains a supervision workbench.
- Charts are readable at a glance.
- Metrics do not become oversized marketing numbers.

## Output Contract

When answering a UI generation request, use this structure:

1. `页面理解`
   - List page name, page type, business object, user role, core goal, fields, actions, states, and TODOs.

2. `结构规划`
   - List selected page pattern, reading order, page regions, loading/empty/error/permission states, and any mixed workflow steps.

3. `组件映射`
   - Map each business region, field, status, and action to the supervision business component and Dorami base protocol.

4. `本次复用的监管平台规范`
   - List the exact shell, layout, color, component, and page-type rules being used.

5. `本次复用的组件交互规则`
   - List the exact component protocols used, such as Button, Table, Select, Modal, Drawer, Form, Upload, Tooltip, Popconfirm, Tabs, Menu, Timeline, or Empty.

6. `界面方案`
   - Describe the generated page structure or implement the requested frontend/Figma-like output.

7. `一致性自检`
   - Check each item below and revise before finalizing if any answer is no.

Consistency checklist:
- Preserves the requested business fields, actions, statuses, page routes, mock-data meaning, and workflow entry points.
- Includes the compiled page blueprint or equivalent page understanding before generation.
- Maps risk, lifecycle, approval, data, and permission states to the correct business display component.
- Uses table Status Indicator for lifecycle statuses by default and reserves Tag for risk level, categories, and high-salience labels.
- Uses RowActionGroup, ToolbarActionGroup, Popconfirm, Modal, or Drawer according to business risk and action complexity.
- Uses the 220px left nav and 56px top bar when generating a full page.
- Keeps left navigation and right content as independent scroll areas; the nav does not scroll when its content fits.
- Uses `dorami-ui-protocol` as the base control protocol: `static-demo` by default, `figma-like` for editable visual output, and `vue-dorami` only when explicitly requested.
- Defines tokens in Raw / Theme / Component order and avoids hard-coded colors when a token exists.
- Uses theme tokens, especially `--theme-primary`, `--theme-nav-start`, `--theme-nav-end`, `--theme-bg`, and `--theme-surface`.
- Uses `--dcp-*` component tokens for Dorami protocol control styling instead of one-off component shell CSS.
- Uses functional icons only from `assets/icons/`; no hand-made arrows, emoji, Lucide icons, or inline SVG replacements.
- Uses 14px as the main font size for body, table, and form text; do not describe this as "14px information density".
- Uses D-DIN-PRO from `assets/fonts/` for all English letters and numeric glyphs through the `--font-alphanumeric` / `--font-number` tokens.
- Uses 8px or smaller standard radius for normal cards and controls.
- Uses filter/table/detail/dialog patterns from this skill.
- Lists the component interaction protocols used before generation.
- Every interactive control has hover, focus, disabled, and active/selected states where applicable.
- Popup components have open/close behavior, Escape close where safe, outside-click behavior where safe, and correct z-index.
- Keyboard behavior is covered for buttons, tabs, menus, dropdowns, pagination, modal/drawer close, and form submit.
- Dangerous actions require confirmation and never use solid primary styling unless they are final destructive confirmation actions.
- Loading, empty, error, and permission states are defined for tables/forms/actions when relevant.
- More menus are used when row or toolbar actions exceed the direct-action limit.
- Modal/drawer scroll behavior keeps header, close control, and footer actions stable.
- Responsive table behavior keeps overflow inside the work card and keeps non-action columns proportional.
- Uses source-derived frosted metric cards, fixed top JPG background, and Brand-1 bottom background, while keeping list/work cards plain white and avoiding decorative glassmorphism, marketing hero layout, and big-screen styling.
- Keeps information density close to the source screenshots.
- Uses best cases for calm hierarchy and bad cases as hard prohibitions.
- Lists unresolved TODOs instead of inventing missing business facts.

If implementing frontend code:
- Encode the tokens as CSS variables or theme constants.
- Keep layout dimensions explicit.
- Build reusable components for shell, filters, table rows, status tags, dialogs, and dashboard cards.
- In `static-demo`, use `dcp-*` protocol classes for base controls rather than one-off handmade component classes.
- Do not introduce a third-party component visual style that conflicts with this contract.

If creating Figma-like output:
- Prefer editable rectangles, text, groups, and components over flat screenshots.
- Match source dimensions and component proportions before adding polish.
- Use source screenshot import only as a visual reference, not as the final editable design.

## Versioning

- `v0.1.0`: Initial platform contract from Sketch and screenshot assets.
- `v0.2.0`: Add source-derived frosted surfaces, sidebar gradient, translucent top bar, integrated filter/table work card, and custom dropdown guidance.
- `v0.3.0`: Clarify metric cards versus large work cards, non-clickable metrics by default, number-first metric layout, and shared custom dropdown treatment.
- `v0.4.0`: Add intelligent supervision theme color tokens with Brand-1~10, Gray-1~10, semantic theme tokens, and the rule that all new colors must be tokenized before use.
- `v0.5.0`: Add Dorami component library icon assets and require every functional icon to reference `assets/icons/` instead of self-made icons.
- `v0.6.0`: Add the fixed top `assets/bg.jpg` background rule with Brand-1 as the bottom/fallback color to avoid long-page image breaks.
- `v0.7.0`: Add dedicated sidebar gradient tokens and stop deriving side navigation colors from Brand tokens.
- `v0.8.0`: Clarify one-title-per-card, omit subtitles by default, and remove metric unit suffixes unless source requires them.
- `v0.9.0`: Set sidebar gradient tokens to `#181C4F` -> `#394183` from top to bottom.
- `v0.10.0`: Add adaptive layout rules: fixed 220px sidebar, fluid right content, module width follows page width, and 1366px minimum total width.
- `v0.11.0`: Add table header corner/divider rules, require top-bar dropdowns to layer above content, and require business tabs to slide and sync content.
- `v0.12.0`: Clarify adaptive table columns: action column stays fixed, all other columns stretch proportionally.
- `v0.13.0`: Clarify recolorable icon usage and require white sidebar expand/collapse arrows.
- `v0.14.0`: Remove the divider line between standard list filters and table headers.
- `v0.15.0`: Align business scope tab outer frame with metric-card frosted surface.
- `v0.16.0`: Move background image origin to the top of the right main region and define the top bar as 60% white with 6px blur.
- `v0.17.0`: Require restrained hover states for all clickable controls.
- `v0.18.0`: Require time/date values to be separate table columns, not secondary text under identifiers.
- `v0.19.0`: Set standard table single-line row height to 56px, with auto expansion for multi-line rows.
- `v0.20.0`: Remove generic non-business helper text from table cells by default.
- `v0.64.0`: Add page compiler rules, business semantics, field/status/action mapping, and the page understanding -> structure planning -> component mapping -> generation -> consistency-check output contract.
- `v0.21.0`: Set filter spacing to 16px from the card title and 16px to the table.
- `v0.22.0`: Add synchronized table/card width, top-aligned table cells, no-wrap short status fields, and capped two-row action buttons.
- `v0.23.0`: Add 4px spacing between dropdown options.
- `v0.24.0`: Use danger-colored text for withdraw/delete/revoke-style action buttons.
- `v0.25.0`: Limit each row action group to at most one filled primary button, with no primary button allowed.
- `v0.26.0`: Clarify filter spacing must be true external spacing, not padding inside the fixed-height filter row.
- `v0.27.0`: Align dialog style: no internal divider lines, 32px footer buttons, and icon-only close control.
- `v0.28.0`: Add `assets/icons/关闭.svg` and require it for all dialog/drawer/overlay close controls.
- `v0.29.0`: Add Dorami integration rules and make Dorami the preferred base component layer for supervision UI.
- `v0.30.0`: Reframe Dorami as a technology-neutral component protocol; default supervision demos to `static-demo` and reserve `vue-dorami` for explicit production implementation requests.
- `v0.31.0`: Add D-DIN-PRO numeric font assets and require all numeric glyphs to use the `--font-number` token.
- `v0.32.0`: Clarify business scope tab spacing: inner tab padding must be equal on all sides.
- `v0.33.0`: Correct business scope tab dimensions: outer frame remains 40px, inner button is 32px, spacing is 4px on all sides, and the 1px stroke must be inner stroke that does not consume layout space.
- `v0.34.0`: Require static demos to use Dorami protocol `dcp-*` class hooks for base controls such as button, select, table, pagination, and modal.
- `v0.35.0`: Add browser-safe ASCII icon aliases for static-demo HTML so `file://` preview does not fail on Chinese SVG filenames.
- `v0.36.0`: Avoid CSS mask for critical static-demo icons by default; prefer image/background SVG aliases so sidebar arrows and modal close icons render reliably in browser preview.
- `v0.37.0`: Clarify ownership split: Dorami protocol owns base Modal/Drawer/control shells, supervision theme changes atomic tokens, and this skill only owns business layout/content inside component slots.
- `v0.38.0`: Set table body cell vertical padding to 14px top and 14px bottom.
- `v0.39.0`: Adopt the lightweight Raw / Theme / Component token system and require pages to use Theme tokens while Dorami protocol controls use `--dcp-*` Component tokens.
- `v0.40.0`: Require English letters as well as numeric glyphs to use D-DIN-PRO, while Chinese text continues to use the normal Chinese UI font.
- `v0.41.0`: Require left navigation and right content to be independent scroll areas, with no nav scrolling when menu content fits.
- `v0.42.0`: Require description-list inline links and text buttons to preserve row height instead of inheriting taller button heights.
- `v0.43.0`: Expand icon rules to all platform icon-like affordances, forbidding text/unicode/CSS pseudo icons and unintended residual icon backgrounds.
- `v0.44.0`: Add tag importance hierarchy and require warning/risk level tags to use filled color backgrounds with white text.
- `v0.45.0`: Require tables to use an internal overflow container and fixed-width time/status/action columns so responsive shrink does not bleed outside the work card.
- `v0.46.0`: Align sidebar selected state with detail-page demo: translucent nav overlay plus 3px white left indicator, not bright Brand-blue fill.
- `v0.47.0`: Clarify sidebar interaction states: hover is white 8% translucent overlay without indicator; selected is white 12% translucent overlay plus indicator.
- `v0.48.0`: Make the skill portable by bundling Sketch and screenshot references under `references/` and replacing Desktop absolute paths with relative asset paths.
- `v0.49.0`: Bundle the platform logo asset and require shell demos to render it at the appropriate 24px visual size beside the system name.
- `v0.50.0`: Require table operation-column actions to use filled or outline compact buttons instead of text-only/link-style buttons.
- `v0.51.0`: For supervision static-demo updates, default to capturing reusable rules in this skill and require all sidebar functional icons to render as unified white linear icons.
- `v0.52.0`: Require static-demo input normalization to exclude checkbox/radio controls and style checkboxes separately at Dorami component scale.
- `v0.53.0`: Require the right-side background image to be attached to the right main/content region and sized by that region, preventing viewport-shrink displacement.
- `v0.54.0`: Require table operation buttons to use standard Dorami Button protocol modifiers such as `secondary small`, not ad hoc row-action classes.
- `v0.55.0`: Make table responsive width a hard constraint; only the operation column may stay fixed, while all other columns resize proportionally with the work card.
- `v0.56.0`: Link supervision pages to the newly extracted backend component rules for Button, Tag, Modal, and Drawer, especially button minimum width and overlay shell behavior.
- `v0.57.0`: Add exact button screenshot rules and the `DS-COMP-TABLE-003` table operation button contract, including one-primary-only, danger secondary actions, max three direct row buttons, and More-menu overflow.
- `v0.58.0`: Add full component interaction coverage workflow, expanded base-control ownership, supervision business interaction rules, and interaction self-checks for hover, focus, disabled, loading, popups, keyboard, More menus, scroll, and responsive behavior.
- `v0.59.0`: Add detailed Tag usage rules for light/outline/solid visual weight, tag count limits, non-interactive display tags, closable tags, truncation tooltip, disabled tags, and table tag folding.
- `v0.60.0`: Separate table row status into Status Indicator; table statuses use dot-plus-text and must not use Tag visual styles by default.
- `v0.61.0`: Require business scope tab outer frames to use frosted fill plus inner stroke only, with no outer shadow.
- `v0.62.0`: Set all filter-area Select, Input, Date/Time, and Button controls to 32px height.
- `v0.63.0`: Clarify static-demo table column syncing: calculate from the parent container width, observe container resizing, keep only the operation column fixed, and prevent intrinsic cell content from forcing table overflow.

Update the `Skill Version` line whenever behavior changes.
