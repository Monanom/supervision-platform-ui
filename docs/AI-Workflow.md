# AI Workflow

本文定义 AI 使用本 KB 时的工作流程。

## 读取阶段

AI 必须先读取：

1. `compiler/system-prompt.md`
2. `compiler/validation-checklist.md`
3. `knowledge/`
4. `data/`

## 判断阶段

AI 需要先判断 Demo 属于哪类页面：

- Dashboard：总体态势、关键指标、风险趋势、明细数据。
- ListPage：筛选、统计、表格、分页、操作。
- DetailPage：单个对象或事项的详情查看。
- Form：创建、编辑、提交信息。
- Dialog：局部任务、确认或短流程处理。

## 映射阶段

AI 需要输出组件映射表：

```text
原 Demo 区块 -> KB 组件 -> 保留信息 -> TODO
```

示例：

```text
筛选区 -> SearchPanel -> 项目名称、区域、风险等级、状态、时间范围 -> 无
列表区 -> DataTable -> 项目、主体、状态、时间、操作 -> 无
```

## 重构阶段

AI 只能做以下事情：

- 调整页面结构，使其符合 Page Recipe。
- 应用 KB 中已有组件。
- 应用 KB 中已有 Token。
- 保留业务字段、流程、状态和操作。
- 对信息不足处写 TODO。

AI 不能做以下事情：

- 删除重要字段。
- 将表格改成电商风卡片。
- 添加未在 KB 中出现的组件。
- 使用 Hero Banner、毛玻璃、大渐变、胶囊按钮、大圆角、彩色阴影。

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
