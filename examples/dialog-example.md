# Dialog Example

预警处理弹窗：

## 页面类型

Dialog

## Page Recipe

DialogTitle -> Content -> FooterAction

## 组件映射

- DialogTitle：说明局部任务，例如“处理预警”“确认提交”“退回原因”。
- Content：承载任务说明、必要字段、当前状态和处理意见。
- FooterAction：承载取消、确认等底部操作。
- StatusTag：可用于展示当前状态，不作为按钮。

## 使用边界

- Dialog 用于局部任务和短流程处理。
- 复杂信息查看应使用 Drawer。TODO：KB 未定义 Drawer 详细结构。
- 不要把完整详情页塞进 Dialog。

## 校验重点

- Dialog 圆角 12px。
- 内容保持紧凑、清晰，不使用透明浮层或毛玻璃。
- 操作按钮语义明确，不使用胶囊按钮。
