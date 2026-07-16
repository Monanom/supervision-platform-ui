# 表格、状态与操作参数

最终参数优先于 Sketch 原始观测值；颜色必须使用已有 Theme/DCP token。

## DataTable

- 置信度：`human-confirmed`
- 分类：`table-status-actions`
- Sketch Symbol：`43E1BF89-CF92-4F1F-BF6B-AF94A9C26976`, `EA7454BF-4B8B-405C-9406-5F62D3B513A0`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"headerHeight":48,"headerTopRadius":4,"operationColumnWidth":224,"singleLineRowMinHeight":56,"width":"100%"}` |
| `spacing` | `{"cellHorizontalPadding":16,"cellPaddingBottom":14,"cellPaddingTop":14,"rowActionGap":8}` |
| `appearance` | `{"headerBackgroundToken":"--theme-table-header","headerBottomDivider":"none","headerTopDivider":"none","outerBorder":"none","rowDividerToken":"--theme-divider"}` |
| `typography` | `{"bodyFontSize":14,"cellVerticalAlign":"top","headerFontSize":14,"statusWhiteSpace":"nowrap"}` |
| `states` | `{"empty":"quiet local Empty","error":"retryable table-local error","filteredEmpty":"preserve filters and show filtered empty","loading":"table-local loading","selection":"selected rows enable valid batch actions"}` |
| `layout` | `{"multiline":"expand downward while preserving 14px vertical padding","operationColumn":"fixed width right column","otherColumns":"stretch proportionally from parent card width","status":"StatusIndicator only","tableLayout":"fixed","time":"independent column"}` |
| `responsive` | `{"fixedProperties":["operation column width","row minimum height"],"fluidProperties":["all non-operation column widths"],"measurement":"observe parent work-card width","overflow":"remain inside work card; use internal overflow only as guard"}` |

覆盖说明：Latest confirmed table contract replaces legacy 44px metrics and intrinsic-width behavior.

## StatusIndicator

- 置信度：`human-confirmed`
- 分类：`table-status-actions`
- Sketch Symbol：`0B188981-C715-4EE3-89DC-94AAC34DEE48`, `1A4B3BF3-8B80-425E-942E-F81EC4579035`, `2A3DEC8F-B27B-410D-8CBA-46FC7A6F903E`, `2E1CA6FD-86C1-438C-B04A-3FA702DCE306`, `447BC7C2-1159-480F-B16D-1C0D1B13A9E3`, `5A6BA72D-24E4-4B4C-B77E-CBC1D5A0E708`, `855B63E3-28F8-4FB6-8CCC-CEA1BB48B2BE`, `B4D3B402-B5FA-4DAB-B90E-508E85796CDA`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"dotSize":8,"height":20}` |
| `spacing` | `{"dotTextGap":8}` |
| `appearance` | `{"background":"none","border":"none","dotColor":"semantic status token"}` |
| `typography` | `{"fontSize":14,"textColorToken":"--theme-text-secondary","whiteSpace":"nowrap"}` |
| `states` | `{"default":"display only","disabled":"not applicable","hover":"none"}` |
| `layout` | `{"alignment":"left","composition":"dot plus text","forbidden":["Tag fill","rounded container","close icon","click state"]}` |
| `responsive` | `{"wrap":"forbidden for short lifecycle states"}` |

覆盖说明：Table lifecycle status is a dedicated status component, not Tag.

## Pagination

- 置信度：`manual-calibrated`
- 分类：`table-status-actions`
- Sketch 画板：`2C802BEA-6E11-4AF4-BCB5-8C79112A8B98`, `4117FD63-C212-482C-AE9D-495AE0AA1EE0`, `6FDD8B32-79D3-466A-A243-04B2C469CB1D`, `8371E3AC-3AFD-4F5C-9239-5C2C2EF6BC9B`, `CD00DB3B-CFB7-42E2-8B1A-D12BE584037D`, `E89831AA-68B8-46A4-9781-5D3D41BF0DF1`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"controlHeight":32,"radius":4}` |
| `spacing` | `{"itemGap":8,"topMargin":16}` |
| `appearance` | `{"activeToken":"--dcp-pagination-active-*","borderToken":"--dcp-pagination-border"}` |
| `typography` | `{"fontSize":14}` |
| `states` | `{"active":"single current page","disabled":"previous/next disabled at boundary","hover":"tokenized hover","loading":"lock page changes while data loads"}` |
| `layout` | `{"alignment":"right","content":["total","previous","page numbers","next"]}` |
| `responsive` | `{"wrap":"keep as one group; simplify page numbers when space is constrained"}` |

覆盖说明：Aligned with Dorami pagination and current golden demo.
