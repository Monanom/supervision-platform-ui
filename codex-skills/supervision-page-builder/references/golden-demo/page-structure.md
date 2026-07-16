# Golden Demo Page Structure

Use this structure as the default list-page skeleton.

## Shell

- `app`: full application frame.
- `side`: fixed 220px sidebar; dark gradient; selected item uses white 12% overlay plus left indicator.
- `main`: right adaptive area; has top background image from page top and Brand-1 base color.
- `top`: 56px translucent top bar with blur.
- `content`: scrollable right content area.
- `workspace`: full-width page work area.

## Page Body

- `page-head`: page title plus business switch/tabs.
- `overview`: horizontal metric cards.
- `work-card`: one white card containing title, filters, table, empty state, and pagination.

## List Work Card

- One visible card title only.
- No subtitle unless required by business.
- Filter row sits 16px below title and 16px above table.
- Table and filters stay in the same card.
- Table follows parent width; only action column may stay fixed.

## Interaction

- Selects use custom popup behavior, not native black popovers.
- Business switch moves active state and updates content.
- Search, reset, pagination, modal open/close, and row actions must be interactive in static demos when shown.
