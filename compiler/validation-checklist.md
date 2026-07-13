# Validation Checklist

## 业务完整性

- [ ] 是否保留用户提供的业务结构、字段、状态、操作和流程？
- [ ] 是否明确页面名称、页面类型、业务对象、使用角色和核心目标？
- [ ] 是否把信息不足处写成 TODO，而不是编造？
- [ ] 是否覆盖加载、空状态、错误、权限不足、禁用和保存中状态？

## 页面编译

- [ ] 是否先输出“页面理解”？
- [ ] 是否选择正确 Page Recipe？
- [ ] 是否说明页面阅读顺序和主要区域？
- [ ] 混合流程是否拆成清晰步骤，而不是堆在一个页面里？

## 组件一致性

- [ ] 是否使用 `data/component-library.json` 已有组件？
- [ ] 字段、状态、操作是否按 `data/field-component-map.json` 映射？
- [ ] 表格生命周期状态是否默认使用 StatusIndicator，而不是 Tag？
- [ ] 风险等级是否使用 RiskTag 或高权重状态表达？
- [ ] 操作过多时是否使用 More / Dropdown？
- [ ] 危险操作是否使用 Popconfirm 或 Modal 二次确认？

## Token 一致性

- [ ] 是否使用 Raw / Theme / Component 三层 Token？
- [ ] Page Padding 是否 20px 左右？
- [ ] Button / Tag / Input 是否使用 4px 小圆角？
- [ ] Card 是否使用 8px 或更小圆角？
- [ ] Dialog / Drawer 是否使用 12px 圆角？
- [ ] 是否避免硬编码新颜色、阴影、圆角和控件高度？

## 交互完整性

- [ ] Button、Input、Select、Table、Tabs、Pagination 是否有 hover / focus / disabled / active 状态？
- [ ] Modal / Drawer 是否说明关闭、滚动、footer 固定和危险操作行为？
- [ ] 表单是否包含校验、错误提示、提交 loading 和失败处理？
- [ ] 表格是否包含空数据、筛选为空、加载、错误和分页状态？

## 反例检查

- [ ] 是否避免 Hero Banner？
- [ ] 是否避免营销页、大屏风、电商风、通用 SaaS 风？
- [ ] 是否避免大面积渐变、霓虹、过度毛玻璃、胶囊按钮、大圆角和彩色阴影？
- [ ] 是否保持监管平台克制、专业、高信息密度？

## 输出可用性

- [ ] 是否输出组件映射表？
- [ ] 是否输出 token 和资源引用说明？
- [ ] 如输出代码，是否说明可运行方式和依赖边界？
