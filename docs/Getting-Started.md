# Getting Started

本文说明如何使用 Supervision KB 指导 AI 重构普通后台 Demo。

## 适用场景

- 将普通后台 Demo 调整为监管平台页面。
- 让 AI 在生成页面前先读取统一规范，并把需求编译成页面理解、结构规划和组件映射。
- 检查页面是否符合监管平台的克制、专业、高信息密度要求。

## 不适用场景

- 创建通用设计系统。
- 重新设计监管平台品牌。
- 扩展成乐采、政采、电商、营销页或其他产品主题。
- 新增未在 KB 中出现的业务组件。

## 最小使用步骤

1. 将 `Supervision-KB/` 放在业务项目旁边。
2. 让 AI 先读取 `compiler/system-prompt.md`。
3. 让 AI 继续读取 `knowledge/`、`data/page-recipe.json`、`data/component-library.json`、`data/business-semantics.json`、`data/field-component-map.json` 和 `data/design-token.json`。
4. 输入 Demo 代码、页面描述或截图信息。
5. 要求 AI 输出页面理解、结构规划、组件映射、代码和校验清单。

## 推荐输入

```text
请先阅读 Supervision-KB/compiler/system-prompt.md，
再阅读 knowledge/ 与 data/。

现在请将以下 Demo 重构为 监管平台页面：
[粘贴 Demo 代码或页面描述]

输出：
1. 页面理解
2. 结构规划
3. 组件映射
4. 重构后的代码
5. 校验清单
6. TODO
```

## 验收标准

- 业务结构、字段、流程没有被删除或改写。
- 页面类型选择合理。
- 页面结构符合 `data/page-recipe.json`。
- 组件来自 `data/component-catalog.json`。
- 业务语义符合 `data/business-semantics.json`。
- 字段、状态、操作映射符合 `data/field-component-map.json`。
- Token 符合 `data/design-token.json`。
- 没有出现 `knowledge/05-Anti-Patterns.md` 中的禁用项。
