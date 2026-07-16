# Golden Demo Token And Component Notes

## Required Assets

- Background: `assets/bg.jpg`
- Logo: `assets/supervision-platform-logo-2x.png`
- Icons: `assets/icons/`
- Font: `assets/fonts/D-DIN-PRO-*.otf`

## Token Rules

- Define tokens in Raw / Theme / Component order.
- Page surfaces consume `--theme-*`.
- Dorami protocol controls consume `--dcp-*`.
- Do not add new colors directly in component CSS if a token exists.

## Component Rules

- Buttons: Dorami protocol button; filters use 32px; row actions use compact buttons.
- Select/Dropdown: custom trigger and popup; 4px option spacing; tokenized hover/focus.
- Table: parent-width adaptive; header has top 4px radius only; body cells top-align.
- Status: table lifecycle status is dot plus text, not Tag.
- Modal: no internal divider lines; close is icon-only; footer buttons are 32px.
- Sidebar: hover is white 8%; selected is white 12% plus indicator.

## Golden Checks

If a generated page feels different from the golden demo, check these first:

1. Background starts at the top of the right main region.
2. Work cards are plain white, not frosted.
3. Metric cards use the frosted 60%-to-100% white treatment.
4. Filter controls are 32px high.
5. Table columns resize together.
6. Row actions use at most one primary button.
7. Icons come from bundled assets.
