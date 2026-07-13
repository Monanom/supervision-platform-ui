# 通用 AI 使用流程

这份流程适用于 ChatGPT、Claude、Cursor、Gemini、通义、豆包等 AI 工具。

## 使用目标

让 AI 在改造后台页面时，先读取本仓库的监管平台规范，把需求编译成页面理解、结构规划和组件映射，再输出符合监管平台风格的页面结构、组件样式和校验结果。

## 推荐读取顺序

1. `compiler/system-prompt.md`
2. `compiler/validation-checklist.md`
3. `knowledge/00-Core-Principles.md`
4. `knowledge/01-Design-DNA.md`
5. `knowledge/02-Component-DNA.md`
6. `knowledge/03-Page-Patterns.md`
7. `knowledge/04-Visual-Rules.md`
8. `knowledge/05-Anti-Patterns.md`
9. `knowledge/06-AI-Prompt.md`
10. `data/design-token.json`
11. `data/component-library.json`
12. `data/page-recipe.json`
13. `data/business-semantics.json`
14. `data/field-component-map.json`
15. `data/component-catalog.json`

## 工作步骤

1. 让 AI 先读取上面的规范文件。
2. 提供原始页面代码、截图描述或页面结构。
3. 要求 AI 先输出页面理解：页面类型、业务对象、使用角色、目标、字段、操作、状态和 TODO。
4. 要求 AI 输出结构规划、组件映射和 token 使用方式。
5. 确认方向后，再让 AI 输出代码或设计稿。
6. 用 `compiler/validation-checklist.md` 做最后自检。

## 通用约束

- 保留原页面的业务字段、筛选项、表格列、流程和操作入口。
- 优先使用 `data/component-catalog.json` 中已有组件。
- 页面结构优先匹配 `data/page-recipe.json`。
- 业务语义优先匹配 `data/business-semantics.json`。
- 字段、状态、操作优先匹配 `data/field-component-map.json`。
- 颜色、间距、高度、圆角优先使用 `data/design-token.json`。
- 不要改成营销页、大屏、官网、电商后台或通用 SaaS 风格。
- 不要新增与监管平台无关的组件。
