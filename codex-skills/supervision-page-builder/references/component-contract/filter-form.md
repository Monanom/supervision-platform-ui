# 筛选区、表单与按钮参数

最终参数优先于 Sketch 原始观测值；颜色必须使用已有 Theme/DCP token。

## SearchPanel

- 置信度：`human-confirmed`
- 分类：`filter-form`
- Sketch 画板：`4117FD63-C212-482C-AE9D-495AE0AA1EE0`, `6FDD8B32-79D3-466A-A243-04B2C469CB1D`, `8371E3AC-3AFD-4F5C-9239-5C2C2EF6BC9B`, `CD00DB3B-CFB7-42E2-8B1A-D12BE584037D`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"cardRadius":8,"controlHeight":32}` |
| `spacing` | `{"buttonGap":8,"cardPadding":20,"fieldGap":16,"fieldsToTable":16,"titleToFields":16}` |
| `appearance` | `{"cardBackgroundToken":"--theme-surface","cardBorder":"none","cardShadow":"none","controlBorderToken":"--dcp-control-border"}` |
| `typography` | `{"controlFontSize":14,"labelFontSize":14,"titleFontSize":18}` |
| `states` | `{"disabled":"40% opacity and not-allowed cursor","focus":"tokenized focus ring","hover":"all interactive controls show tokenized hover","loading":"search button locks duplicate submission"}` |
| `layout` | `{"actions":"reset then search on the right","relationship":"filters and table remain inside one work card","subtitle":"omit","titleCount":1}` |
| `responsive` | `{"actions":"keep grouped and visible","fields":"resize with card and wrap only when required"}` |

覆盖说明：All filter controls are 32px and external spacing is 16px above and below.

## Button

- 置信度：`human-confirmed`
- 分类：`filter-form`
- Sketch Symbol：`0140381F-0983-47CE-9E16-146D85A97CE2`, `1ABB4789-DC5B-4C38-A45E-948DF69C397D`, `285ED4C4-78CE-4650-8F26-3046D18CD492`, `5C4DF08D-6654-4B2E-B9C0-41BA7120972F`, `7BA3FDFB-D0DF-40AD-9BE9-FC7832FAD94C`, `C395D1D7-0B6A-4140-825B-7A39328DF20C`, `C3F70649-9FCB-454B-8B07-35300AB1FAE3`, `D0D3A952-0D68-4AB0-9626-08C8EFEFD0B0`, `DEAC7624-5D27-4D21-94CD-061ED6D0CEC4`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"radius":4,"sizes":{"28":{"fontSize":12,"height":28,"horizontalPadding":12,"minWidthIconText":76,"minWidthText":56},"32":{"fontSize":14,"height":32,"horizontalPadding":12,"minWidthIconText":84,"minWidthText":64},"36":{"fontSize":14,"height":36,"horizontalPadding":16,"minWidthIconText":92,"minWidthText":72},"40":{"fontSize":16,"height":40,"horizontalPadding":16,"minWidthIconText":96,"minWidthText":80},"44":{"fontSize":16,"height":44,"horizontalPadding":20,"minWidthIconText":104,"minWidthText":88},"48":{"fontSize":16,"height":48,"horizontalPadding":20,"minWidthIconText":108,"minWidthText":96}}}` |
| `spacing` | `{"controlGroupGap":16,"iconTextGap":4,"sameGroupGap":8}` |
| `appearance` | `{"danger":"--dcp-button-danger-*","disabledOpacity":0.4,"primary":"--dcp-button-primary-*","secondary":"--dcp-button-secondary-*"}` |
| `typography` | `{"fontBySize":"see dimensions.sizes","weight":400}` |
| `states` | `{"active":"pressed token","disabled":"40% opacity and no action","focus":"visible focus ring","hover":"use component hover token","loading":"show loading and lock repeat click"}` |
| `layout` | `{"danger":"never solid primary","overflow":"use More menu","rowActionDirectLimit":3,"rowActionPrimaryLimit":1}` |
| `responsive` | `{"height":"fixed by size","width":"content adaptive but not below minimum width"}` |

覆盖说明：Exact button size, padding and table-action hierarchy were confirmed from the backend component rules.
