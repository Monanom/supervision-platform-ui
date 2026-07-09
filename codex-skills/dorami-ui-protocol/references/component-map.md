# Dorami Component Protocol Map

Use these mappings when generating or reviewing base UI controls. Treat each item as a component protocol that can be rendered as static HTML/CSS/JS, Figma-like editable UI, or real Vue/Dorami code.

## Stack Mapping

- `static-demo`: build semantic HTML, `dcp-*` protocol classes, ARIA where useful, and minimal JS for open/close/select/page/tab behavior. Do not import Vue.
- `figma-like`: create editable component-like groups that preserve structure, sizes, states, and visual hierarchy.
- `vue-dorami`: use real `@zcy/dorami` components and map product tokens through theme variables or wrapper classes.

Use these static-demo class hooks for protocol controls:
- Button: `dcp-button`
- Tag: `dcp-tag`
- Input: `dcp-input`
- Select/Dropdown: `dcp-select`, `dcp-select-menu`, `dcp-option`
- Table: `dcp-table`
- Pagination: `dcp-pagination`, `dcp-page-button`
- Modal: `dcp-modal-mask`, `dcp-modal`, `dcp-modal-head`, `dcp-modal-body`, `dcp-modal-foot`, `dcp-modal-close`
- Drawer: `dcp-drawer-mask`, `dcp-drawer`, `dcp-drawer-head`, `dcp-drawer-body`, `dcp-drawer-foot`, `dcp-drawer-close`

## Tag

Protocol:
- Tag is a compact, non-interactive status or category label.
- Standard tag height is 20px, border radius is 4px, and text is 12px centered vertically.
- Filled color tags use solid color backgrounds with white text.
- Light color tags use pale backgrounds with colored text.
- Neutral tags use gray backgrounds with gray text.

Implementation:
- `static-demo`: use `<span class="dcp-tag">` with modifiers such as `filled`, `light`, `warning`, `success`, `danger`, `info`, or `neutral`.
- `figma-like`: create editable variants for filled, light, and neutral states.
- `vue-dorami`: use the Dorami Tag component and map product colors through theme variables.

Rules:
- Choose tag visual weight by information importance:
  - Level 1 / high salience: filled color tag, solid background with white text. Use for risk levels, warning levels, severity, failure states, or labels that must be seen before surrounding text.
  - Level 2 / medium salience: light color tag, pale background with colored text. Use for secondary classifications, business categories, record types, or table scanning aids.
  - Level 3 / low salience: neutral tag, gray background/text or plain muted text when a tag shape is unnecessary. Use for ordinary metadata, inactive values, and low-priority labels.
- Do not use multiple Level 1 filled tags in the same dense row unless the source screen or business priority requires competing high-salience labels.
- Do not use tags as action buttons. If clickable behavior is needed, use Button or Link protocol.
- Do not let tag padding or line-height change surrounding table or description-list row height.

## Button

Protocol:
- Primary button: filled theme color, white text, hover/active/disabled/loading states.
- Secondary button: light or white fill, border, dark text, hover border/background state.
- Danger text/outline button: danger-colored text for withdraw, delete, revoke, reject, or remove actions; avoid full red fill unless confirming destructive action.
- Icon-only button: use the product icon source or Dorami icon mechanism; include hover/focus/disabled states.
- Button hierarchy supports these authoring levels: primary, secondary, tertiary, primary text, secondary text, and link-style text. Each operation area should normally use only two or three hierarchy levels.
- Button attributes can combine with the hierarchy: icon, danger, dashed, inverse, and ghost.
- Button interaction states must include normal, hover, active, loading, and disabled.

Implementation:
- `static-demo`: use `<button class="dcp-button">` with protocol modifiers such as `primary`, `danger`, `loading`, and `disabled`.
- `figma-like`: create variants for default, hover, active, disabled, loading if the output supports variants.
- `vue-dorami`: use Dorami Button props such as primary/default/danger/loading/disabled.

