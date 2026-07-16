# 弹窗与抽屉参数

最终参数优先于 Sketch 原始观测值；颜色必须使用已有 Theme/DCP token。

## Modal

- 置信度：`manual-calibrated`
- 分类：`modal-drawer`
- Sketch 画板：`446578C5-D814-4FC5-BD9E-C5B6668AFE70`, `6C5E3809-968A-435E-AB6C-8EE93ACAEDF2`, `8079E759-2356-40F7-B53C-E63D65326B9C`, `911A6217-896E-454B-96AB-CDB13A63E39E`, `93811216-43EE-484E-A98F-4A9C214E8162`, `ED8BEF09-3C43-4A78-90AC-7C730786A2E2`, `FAC5D152-CB18-43C7-A80F-B3E5F0B9CD05`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"closeIconSize":16,"confirmWidth":400,"defaultWidth":520,"footerButtonHeight":32,"formWidth":640,"maxHeight":"calc(100vh - 48px)","maxWidth":"calc(100vw - 48px)","radius":12}` |
| `spacing` | `{"bodyPadding":24,"footerButtonGap":8,"footerPadding":24,"headerPadding":24}` |
| `appearance` | `{"backgroundToken":"--theme-surface","closeIcon":"assets/icons/close.svg","divider":"none","overlayToken":"--dcp-overlay-mask"}` |
| `typography` | `{"bodyFontSize":14,"titleFontSize":18}` |
| `states` | `{"close":"icon, Escape or mask according to risk","open":"focus enters modal","submitFailed":"keep input and show error","submitting":"primary loading and duplicate submit locked","validationError":"keep modal open and focus first error"}` |
| `layout` | `{"body":"scroll when content exceeds max height","closeControl":"icon only","footer":"stable and right aligned","header":"stable"}` |
| `responsive` | `{"bodyScroll":"internal","width":"use size variant up to maxWidth"}` |

覆盖说明：Base Modal shell follows Dorami; supervision theme only supplies atomic tokens.

## Drawer

- 置信度：`manual-calibrated`
- 分类：`modal-drawer`
- Sketch 画板：`EF283AB9-4AF1-4765-810D-0A9AF4BCC159`

| 参数组 | 最终规范 |
| --- | --- |
| `dimensions` | `{"closeIconSize":16,"defaultWidth":520,"maxWidth":"90vw","radius":12,"wideWidth":640}` |
| `spacing` | `{"bodyPadding":24,"footerPadding":24,"headerPadding":24}` |
| `appearance` | `{"backgroundToken":"--theme-surface","closeIcon":"assets/icons/close.svg","divider":"none","overlayToken":"--dcp-overlay-mask"}` |
| `typography` | `{"bodyFontSize":14,"titleFontSize":18}` |
| `states` | `{"close":"restore focus to trigger","disabledAction":"show reason with Tooltip when required","loading":"body-local loading","open":"focus enters drawer"}` |
| `layout` | `{"body":"independent scroll","closeControl":"icon only","footer":"stable when actions exist","header":"stable","placement":"right"}` |
| `responsive` | `{"height":"viewport height","width":"variant width up to maxWidth"}` |

覆盖说明：Base Drawer shell follows Dorami; business content remains in slots.
