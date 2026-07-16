# 数据展示参数

最终参数优先于 Sketch 原始观测值；颜色必须使用已有 Theme/DCP token。

## MetricCard

- 置信度：`human-confirmed`
- 分类：`data-display`
- Sketch Symbol：`0C5A0185-FAA4-40D8-B5E4-032059A09963`, `4CB21149-239F-4E99-ABD6-25432F022DA1`, `773527DC-310B-4F15-A8AD-F38A9BCA6E53`, `DCE00270-68A2-48E5-84AB-5972A79A9C7F`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"radius":4,"referenceHeight":106,"referenceWidth":224}` |
| `spacing` | `{"contentGap":8,"padding":16}` |
| `appearance` | `{"backdropBlur":6,"fillToken":"--theme-frosted-white-60-100","shadow":"none","strokeToken":"--theme-white"}` |
| `typography` | `{"labelFontSize":14,"numberFirst":true,"numberFontToken":"--font-number"}` |
| `states` | `{"default":"display only","hover":"none unless the product explicitly adds interaction"}` |
| `layout` | `{"order":["number","status dot and label"],"title":"no separate section title"}` |
| `responsive` | `{"height":"fixed","width":"stretch evenly with sibling cards"}` |

覆盖说明：Metric cards are non-clickable frosted display cards by default.

## DescriptionList

- 置信度：`sketch-and-manual-confirmed`
- 分类：`data-display`
- Sketch Symbol：`26F71EBE-5200-4216-B941-E6611D68EBCF`, `2C7D03C7-4D41-4D33-B50B-8FE13FA7B015`, `31A20B35-269D-4695-9BA1-450E00AEB1CF`, `3E251B9B-6BAC-4A9F-9999-E9E40D8B1E64`, `5DE8C8F1-D81D-4F10-88FB-F441506C03A5`, `93F5B6A9-8B54-4986-A18D-7043B74B5C75`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"contentReferenceWidth":216,"labelReferenceWidth":112,"multiLineMinHeight":68,"singleLineHeight":48}` |
| `spacing` | `{"cellHorizontalPadding":16,"cellVerticalPadding":12}` |
| `appearance` | `{"backgroundToken":"--theme-surface","borderToken":"--theme-divider","radius":4}` |
| `typography` | `{"labelColorToken":"--theme-text-secondary","labelFontSize":14,"valueColorToken":"--theme-text-primary","valueFontSize":14}` |
| `states` | `{"emptyValue":"use a consistent dash","link":"preserve row height","truncated":"show full value in Tooltip"}` |
| `layout` | `{"label":"fixed reference width","multiline":"expand downward","value":"fluid and top aligned"}` |
| `responsive` | `{"labelWidth":"fixed unless page pattern explicitly changes columns","valueWidth":"fluid"}` |

覆盖说明：Uses Sketch description-list dimensions plus confirmed inline-link behavior.
