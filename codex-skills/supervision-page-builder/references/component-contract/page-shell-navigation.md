# 页面骨架与导航参数

最终参数优先于 Sketch 原始观测值；颜色必须使用已有 Theme/DCP token。

## PageShell

- 置信度：`human-confirmed`
- 分类：`page-shell-navigation`
- Sketch 画板：`2C802BEA-6E11-4AF4-BCB5-8C79112A8B98`, `4117FD63-C212-482C-AE9D-495AE0AA1EE0`, `6A7FF0EA-00CB-489B-817D-0C9C080274D3`, `6FDD8B32-79D3-466A-A243-04B2C469CB1D`, `8079E759-2356-40F7-B53C-E63D65326B9C`, `8371E3AC-3AFD-4F5C-9239-5C2C2EF6BC9B`, `911A6217-896E-454B-96AB-CDB13A63E39E`, `93811216-43EE-484E-A98F-4A9C214E8162`, `A40CFE91-1149-4FCA-A996-4201BD3737D9`, `C9611F9A-AC7A-4392-B7E0-04BFC8C6D580`, `CD00DB3B-CFB7-42E2-8B1A-D12BE584037D`, `E89831AA-68B8-46A4-9781-5D3D41BF0DF1`, `EF283AB9-4AF1-4765-810D-0A9AF4BCC159`, `F548738A-9447-4C91-AF95-E642DF7611B6`, `FAC5D152-CB18-43C7-A80F-B3E5F0B9CD05`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"contentMinWidth":1146,"minViewportWidth":1366,"sidebarWidth":220,"topbarHeight":56}` |
| `spacing` | `{"moduleGap":16,"pagePadding":20}` |
| `appearance` | `{"backgroundFallbackToken":"--theme-brand-1","backgroundImage":"assets/bg.jpg","backgroundPosition":"right region top","backgroundRepeat":"no-repeat"}` |
| `typography` | `{"alphanumericFontToken":"--font-number","uiFontToken":"--font-ui"}` |
| `states` | `{"default":"fixed sidebar and fluid right content"}` |
| `layout` | `{"belowMinimum":"keep 1366px canvas width and allow viewport horizontal scroll","content":"fluid width and independent scroll","sidebar":"fixed width and independent scroll"}` |
| `responsive` | `{"fixedProperties":["sidebar width","topbar height","component height"],"fluidProperties":["right content width","module width"],"minimumTotalWidth":1366}` |

覆盖说明：Confirmed adaptive platform shell and golden demo behavior.

## TopNavigation

- 置信度：`golden-demo-confirmed`
- 分类：`page-shell-navigation`
- Sketch 画板：`2C802BEA-6E11-4AF4-BCB5-8C79112A8B98`, `4117FD63-C212-482C-AE9D-495AE0AA1EE0`, `6A7FF0EA-00CB-489B-817D-0C9C080274D3`, `6FDD8B32-79D3-466A-A243-04B2C469CB1D`, `8079E759-2356-40F7-B53C-E63D65326B9C`, `8371E3AC-3AFD-4F5C-9239-5C2C2EF6BC9B`, `911A6217-896E-454B-96AB-CDB13A63E39E`, `93811216-43EE-484E-A98F-4A9C214E8162`, `A40CFE91-1149-4FCA-A996-4201BD3737D9`, `CD00DB3B-CFB7-42E2-8B1A-D12BE584037D`, `E89831AA-68B8-46A4-9781-5D3D41BF0DF1`, `EF283AB9-4AF1-4765-810D-0A9AF4BCC159`, `F548738A-9447-4C91-AF95-E642DF7611B6`, `FAC5D152-CB18-43C7-A80F-B3E5F0B9CD05`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"height":56,"organizationSelectorHeight":40}` |
| `spacing` | `{"horizontalPadding":20}` |
| `appearance` | `{"backdropBlur":6,"backgroundToken":"--theme-topbar-bg-60","shadow":"none"}` |
| `typography` | `{"fontSize":14,"textColorToken":"--theme-text-primary"}` |
| `states` | `{"default":"translucent","dropdownOpen":"popup above page content"}` |
| `layout` | `{"position":"sticky top of right region","stacking":"above content and page background"}` |
| `responsive` | `{"height":"fixed","width":"follow right content width"}` |

覆盖说明：Top bar starts over the page background and uses 60% white plus 6px blur.

## Sidebar

- 置信度：`human-confirmed`
- 分类：`page-shell-navigation`
- Sketch Symbol：`540EA192-3510-467F-8AC9-6E4A6896E60B`, `6AA86917-CFC6-45C6-B2F9-FA122B8EE6B3`, `8C7D3377-E2F6-4D45-8A91-82CE36598AE3`, `A0138E62-F0EB-4E68-BE58-B5E39078E31B`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"menuItemHeight":40,"selectedIndicatorWidth":3,"width":220}` |
| `spacing` | `{"childIndent":32,"menuItemHorizontalPadding":20}` |
| `appearance` | `{"backgroundToken":"--theme-sidebar-gradient","hoverBackgroundToken":"--theme-sidebar-hover-white-8","iconColorToken":"--theme-white","indicatorToken":"--theme-white","selectedBackgroundToken":"--theme-sidebar-selected-white-12","shadow":"none"}` |
| `typography` | `{"fontSize":14,"textColorToken":"--theme-sidebar-text"}` |
| `states` | `{"collapsed":"white recolorable arrow points down","default":"transparent","expanded":"white recolorable arrow points up","hover":"white 8% overlay without indicator","selected":"white 12% overlay plus left indicator"}` |
| `layout` | `{"position":"fixed left","scroll":"independent; do not scroll when menu content fits"}` |
| `responsive` | `{"height":"viewport height","width":"fixed"}` |

覆盖说明：Sidebar interaction states were confirmed against the detail-page demo.

## BusinessSwitch

- 置信度：`human-confirmed`
- 分类：`page-shell-navigation`
- Sketch Symbol：`613B5642-6AB3-41F3-BA29-D72E54AA495E`, `C65A8F22-9F17-4A51-8EA0-4B497212C26F`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"innerHeight":32,"outerHeight":40,"outerPadding":4}` |
| `spacing` | `{"equalInset":4,"innerGap":0}` |
| `appearance` | `{"innerRadius":16,"outerFillToken":"--theme-frosted-white-60-100","outerRadius":20,"outerStrokeMode":"inner","outerStrokeToken":"--theme-white","selectedFillToken":"--theme-primary","shadow":"none"}` |
| `typography` | `{"defaultTextToken":"--theme-text-secondary","fontSize":14,"selectedTextToken":"--theme-white"}` |
| `states` | `{"active":"sliding indicator animation","default":"unselected text","hover":"tokenized low-emphasis hover","selected":"filled active segment"}` |
| `layout` | `{"contentSync":"switch page content with selection","indicator":"slide between equal-width segments"}` |
| `responsive` | `{"height":"fixed","segmentWidth":"equal within component"}` |

覆盖说明：Outer frame stays 40px, inner item stays 32px, uses no shadow.