Rules:
- Row action priority is decided by the business skill.
- Each operation area should have at most one primary button.
- Global page actions such as save/cancel usually use a primary action plus a secondary or tertiary action.
- Module actions such as filter query/reset usually use a primary or secondary action plus a quieter reset action.
- Local dense actions such as table operation columns, cards, and inline links should prefer text/link-style buttons.
- Danger buttons are for deletion, moving, permission change, and other risky operations; clicking them usually requires second confirmation.
- Dashed buttons are normally for adding items in a list and may span the list/content width.
- Inverse buttons are for primary-color backgrounds. Ghost buttons are for complex colored, image, textured, or dark backgrounds where the button surface should stay transparent.
- Use the small/medium/large size set from the active product theme. Common Dorami heights are 28px, 32px, and 40px; product themes may map the set to 28px, 36px, 44px or other approved sizes.
- Button min width should stay proportional to height: about 1.5x to 3x the button height. Let normal buttons grow with text while keeping fixed horizontal padding.
- Keep text/icon spacing and horizontal padding on a 4px rhythm when product rules do not override it.
- In button groups, place secondary actions before the primary action so the primary action appears on the right. Default group gap is 8px unless the product theme overrides it.
- Avoid more than four visible buttons in one operation area. When actions are many, move the third or fourth and lower-priority actions into a dropdown or "more" menu.
- Keep button radius consistent within a product. Product themes may override radius, but arbitrary one-off radius is not allowed.
- Do not hand-roll one-off button visuals outside the protocol.

## Modal

Protocol:
- Structure: mask, centered dialog, header title, icon-only close, body, footer actions.
- Base shell: white/elevated dialog container, no internal divider lines by default, content padding around the shell, close control positioned as a 32px icon button near the top-right, body as the scrollable content region when height is constrained, and footer actions aligned to the right.
- Title region: compact title text, no oversized header bar.
- Footer region: secondary actions before the primary action, consistent button gap, and no footer divider by default.
- Confirm modal: secondary cancel and primary confirm in footer.
- Form modal: body contains Form/Input/Select protocol controls.
- Close control: icon button, not a text button, when required by the product theme.
- Dialog types include basic content dialog, confirmation dialog, feedback/result dialog, and form dialog.
- Basic content dialogs are for text or simple content blocks. Standard widths are 580px, 780px, and 980px.
- Dialog content padding is 20px on all sides unless the product theme or source screen explicitly changes it.
- Confirmation dialogs guide a second confirmation and usually include cancel plus one primary action.
- Feedback/result dialogs can show an icon/status in the title or content area and are used for operation result, danger, warning, or notice messages.
- Feedback/result dialog copy should keep a readable text measure; long explanatory text should wrap rather than stretch the dialog.
- Dialogs may support an optional checkbox such as "do not remind again" when the workflow requires it.
- Form dialogs must keep label/control alignment balanced. If label width varies greatly or there are many fields, use a vertical label-over-control layout instead of forcing a cramped two-column label row.

Implementation:
- `static-demo`: use `dcp-modal-mask` and `dcp-modal` HTML with open/close JS, `aria-hidden`, `role="dialog"`, keyboard Escape, and mask-click close when practical.
- `figma-like`: use grouped overlay layers and editable text/control groups.
- `vue-dorami`: use Dorami Modal slots/props and product theme overrides.

Rules:
- Avoid decorative art, marketing panels, and unnecessary internal divider lines.
- Product theme decides modal radius, shadow, mask color, close icon asset, and footer button height through tokens.
- Business skill decides modal purpose, title, content slots, form fields, summary blocks, attachments, logs, and action wording.
- Use confirmation dialogs for irreversible, risky, or business-sensitive actions instead of relying only on Popconfirm.
- Do not overload feedback/result dialogs with complex forms or long workflows; switch to Drawer when content becomes workflow-like.
- Do not rebuild a different modal shell inside a business skill.

## Drawer

Protocol:
- Structure: mask, side panel, header title, icon-only close, body sections, optional footer.
- Base shell: fixed side panel, close control near the top-right, header/body/footer slots, body scroll when content exceeds the viewport, and optional sticky footer actions.
- Use for detail inspection, contextual forms, and long side workflows where list context should remain visible.
- Use Drawer for create, delete, edit, query, and other operation pages that can stay in context. Prefer Drawer over opening a new page when the workflow can be contained in a side panel.
- Drawer width variants include 400px, 640px, 880px, remaining width after the left menu, and full-screen. Pick width by content complexity, not decoration.
- Drawer can be white-background or gray-background. White background separates content with lines. Gray background should place content sections on white surfaces.
- Drawer content should keep about 20px spacing from left/right edges and from the title divider unless the product theme overrides it.
- Drawer header height is typically 56px. Header action spacing should be compact and consistent.
- Drawer may support full-screen, additional checkbox controls, and other workflow actions when needed.

