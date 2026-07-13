# Dorami Component Protocol Map

Use these mappings when generating or reviewing base UI controls. Treat each item as a component protocol that can be rendered as static HTML/CSS/JS, Figma-like editable UI, or real Vue/Dorami code.

## Stack Mapping

- `static-demo`: build semantic HTML, `dcp-*` protocol classes, ARIA where useful, and minimal JS for open/close/select/page/tab behavior. Do not import Vue.
- `figma-like`: create editable component-like groups that preserve structure, sizes, states, and visual hierarchy.
- `vue-dorami`: use real `@zcy/dorami` components and map product tokens through theme variables or wrapper classes.

Use these static-demo class hooks for protocol controls:
- Button: `dcp-button`
- Tag: `dcp-tag`
- Status indicator: `dcp-status-indicator`, `dcp-status-dot`, `dcp-status-text`
- Input: `dcp-input`
- Textarea: `dcp-textarea`
- Form: `dcp-form`, `dcp-form-item`, `dcp-form-label`, `dcp-form-control`, `dcp-form-help`
- Checkbox: `dcp-checkbox`
- Radio: `dcp-radio`
- Date/Time: `dcp-date-picker`, `dcp-time-picker`, `dcp-picker-panel`
- Upload: `dcp-upload`, `dcp-upload-list`
- Select/Dropdown: `dcp-select`, `dcp-select-menu`, `dcp-option`
- Tabs/Switcher: `dcp-tabs`, `dcp-tab`, `dcp-tab-indicator`
- Menu/Navigation: `dcp-menu`, `dcp-menu-item`, `dcp-submenu`
- Table: `dcp-table`
- Pagination: `dcp-pagination`, `dcp-page-button`
- Modal: `dcp-modal-mask`, `dcp-modal`, `dcp-modal-head`, `dcp-modal-body`, `dcp-modal-foot`, `dcp-modal-close`
- Drawer: `dcp-drawer-mask`, `dcp-drawer`, `dcp-drawer-head`, `dcp-drawer-body`, `dcp-drawer-foot`, `dcp-drawer-close`
- Tooltip/Popconfirm: `dcp-tooltip`, `dcp-popconfirm`
- Empty: `dcp-empty`
- Description list: `dcp-description-list`
- Timeline: `dcp-timeline`

## Shared Interaction Contract

Every interactive component must define:
- Normal, hover, focus, active/pressed, disabled, loading when applicable, selected/checked when applicable, error when applicable, and empty/no-data when applicable.
- Focus must be visible and tokenized. Do not rely on browser-default black outlines in visual demos.
- Disabled components are not interactive and use `aria-disabled`, `disabled`, or equivalent semantics where possible.
- Popup components manage open/closed state, outside click, Escape close, z-index above the invoking surface, and focus return to the trigger.
- Keyboard support follows expected desktop behavior: Tab moves focus, Enter/Space activates buttons/options, Arrow keys navigate menus/options/tabs, Escape closes popups/overlays.
- Loading actions lock repeated submission. If the action is not responsible for async work, use global feedback rather than adding local loading states.
- Use ARIA roles only when they match the rendered behavior. Do not add role names without keyboard behavior.

## Tag

Protocol:
- Tag is a compact, non-interactive status or category label.
- Tag is not the default component for table lifecycle statuses. Use Status Indicator for table status columns unless the business skill explicitly requires a tag.
- Standard status/rectangle tag height is 20px, border radius is 4px, and text is 12px centered vertically.
- Standard table tag height is 20px. Detail/card tags may use 24px when the active product theme allows it.
- Standard tag horizontal padding is 6px. Compact source-spec rectangle tags may use 4px. Capsule tag horizontal text padding is 8px.
- Filled color tags use solid color backgrounds with white text.
- Light color tags use pale backgrounds with colored text.
- Outline tags use white/transparent backgrounds with colored border and colored text.
- Neutral tags use gray backgrounds with gray text.
- Interactive tags are explicit variants. Display-only tags have no hover visual change and no click behavior.

Implementation:
- `static-demo`: use `<span class="dcp-tag">` with modifiers such as `filled`, `light`, `outline`, `warning`, `success`, `danger`, `info`, `neutral`, `closable`, `disabled`, or `collapsed`.
- `figma-like`: create editable variants for filled, light, and neutral states.
- `vue-dorami`: use the Dorami Tag component and map product colors through theme variables.

