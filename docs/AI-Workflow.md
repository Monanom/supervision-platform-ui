# AI Workflow

本文定义 AI 使用本 KB 时的工作流程。

## 读取阶段

AI 必须先读取：

1. `compiler/system-prompt.md`
2. `compiler/validation-checklist.md`
3. `knowledge/`
4. `data/page-recipe.json`
5. `data/component-library.json`
6. `data/business-semantics.json`
7. `data/field-component-map.json`
8. `data/design-token.json`

## 判断阶段

AI 需要先输出页面理解：

- 页面名称。
- 页面类型。
- 业务对象。
- 使用角色。
- 核心目标。
- 关键字段。
- 主要操作。
- 业务状态。
- TODO。

页面类型包括：

- Dashboard：总体态势、关键指标、风险趋势、明细数据。
- ListPage：筛选、统计、表格、分页、操作。
- DetailPage：单个对象或事项的详情查看。
- Form：创建、编辑、提交信息。
- Dialog：局部任务、确认或短流程处理。
- EmptyState：无数据、筛选为空、无权限或加载失败。
- MixedWorkflow：详情、表单、附件、流转和下一步处理混合流程。

## 映射阶段

AI 需要输出组件映射表：

```text
业务区块 / 字段 / 状态 / 操作 -> KB 组件 -> Dorami 基础协议 -> 保留信息 -> TODO
```

示例：

```text
筛选区 -> SearchPanel -> Form/Input/Select/DatePicker -> 项目名称、区域、风险等级、状态、时间范围 -> 无
风险等级 -> RiskTag -> Tag -> 高风险、中风险、低风险 -> 无
处理状态 -> StatusIndicator -> StatusIndicator -> 已通知、处理中、已完成 -> 无
列表操作 -> RowActionGroup -> Button/Dropdown/Popconfirm -> 查看、处理、导出 -> 无
```

## 重构阶段

AI 只能做以下事情：

- 调整页面结构，使其符合 Page Recipe。
- 应用 KB 中已有组件。
- 应用 KB 中已有 Token。
- 按 `business-semantics.json` 保持监管业务优先级。
- 按 `field-component-map.json` 映射字段、状态和操作。
- 保留业务字段、流程、状态和操作。
- 对信息不足处写 TODO。

AI 不能做以下事情：

- 删除重要字段。
- 将表格改成电商风卡片。
- 添加未在 KB 中出现的组件。
- 使用 Hero Banner、毛玻璃、大渐变、胶囊按钮、大圆角、彩色阴影。
- 把所有状态都做成 Tag。
- 把风险等级降级成普通文本。

## 校验阶段

AI 输出前必须按 `compiler/validation-checklist.md` 自检，并说明：

- 已通过项。
- 未通过项。
- 信息不足导致的 TODO。

## 冲突处理

如果 `knowledge/` 与 `data/` 出现冲突：

1. 先列出冲突文件和冲突内容。
2. 说明对实现的影响。
3. 不擅自修改设计规则。
4. 若必须继续实现，选择更保守、更接近核心原则的方案，并写 TODO。