Implementation:
- `static-demo`: use positioned side panel with open/close JS.
- `figma-like`: create editable panel sections.
- `vue-dorami`: use Dorami Drawer.

Rules:
- Product theme decides drawer radius when applicable, shadow, mask color, close icon asset, and footer button height through tokens.
- Business skill decides drawer purpose, width variant, section content, section density, and whether footer actions are needed.
- Close control follows the product overlay close icon token.
- Drawer defaults to no dark transparent mask unless the product or workflow explicitly requires a mask.
- Editing drawers must not close automatically when clicking outside the drawer. Read-only drawers may close on outside click when safe.
- Show at most one primary action in the drawer action area.
- When drawer actions exceed three visible buttons, move low-frequency actions into a "more" dropdown.
- Drawers can have no actions, up to three direct actions, or a primary/secondary/more structure. Keep action wording task-based.
- When drawer content is large or form-heavy, use grid/form structure to keep information aligned and scannable.

## Select and Dropdown

Protocol:
- Trigger: bordered control with label/value, arrow icon, hover/focus/disabled states.
- Popup: elevated white panel, option list, selected state, hover state, disabled state.
- Options can have product-specific spacing, radius, and shadow.

Implementation:
- `static-demo`: do not use native browser select for product visuals; use `dcp-select`, `dcp-select-menu`, and `dcp-option` with button-like trigger plus custom popup when visual fidelity matters.
- `figma-like`: show trigger and popup state when needed for review.
- `vue-dorami`: use Dorami Select, Dropdown, Cascader, or TreeSelect as appropriate.

Rules:
- Single-choice filters use Select.
- Command menus use Dropdown.
- Product theme controls popup spacing, radius, shadow, and token colors.

## Pagination

Protocol:
- Standard list footer: total count when useful, previous/next controls, numeric page items, active item, disabled state.
- Interaction states: hover, active, disabled.

Implementation:
- `static-demo`: use `dcp-pagination` plus `dcp-page-button` markup and JS for page state if interaction is required.
- `figma-like`: create editable active/disabled variants.
- `vue-dorami`: use Dorami Pagination.

Rules:
- Align according to the business skill, usually right aligned in dense table pages.
- Product theme controls active color, item height, and spacing.

## Table

Protocol:
- Structure: table container, header, body rows, empty state, optional pagination.
- Header and row density are controlled by the business skill.
- Operation column can be fixed while other columns stretch proportionally.
- Row actions use Button protocol.

Implementation:
- `static-demo`: use real `<table class="dcp-table">` when possible; use CSS variables or column definitions to keep widths synchronized.
- `figma-like`: use editable table groups and consistent column guides.
- `vue-dorami`: use Dorami Table with explicit columns and scoped renderers for business cells/actions.

Rules:
- Business skill decides row height, column ratios, action column width, top alignment, wrapping, and empty state tone.
- Do not mix business timing into identifier columns when the business skill defines a time column.

## Form and Input

Protocol:
- Form item: label, control, optional help/error text.
- Input controls: placeholder, hover, focus, disabled, error, and clearable states.
- Use Select, DatePicker, TimePicker, Radio, Checkbox, InputNumber, and Textarea protocols as needed.

Implementation:
- `static-demo`: use semantic inputs for simple fields, custom wrappers only when visual fidelity requires it.
- `figma-like`: keep labels and controls editable and aligned.
- `vue-dorami`: use Dorami Form/FormItem and field components.

Rules:
- Business skill decides label alignment, control height, and filter/form layout.
- Product theme controls focus ring, border, and error colors.

## Tooltip and Popconfirm

Protocol:
- Tooltip: small explanatory popup for non-essential hover information.
- Popconfirm: lightweight confirmation for simple row actions.
- Modal is required when the operation needs business context, a reason field, or stronger confirmation.

Implementation:
- `static-demo`: simple hover/focus popup is enough unless the flow requires click confirmation.
- `figma-like`: show popup state only when reviewing interaction states.
- `vue-dorami`: use Dorami Tooltip or Popconfirm.

Rules:
- Do not hide essential business data inside Tooltip.
- Business skill decides whether Popconfirm is too weak and should become Modal.
