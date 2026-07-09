# 校验提示词

复制下面提示词给任意 AI 使用。

```text
请按照 监管平台规范校验当前页面。

请读取：
- compiler/validation-checklist.md
- knowledge/05-Anti-Patterns.md
- data/page-recipe.json
- data/component-catalog.json
- data/design-token.json

请检查：
1. 页面类型是否判断合理。
2. 页面结构是否符合 Page Recipe。
3. 组件是否来自组件目录。
4. 颜色、间距、高度、圆角是否符合 token。
5. 是否保留原业务字段、流程和操作入口。
6. 是否出现营销页、大屏、电商后台、通用 SaaS 等错误方向。
7. 是否出现大渐变、胶囊按钮、大圆角、彩色阴影等反例。

请按下面格式输出：
- 通过项
- 问题项
- 修改建议
- 是否可以交付
```

