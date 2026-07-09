# supervision-platform-ui
这是一个给 AI 使用的监管平台页面规范知识库。它帮助 ChatGPT、Claude、Cursor、Codex 等工具在改造后台页面时，尽量生成符合监管平台风格的页面结构、组件和视觉规则。

它不是业务系统源码，也不是可直接运行的前端项目。
适合做什么
把普通后台 Demo 改造成监管平台风格页面。
生成列表页、详情页、弹窗、看板等页面结构。
让 AI 按统一的组件、颜色、密度、排版规则输出设计或代码。
给团队成员下载后，在自己的 AI 工具里复用同一套页面规范。
目录说明

compiler/   给 AI 的总提示词、校验清单、Demo 改造提示词
knowledge/  设计原则、页面模式、组件规则、视觉规则、反例
data/       设计 token、组件库、页面配方、组件目录
docs/       面向使用者的流程说明
examples/   页面结构示例，不是可运行 Demo
assets/     监管平台背景图、图标、D-DIN-PRO 字体资源
ai-guides/  给任何 AI 阅读的通用能力指南
ai-prompts/ 可直接复制给任何 AI 的提示词
codex-skills/ Codex 可选安装的两个 skill
最快使用方式
把这个仓库放到你的业务项目旁边：


workspace/
- Supervision-KB/
- your-business-demo/
然后在 AI 工具里输入：


请先阅读 Supervision-KB/compiler/system-prompt.md，
再阅读 knowledge/、data/ 和 compiler/validation-checklist.md，
然后把我的页面改造成符合监管平台规范的版本。
如果只是想改一个已有 Demo，可以这样说：


请使用 Supervision-KB 的规则，保留原页面业务字段和操作流程，
只调整页面结构、组件样式、视觉密度和交互呈现。
不要新增无关功能，不要改成营销页或大屏风格。
任意 AI 使用方式
ChatGPT、Claude、Cursor、Gemini、通义、豆包等工具都可以使用本包。

推荐让 AI 先读：


compiler/system-prompt.md
compiler/validation-checklist.md
knowledge/
data/
ai-guides/
也可以直接复制这些提示词：


ai-prompts/page-refactor-prompt.md      页面重构
ai-prompts/component-style-prompt.md    组件样式优化
ai-prompts/validation-prompt.md         页面校验
Codex Skill 使用方式
如果使用 Codex，可以额外安装 codex-skills/ 里的两个 skill：


codex-skills/dorami-ui-protocol/
codex-skills/supervision-page-builder/
安装方式：

复制这两个目录到你的 Codex skills 目录。
常见位置是 ~/.codex/skills/。
重启 Codex。
安装后目录类似：


~/.codex/skills/dorami-ui-protocol/
~/.codex/skills/supervision-page-builder/
非 Codex 工具不能自动触发这些 skill，但可以直接阅读里面的 SKILL.md，当作高级说明文档使用。

推荐读取顺序
compiler/system-prompt.md
compiler/validation-checklist.md
knowledge/00-Core-Principles.md
knowledge/01-Design-DNA.md
knowledge/02-Component-DNA.md
knowledge/03-Page-Patterns.md
knowledge/04-Visual-Rules.md
knowledge/05-Anti-Patterns.md
knowledge/06-AI-Prompt.md
data/design-token.json
data/component-library.json
data/page-recipe.json
data/component-catalog.json
AI 工作流程
先判断页面类型：列表页、详情页、弹窗、看板、表单或混合流程。
从 data/page-recipe.json 选择页面结构。
从 data/component-library.json 匹配组件。
从 data/design-token.json 应用颜色、间距、高度、圆角和密度。
用 knowledge/05-Anti-Patterns.md 和 compiler/validation-checklist.md 做自检。
输出页面代码、组件映射说明和仍需确认的问题。
输出要求
保留原页面的业务流程、字段、筛选项、表格列和操作入口。
先说明识别到的页面类型，再说明使用的 Page Recipe。
优先使用 KB 已列出的组件；信息不足时写 TODO，不要乱造组件。
视觉表达保持克制、专业、高信息密度。
如发现规则冲突，先列出冲突点和影响，不要擅自改设计规则。
资源使用
本包已内置监管平台常用视觉资源：


assets/bg.jpg                 页面顶部背景图
assets/icons/                 功能图标 SVG
assets/fonts/D-DIN-PRO-*.otf  英文和数字字体
页面或 Demo 中请使用相对路径引用资源：


background-image: url("./assets/bg.jpg");

@font-face {
  font-family: "D-DIN-PRO-Alphanumeric";
  src: url("./assets/fonts/D-DIN-PRO-400-Regular.otf") format("opentype");
  font-weight: 400;
}
如果本仓库需要公开发布，请先确认字体、图标、背景图的分发授权。

不要做什么
不要改成官网、营销页、电商后台或其他产品主题。
不要新增通用设计系统。
不要新增与监管平台无关的组件。
不要使用 Hero Banner、大渐变、胶囊按钮、大圆角、彩色阴影。
不要把一次性 DEMO、预览 HTML、本机 skill 文件放回仓库。
