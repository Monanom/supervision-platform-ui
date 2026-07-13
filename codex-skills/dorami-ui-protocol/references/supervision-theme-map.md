# Supervision Theme Map for Dorami Protocol

Use this reference when `dorami-ui-protocol` and `supervision-page-builder` are both active.

## Theme Strategy

Do not edit Dorami component source for supervision-only needs. In `static-demo`, reproduce these mappings as CSS variables and classes. In `vue-dorami`, apply the supervision look through:

1. Runtime CSS variable overrides.
2. A supervision wrapper class, for example `.supervision-theme`.
3. Product-specific assets such as the close icon from `supervision-page-builder/assets/icons/关闭.svg`.

The supervision theme uses the lightweight Raw / Theme / Component token system. It adapts atoms only: color, text color, border color, radius, shadow, mask color, focus ring, icon asset, and control height tokens. It must not redefine the basic Modal, Drawer, Button, Select, Table, or Pagination shell. Business skills fill component slots with business content.

## Token Mapping

Map supervision tokens to Dorami CSS variables in this order:

1. Raw tokens: original palette, size, radius, shadow, and asset values.
2. Theme tokens: page-level semantic values consumed by supervision layouts.
3. Component tokens: `--dcp-*` values consumed by Dorami protocol controls.

```css
.supervision-theme {
  /* Raw tokens */
  --brand-main: var(--brand-8);
  --brand-1: #F7F7FF;
  --brand-2: #EEF0FF;
  --brand-3: #E3E7FF;
  --brand-4: #CED4FF;
  --brand-5: #B0B8FF;
  --brand-6: #8691FF;
  --brand-7: #5D6AFF;
  --brand-8: #4353FF;
  --brand-9: #2C0DF1;
  --brand-10: #1B00C7;

  --neutral-1: #F7F8FA;
  --neutral-2: #F2F4F7;
  --neutral-3: #ECEEF2;
  --neutral-4: #E3E6EB;
  --neutral-5: #D8DCE2;
  --neutral-6: #C2C7D1;
  --neutral-7: #A7AEBB;
  --neutral-8: #838B99;
  --neutral-9: #505663;
  --neutral-10: #20242C;

  --nav-gradient-start: #181C4F;
  --nav-gradient-end: #394183;
  --state-success: #00B552;
  --state-warning: #F0770B;
  --state-danger: #DF1F1F;
  --radius-sm: 4px;
  --radius-lg: 8px;
  --height-control-sm: 28px;
  --height-control-md: 32px;
  --height-control-lg: 40px;
  --height-table-header: 48px;
  --height-table-row: 56px;
  --shadow-overlay: 0 16px 48px rgba(24, 28, 79, 0.18);
  --font-alphanumeric: "D-DIN-PRO-Alphanumeric";
  --font-number: var(--font-alphanumeric);
  --asset-bg-image: url("assets/bg.jpg");
  --asset-overlay-close: url("assets/icons/关闭.svg");

  /* Theme tokens */
  --theme-primary: var(--brand-8);
  --theme-primary-hover: var(--brand-7);
  --theme-primary-active: var(--brand-9);
  --theme-primary-deep: var(--brand-10);
  --theme-bg: var(--brand-1);
  --theme-bg-soft: var(--brand-1);
  --theme-bg-tint: var(--brand-2);
  --theme-bg-image: var(--asset-bg-image);
  --theme-surface: #FFFFFF;
  --theme-surface-metric-from: rgba(255, 255, 255, 0.60);
  --theme-surface-metric-to: #FFFFFF;
  --theme-border: var(--neutral-4);
  --theme-border-soft: var(--neutral-3);
  --theme-table-head: var(--neutral-1);
  --theme-text: var(--neutral-10);
  --theme-text-secondary: var(--neutral-9);
  --theme-text-muted: var(--neutral-8);
  --theme-text-disabled: var(--neutral-6);
  --theme-nav-start: var(--nav-gradient-start);
  --theme-nav-end: var(--nav-gradient-end);
  --theme-focus-ring: rgba(67, 83, 255, 0.10);
  --theme-overlay: rgba(32, 36, 44, 0.45);
  --theme-success: var(--state-success);
  --theme-warning: var(--state-warning);
  --theme-danger: var(--state-danger);
  --theme-danger-hover: #C91616;
  --theme-danger-light: rgba(223, 31, 31, 0.08);
  --theme-disabled-opacity: 0.40;
  --theme-popup-shadow: 0 8px 24px rgba(24, 28, 79, 0.12);

  /* Component tokens */
  --dcp-radius-sm: var(--radius-sm);
  --dcp-radius-lg: var(--radius-lg);
  --dcp-control-height-sm: var(--height-control-sm);
  --dcp-control-height-md: var(--height-control-md);
  --dcp-control-height-lg: var(--height-control-lg);
  --dcp-button-primary-bg: var(--theme-primary);
  --dcp-button-primary-bg-hover: var(--theme-primary-hover);
  --dcp-button-primary-bg-active: var(--theme-primary-active);
  --dcp-button-primary-text: #FFFFFF;
  --dcp-button-default-bg: var(--theme-surface);
  --dcp-button-default-border: var(--theme-border);
  --dcp-button-default-text: var(--theme-text);
  --dcp-button-default-bg-hover: var(--neutral-1);
  --dcp-button-default-border-hover: var(--theme-primary);
  --dcp-button-danger-text: var(--theme-danger);
  --dcp-button-danger-border: var(--theme-danger);
  --dcp-button-danger-bg-hover: var(--theme-danger-light);
  --dcp-button-danger-border-hover: var(--theme-danger-hover);
  --dcp-control-disabled-opacity: var(--theme-disabled-opacity);
  --dcp-tag-height-sm: 20px;
  --dcp-tag-height-md: 24px;
  --dcp-tag-radius: var(--radius-sm);
  --dcp-tag-padding-x: 6px;
  --dcp-tag-font-size: 12px;
  --dcp-tag-light-bg: var(--brand-2);
  --dcp-tag-outline-bg: transparent;
  --dcp-tag-solid-text: #FFFFFF;
  --dcp-tag-disabled-opacity: var(--theme-disabled-opacity);
  --dcp-tag-close-hover-bg: rgba(32, 36, 44, 0.08);
  --dcp-tag-collapse-bg: var(--neutral-2);
  --dcp-tag-collapse-text: var(--theme-text-secondary);
  --dcp-status-dot-size: 6px;
  --dcp-status-text: var(--theme-text-secondary);
  --dcp-status-info: var(--theme-primary);
  --dcp-status-success: var(--theme-success);
  --dcp-status-warning: var(--theme-warning);
  --dcp-status-danger: var(--theme-danger);
  --dcp-status-neutral: var(--neutral-8);
  --dcp-table-header-bg: var(--theme-table-head);
  --dcp-table-header-height: var(--height-table-header);
  --dcp-table-row-height: var(--height-table-row);
  --dcp-table-border-color: var(--theme-border-soft);
  --dcp-table-row-hover-bg: rgba(67, 83, 255, 0.04);
  --dcp-table-row-selected-bg: var(--brand-2);
  --dcp-table-empty-text: var(--theme-text-muted);
  --dcp-select-bg: var(--theme-surface);
  --dcp-select-border: var(--theme-border);
  --dcp-select-border-hover: var(--theme-primary);
  --dcp-select-focus-ring: var(--theme-focus-ring);
  --dcp-dropdown-bg: var(--theme-surface);
  --dcp-dropdown-radius: var(--dcp-radius-lg);
  --dcp-dropdown-shadow: var(--theme-popup-shadow);
  --dcp-dropdown-option-gap: 4px;
  --dcp-dropdown-option-hover-bg: var(--neutral-1);
  --dcp-dropdown-option-selected-bg: var(--brand-2);
  --dcp-pagination-active-bg: var(--theme-primary);
  --dcp-pagination-active-text: #FFFFFF;
  --dcp-checkbox-size: 16px;
  --dcp-checkbox-border: var(--theme-border);
  --dcp-checkbox-checked-bg: var(--theme-primary);
  --dcp-radio-size: 16px;
  --dcp-picker-panel-bg: var(--theme-surface);
  --dcp-picker-panel-shadow: var(--theme-popup-shadow);
  --dcp-upload-border: var(--theme-border);
  --dcp-upload-hover-border: var(--theme-primary);
  --dcp-tooltip-bg: rgba(32, 36, 44, 0.92);
  --dcp-tooltip-text: #FFFFFF;
  --dcp-popconfirm-bg: var(--theme-surface);
  --dcp-popconfirm-shadow: var(--theme-popup-shadow);
  --dcp-tabs-active-bg: var(--theme-primary);
  --dcp-tabs-active-text: #FFFFFF;
  --dcp-tabs-hover-bg: rgba(67, 83, 255, 0.08);
  --dcp-menu-hover-bg: color-mix(in srgb, var(--theme-surface) 8%, transparent);
  --dcp-menu-selected-bg: color-mix(in srgb, var(--theme-surface) 12%, transparent);
  --dcp-modal-bg: var(--theme-surface);
  --dcp-modal-mask-bg: var(--theme-overlay);
  --dcp-modal-shadow: var(--shadow-overlay);
  --dcp-modal-close-size: 32px;
  --dcp-modal-close-offset: 12px;
  --dcp-modal-close-icon: var(--asset-overlay-close);
  --dcp-modal-footer-button-height: 32px;
  --dcp-drawer-bg: var(--theme-surface);
  --dcp-drawer-mask-bg: var(--theme-overlay);
  --dcp-drawer-shadow: var(--shadow-overlay);
  --dcp-drawer-close-icon: var(--asset-overlay-close);

  /* Compatibility mappings for real Dorami / Ant Design Vue integrations */
  --v6-color-primary: var(--theme-primary);
  --v6-color-primary-hover: var(--theme-primary-hover);
  --v6-color-primary-active: var(--theme-primary-active);
  --v6-color-primary-bg: var(--theme-bg);
  --v6-color-focus-ring: var(--theme-focus-ring);
  --v6-color-text: var(--theme-text-secondary);
  --v6-color-text-heading: var(--theme-text);
  --v6-color-text-secondary: var(--theme-text-muted);
  --v6-color-border: var(--theme-border);
  --v6-color-border-secondary: var(--theme-border-soft);
  --v6-color-fill-secondary: var(--neutral-2);
  --v6-color-fill-tertiary: var(--neutral-1);
  --v6-color-bg-container: var(--theme-surface);
  --v6-color-bg-elevated: var(--theme-surface);
  --v6-color-bg-mask: var(--theme-overlay);
}
```