Rules:
- Semantic consistency: the same business meaning must use the same tag copy, style, and color across the whole product.
- Tag visual strength must match information importance and must not compete with primary actions or table operation buttons.
- Visual strength order is: light fill < outline < dark/solid fill.
- Prefer light fill for common/high-frequency status and category tags. Use outline for secondary or weak-emphasis metadata. Use solid fill only for key status, high-priority alerts, core result labels, severe failure, or other rare high-salience cases.
- Choose tag visual weight by information importance:
  - Level 1 / high salience: filled color tag, solid background with white text. Use for risk levels, warning levels, severity, failure states, or labels that must be seen before surrounding text.
  - Level 2 / medium salience: light color tag, pale background with colored text. Use for secondary classifications, business categories, record types, or table scanning aids.
  - Level 3 / low salience: neutral tag, gray background/text or plain muted text when a tag shape is unnecessary. Use for ordinary metadata, inactive values, and low-priority labels.
- Do not use multiple Level 1 filled tags in the same dense row unless the source screen or business priority requires competing high-salience labels. Within one region, solid-fill tags should stay below 20% of the visible tag count.
- Do not use tags as action buttons. If clickable behavior is needed, use Button or Link protocol.
- Do not let tag padding or line-height change surrounding table or description-list row height.
- Status-like tags are allowed for high-salience results, warning levels, risk levels, or page/detail summary labels. They are not used for ordinary table status columns.
- Category tags mark attributes, classification, priority, markers, or audience labels. Tags from the same dimension may show at most three inline; overflow becomes a collapsed `+N` tag.
- Tag copy should normally stay within 8 Chinese characters. If the source text is longer, prefer a shorter business label rather than widening the tag into a sentence.
- Rectangle tags support three schemes: dark fill with white text, light fill with colored text, and colored border with colored text.
- Filled tags require readable contrast. When using a color scale, choose a stronger color step for filled backgrounds and keep text white.
- Light tags use pale backgrounds and colored text. Border tags use white background plus colored border/text.
- Display-only tags do not show pointer cursor, hover fill, focus ring, or click feedback.
- Closable tags place the close icon on the right. Hover may reveal or emphasize the close affordance; clicking the close affordance removes the tag directly unless the business skill requires confirmation.
- Long tags truncate with ellipsis at the component's max width. Hover/focus may show the full copy in Tooltip.
- Disabled tags use about 40% opacity, cannot be clicked or closed, and may show a Tooltip reason on hover/focus.
- Table row status tags align left inside the status column and must not mix with row operation buttons.
- When a `+N` collapsed tag is shown, hover/focus reveals all hidden tags in a lightweight Tooltip/Popover using the same tag styles.
- Ribbon tags are one-character labels only. Do not use them for normal status or table metadata.
- Bubble tags only use dark background with white text. Do not create light or outlined bubble variants.
- Icon-text tags follow the same three color schemes and customization rules as rectangle tags.

## Status Indicator

Protocol:
- Status Indicator is a lightweight read-only status display made of a small colored dot plus text.
- It is the default component for table status columns and process/lifecycle states such as notified, replied, verified, withdrawn, pending, read, unread, and processing.
- It is not a Tag: no filled background, no border, no rounded container, no close icon, no `+N` folding, and no tag hover behavior.

Implementation:
- `static-demo`: use `<span class="dcp-status-indicator"><i class="dcp-status-dot"></i><span class="dcp-status-text">已通知</span></span>`.
- `figma-like`: render dot and text as separate editable elements.
- `vue-dorami`: implement as a lightweight status-display wrapper or the product's Status component if one exists; do not substitute Tag unless explicitly required.

Rules:
- Dot size is compact, normally 6px to 8px. Text uses the surrounding table/body text style, normally 14px.
- The dot and text align horizontally on the text baseline or optical center.
- Status indicator is left-aligned in table status columns and must not mix with operation buttons.
- It is display-only by default: no click, no hover background, no pointer cursor.
- If extra explanation is required, use Tooltip on the text or row, not a tag container.
- Use functional color semantics: blue for in-progress/notified/read, green for completed/verified/success, orange for abnormal/replied/warning when the business uses it, gray for withdrawn/invalid/disabled.
- Do not use Status Indicator for classification labels, risk levels, or multi-value attributes; use Tag for those.

## Button

