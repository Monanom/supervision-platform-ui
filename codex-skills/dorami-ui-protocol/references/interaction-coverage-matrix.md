# Supervision Component Interaction Coverage Matrix

Use this matrix when generating or reviewing supervision platform UI. It is a coverage index, not a visual spec. Detailed behavior stays in `component-map.md`; product-specific use stays in `supervision-page-builder`.

## Covered In This Version

| Component | Base Protocol | Product/Business Owner | Coverage |
| --- | --- | --- | --- |
| Button | `dorami-ui-protocol` | supervision row/toolbar priority | structure, size, hover, active, disabled, loading, danger, icon, keyboard |
| Table | `dorami-ui-protocol` | supervision columns/actions/density | header, row, empty, hover, selection-ready, responsive, actions |
| Tag/Status | `dorami-ui-protocol` | supervision importance/status mapping | filled/light/border, dot status, size, copy length |
| Input/Textarea | `dorami-ui-protocol` | supervision filter/form layout | placeholder, hover, focus, disabled, error, clearable |
| Select/Dropdown | `dorami-ui-protocol` | supervision filter/topbar usage | trigger, popup, option hover/selected/disabled, keyboard, z-index |
| Pagination | `dorami-ui-protocol` | supervision table footer placement | active, hover, disabled, previous/next, page change |
| Modal/Dialog | `dorami-ui-protocol` | supervision business content | mask, close, footer, scroll, Escape, focus, confirm |
| Drawer | `dorami-ui-protocol` | supervision detail/workflow content | side panel, width, close, outside click, scroll, sticky footer |
| Form | `dorami-ui-protocol` | supervision label/control density | label, help, validation, required, submit |
| Checkbox/Radio | `dorami-ui-protocol` | supervision filters/forms/confirmations | checked, indeterminate, disabled, keyboard |
| Date/Time Picker | `dorami-ui-protocol` | supervision filter columns | popup, range, disabled date, clear, keyboard |
| Upload | `dorami-ui-protocol` | supervision evidence/attachment flows | select, uploading, success, failed, remove, disabled |
| Tooltip | `dorami-ui-protocol` | supervision permissions/help | hover/focus trigger, placement, non-essential info |
| Popconfirm | `dorami-ui-protocol` | supervision simple risk confirmation | trigger, confirm/cancel, when to escalate to Modal |
| Tabs/Switcher | `dorami-ui-protocol` | supervision business scope tabs | active, hover, keyboard, content sync |
| Navigation/Menu | `dorami-ui-protocol` | supervision sidebar/topbar shell | hover, selected, expanded, collapsed, keyboard |
| Description List | `supervision-page-builder` | supervision detail pages | label/value alignment, links, row height |
| Timeline/Flow Log | `supervision-page-builder` | supervision process records | chronological rows, attachments, scroll |
| Empty State | `dorami-ui-protocol` | supervision local empty states | title, description, action, no-data behavior |

## Needs Source-Spec Calibration

These rules are derived from Dorami protocol plus supervision screenshots and should be replaced or tightened when the matching source pages are supplied:

- DatePicker / TimePicker exact panel dimensions and option spacing.
- Upload list thumbnail/file-row dimensions and progress visuals.
- Tooltip and Popconfirm exact arrow, offset, and shadow.
- Tabs outside the current business scope switcher.
- Advanced table row selection, batch toolbar, and column-setting panel.