Authoring rules:
- Page layout and business styles consume `--theme-*` tokens.
- Dorami protocol controls consume `--dcp-*` tokens.
- Raw tokens such as `--brand-*`, `--neutral-*`, `--radius-*`, and `--height-*` are source values. Do not use them directly in component CSS when a Theme or Component token exists.
- Keep `--v6-color-*` only for compatibility with real Dorami / Ant Design Vue integration. Static demos should use `--theme-*` and `--dcp-*` first.

## Supervision Overrides

Apply these theme-token overrides on top of Dorami:

- Modal and Drawer close controls use `supervision-page-builder/assets/icons/关闭.svg`.
- Modal header and footer should not show internal divider lines unless a source screen explicitly requires them.
- Modal footer buttons are 32px high.
- Filter controls are 32px high on supervision list pages.
- Select and Dropdown option spacing is 4px.
- Table header height is 48px; standard single-line row height is 56px.
- Table operation column stays fixed when the business skill requires it; other columns stretch proportionally.
- Row action groups show at most one filled primary button and may show none.
- Withdraw/delete/revoke-style actions use danger-colored text unless they are destructive primary confirmation actions.

Business content rules, such as what form fields appear in a supervision modal or what timeline rows appear in a drawer, belong to `supervision-page-builder`, not this theme map.

## Static Demo and Figma-Like Output

When real Dorami components are not part of the output:

- Reproduce the Dorami component protocol and state behavior visually.
- Use the same supervision token mapping.
- Still follow the supervision business rules for density, layout, table behavior, and overlay close icon.