Protocol:
- Primary button: filled theme color, white text, hover/active/disabled/loading states.
- Secondary button: light or white fill, border, dark text, hover border/background state.
- Danger text/outline button: danger-colored text for withdraw, delete, revoke, reject, or remove actions; avoid full red fill unless confirming destructive action.
- Icon-only button: use the product icon source or Dorami icon mechanism; include hover/focus/disabled states.
- Button hierarchy supports these authoring levels: primary, secondary, tertiary, primary text, secondary text, and link-style text. Each operation area should normally use only two or three hierarchy levels.
- Button attributes can combine with the hierarchy: icon, danger, dashed, inverse, and ghost.
- Button interaction states must include normal, hover, active, loading, and disabled.
- Standard heights are 28px, 32px, and 40px. Extended preset heights are 36px, 44px, and 48px.
- Button width adapts to text while keeping horizontal padding stable. If the text is very short, the button uses the preset minimum width instead of shrinking to the padding rule.
- Custom minimum width must stay in this range: button height x 1.5, rounded up to an even number, through button height x 3.
- Text-only preset minimum width uses this ladder when no product override exists: H28 -> 56px, H32 -> 64px, H36 -> 72px, H40 -> 80px, H44 -> 88px, H48 -> 96px.
- Icon-text preset minimum width uses this ladder when no product override exists: H28 -> 76px, H32 -> 84px, H36 -> 92px, H40 -> 96px, H44 -> 104px, H48 -> 108px.
- Horizontal text padding uses this ladder when no product override exists: H28/H32 -> 12px left and right, H36/H40 -> 16px left and right, H44/H48 -> 20px left and right.
- Horizontal text padding and icon gap must use 4px rhythm. Icon-text spacing defaults to 4px unless the product theme overrides it.
- Font size uses this ladder when no product override exists: H28 -> 12px, H32 -> 14px, H36 -> 14px, H40 -> 16px, H44 -> 16px, H48 -> 16px.

Implementation:
- `static-demo`: use `<button class="dcp-button">` with protocol modifiers such as `primary`, `secondary`, `danger`, `small`, `medium`, `large`, `loading`, and `disabled`.
- `figma-like`: create variants for default, hover, active, disabled, loading if the output supports variants.
- `vue-dorami`: use Dorami Button props such as primary/default/danger/loading/disabled.

Rules:
- Row action priority is decided by the business skill.
- Each operation area should have at most one primary button.
- A single button can be used alone. Do not add a fake secondary action only for visual balance.
- Global page actions such as save/cancel usually use a primary action plus a secondary or tertiary action.
- Module actions such as filter query/reset usually use a primary or secondary action plus a quieter reset action.
- Local dense actions such as cards and inline links may use text/link-style buttons. Table operation columns follow the active business skill; do not default them to text buttons when the product requires filled or outline row actions.
- Danger buttons are for deletion, moving, permission change, and other risky operations; clicking them usually requires second confirmation.
- Dashed buttons are normally for adding items in a list and may span the list/content width.
- Inverse buttons are for primary-color backgrounds. Ghost buttons are for complex colored, image, textured, or dark backgrounds where the button surface should stay transparent.
- Use the small/medium/large size set from the active product theme. Common Dorami heights are 28px, 32px, and 40px; product themes may map the set to 28px, 36px, 44px or other approved sizes.
- Small buttons are for compact spaces such as pop confirmations, warning prompts, and dense row operations. Large buttons are for special scenarios such as login/register or full-width form actions.
- Standard type sizes follow the exact height mapping in the protocol: 28px uses 12px, 32px and 36px use 14px, and 40px/44px/48px use 16px unless the product theme overrides it.
- In static demos, prefer standard protocol modifiers such as `dcp-button secondary small` for compact outline buttons. Do not introduce ad hoc classes such as `row-action` when a standard modifier combination can express the same component state.
- In button groups, place secondary actions before the primary action so the primary action appears on the right. Default group gap is 8px unless the product theme overrides it.
- Avoid more than four visible buttons in a generic non-table operation area. When actions are many, move lower-priority actions into a dropdown or "more" menu. Table/list row actions may be stricter when the active business skill defines a smaller limit.
- Keep button radius consistent within a product. Product themes may override radius, but arbitrary one-off radius is not allowed.
- The default button radius is 4px. If a product customizes radius, choose one consistent radius for the product and keep it on a 4px rhythm where possible.
- Bordered buttons use a 1px border by default. A product may use 1.5px or 2px only as a deliberate theme decision.
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
- Feedback/result dialog explanatory copy should use about a 320px readable measure before wrapping unless the product theme or content layout requires otherwise.
- Dialogs may support an optional checkbox such as "do not remind again" when the workflow requires it.
- Confirmation dialogs may support one optional checkbox, such as "do not remind again". Keep the checkbox in the body/content flow rather than mixing it into the footer button group.
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
- Use one of the standard modal widths first: 580px, 780px, or 980px.
- Keep modal content padding at 20px on all sides by default.
- Modal footer buttons follow Button protocol. Secondary/cancel stays left of confirm/primary, and the group gap is 8px by default.
- Modal close must be an icon-only affordance, not a text button.
- Modal body may scroll when content exceeds the allowed height; the header and footer should remain stable.

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
- Drawer background has two base modes:
  - White background: separate content with lines.
  - Gray background: place content sections on white surfaces.
