# Golden Demo

This folder contains the first golden reference for supervision-platform UI generation.

Primary file:

```text
golden-demo/supervision-warning-supervise-query.html
```

Use it as the visual and structural anchor before generating any new page.

## What To Reuse

- 220px fixed left sidebar with dark vertical gradient.
- 56px translucent top bar.
- Right content background: fixed top JPG plus Brand-1 bottom color.
- Platform Logo from `assets/supervision-platform-logo-2x.png`.
- D-DIN-PRO for English letters and numbers.
- 14px primary information text.
- Frosted metric cards, normal white work cards.
- Filter controls at 32px height.
- Table header, adaptive columns, 56px row baseline, 14px vertical cell padding.
- Table status as colored dot plus text.
- Table row actions as Dorami protocol buttons with at most one primary action.
- Modal close as icon-only close affordance.

## What Not To Copy Blindly

- The exact business data is sample data.
- The page name and table fields should change with the user's requirement.
- Do not force every future page to be a warning/supervision query page.

## Companion Notes

- `page-structure.md`: page regions and layout rules.
- `token-component-notes.md`: token and component rules to preserve.