- Content should keep 20px spacing from left/right edges and from the title divider by default.
- Footer action gap follows Button protocol, usually 8px.
- Optional checkbox controls may appear near drawer actions only when the workflow requires user acknowledgement.

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
- Trigger supports hover, focus, open, disabled, and error states.
- Popup opens from click or keyboard, closes on outside click or Escape, and returns focus to the trigger.
- Arrow Up/Down moves active option; Enter selects; disabled options cannot be selected.
- Selected option must be visible in both trigger value and menu selected state.
- Popup uses an elevated layer above cards, modals, drawers, and sticky headers according to context.
- Long option text truncates or wraps according to product density, but the selected value should stay readable.

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
- Previous/next buttons disable at the first/last page.
- Page changes update table/list content, current page state, and total display together.
- Hover and focus states apply to enabled page items only.
- Enter/Space activates focused page items.
- If page size controls are present, changing page size resets or validates current page according to the data set.

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
- Header, body, empty state, loading state, selection state, and pagination must be visually coherent.
- Row hover may highlight the row subtly, but must not obscure tags, links, or action buttons.
- Sortable headers show hover/focus and sorted direction state. Do not show sort affordances on non-sortable columns.
- Row selection uses Checkbox protocol; indeterminate header checkbox appears when only some rows are selected.
- Loading state should preserve table width and column rhythm; avoid layout jump.
- Empty state appears inside the table area and may include one relevant action.
- Sticky or fixed columns must not break proportional resizing unless the active business skill explicitly requires fixed action columns.

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
- Required fields must show a required mark and a validation message when invalid.
- Error state includes error border/focus and help text; do not communicate error only by color.
- Placeholder text is muted and disappears when value exists.
- Clearable controls show clear affordance only when the field has value and is enabled.
- Textarea supports disabled, error, character count when required, and vertical resize only if the product allows it.
- Form submit validates visible required fields before executing. Failed submit focuses or scrolls to the first invalid field when practical.
- Filter forms may validate lightly; business forms must show field-level validation.

## Checkbox and Radio

Protocol:
- Checkbox supports unchecked, checked, indeterminate, hover, focus, disabled, and error states.
- Radio supports unchecked, checked, hover, focus, disabled, and error states.
- Checkbox is for multi-select or acknowledgement. Radio is for exactly one option in a group.

Implementation:
- `static-demo`: use semantic `<input type="checkbox">` / `<input type="radio">` where possible, wrapped with `dcp-checkbox` or `dcp-radio` for visual fidelity.
- `figma-like`: show selected, disabled, and indeterminate variants when relevant.
- `vue-dorami`: use Dorami Checkbox/Radio components.

Rules:
- Space toggles focused checkbox/radio. Arrow keys move within radio groups.
- Label click toggles the control when the label is part of the same form item.
- Indeterminate is only for parent checkbox selection state and does not mean checked.
- Disabled controls cannot change value and should not show hover feedback.
- Do not let broad input sizing rules enlarge checkbox/radio beyond component scale.

## Date and Time Picker

Protocol:
- Trigger behaves like an input/select hybrid with value, placeholder, clear, disabled, error, and focus states.
- Picker panel is an elevated popup with hover, selected, today/current, range, disabled date/time, and footer actions when needed.

Implementation:
- `static-demo`: reproduce trigger and panel only when the opened state is needed for review; otherwise use protocol-compatible input.
- `figma-like`: show trigger plus opened panel state for interaction review.
- `vue-dorami`: use Dorami DatePicker/TimePicker/RangePicker.

Rules:
- Click or keyboard opens the panel; Escape closes; Enter confirms highlighted value when practical.
- Disabled dates/times cannot be selected.
- Range picker keeps start/end order clear and highlights the in-range segment.
- Clear action resets value without submitting the form.
- Date/time format should match business data and table columns.

## Upload

Protocol:
- Upload includes trigger button/drop zone, file list, uploading progress, success, failure, remove, retry when needed, and disabled states.

Implementation:
- `static-demo`: use protocol-compatible upload button and file list; mock progress only when the flow requires it.
- `figma-like`: show empty, uploading, uploaded, and failed states when reviewing upload flows.
- `vue-dorami`: use Dorami Upload.

Rules:
- Show accepted file type/size hints when constraints matter.
- Uploading files show progress or loading state and block duplicate submit when required.
- Failed files show reason and allow retry/remove when supported.
- Remove is a risk action only when it deletes already-submitted evidence; otherwise it removes the local queued file.
- File names should be readable and support download/open actions only when business flow allows.

## Tabs and Switcher

Protocol:
- Tabs/switchers support inactive, hover, active, disabled, focus, and animated indicator states.
- Switching tabs updates selected state and the associated content region together.

Implementation:
- `static-demo`: use `dcp-tabs`, `dcp-tab`, and `dcp-tab-indicator` with minimal JS.
- `figma-like`: show active and hover variants.
- `vue-dorami`: use Dorami Tabs or segmented control equivalents.

Rules:
- Click, Enter, or Space selects a tab. Arrow keys move focus among tabs.
- Active tab must be visually clear without relying only on color.
- Tabs that change business data must reset or preserve filters intentionally according to the business skill.
- Do not use tabs as decorative pills when content does not switch.

## Menu and Navigation

Protocol:
- Menu items support normal, hover, selected, expanded/collapsed, disabled, and focus states.
- Submenus show disclosure state and preserve selected child context.

Implementation:
- `static-demo`: use semantic nav/list markup with `dcp-menu`, `dcp-menu-item`, and `dcp-submenu` hooks.
- `figma-like`: create active, hover, and expanded states.
- `vue-dorami`: use Dorami Menu/Nav components when available.

Rules:
- Click selects navigation item or toggles submenu depending on item type.
- Keyboard supports Tab to enter menu and Arrow keys within menu when implemented as a true menu.
- Selected page remains visible after route/content switch.
- Disabled menu items cannot be selected and should explain permissions only if needed.

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
- Tooltip opens on hover/focus and closes on mouse leave, blur, or Escape.
- Tooltip content is short and read-only. It must not contain primary workflows.
- Popconfirm opens on click, traps intent around confirm/cancel, and returns focus to the trigger after close.
- Popconfirm confirm/cancel buttons follow Button protocol and danger semantics when confirming a risk action.
- Do not use Popconfirm for forms, reason entry, attachment flows, or irreversible high-risk workflows that require context.

## Empty

Protocol:
- Empty state includes optional icon/illustration, short title, optional description, and optional action.

Implementation:
- `static-demo`: use `dcp-empty` inside the owning component area.
- `figma-like`: keep icon/text/action editable.
- `vue-dorami`: use Dorami Empty or product empty-state component.

Rules:
- Empty state appears in place, not as a full-page hero unless the entire page is empty.
- Use one primary action only when the user can directly resolve the empty state.
- Do not show irrelevant batch actions when table data is empty.
- Loading and empty states are distinct; do not show empty while data is still loading.

## Description List and Timeline

Protocol:
- Description list displays label/value rows or columns with optional links/actions.
- Timeline displays chronological events with dot/line, actor, time, action, remark, and attachments when present.

Implementation:
- `static-demo`: use `dcp-description-list` and `dcp-timeline` structure hooks.
- `figma-like`: keep labels, values, and timeline rows editable.
- `vue-dorami`: use Dorami description/timeline components or equivalent layout.

Rules:
- Description values align consistently and allow text wrapping without changing unrelated rows.
- Inline actions inside description values use text/link protocol and must not increase row height.
- Timeline rows are ordered newest-first or oldest-first according to business skill, and the order must be visually obvious.
- Timeline attachments use Upload/File-list interaction rules for download/remove where applicable.
- Long remarks wrap within the content column and must not collide with the time column.
