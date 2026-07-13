# Supervision KB

当前版本：v1.1.0  
更新时间：2026-07-13

`Supervision KB` 是一套给 AI 使用的监管平台页面规范包。它帮助 ChatGPT、Claude、Cursor、Codex 等工具，把产品需求或页面功能提示词转成符合监管平台风格的页面 demo。

它不是业务系统源码，也不是可直接运行的前端项目。

## 现有能力

- 根据产品文档或页面功能提示词，生成列表页、详情页、弹窗、看板、空状态、混合流程等页面 demo。
- 先输出页面理解、结构规划、组件映射，再生成页面，减少 AI 直接乱画。
- 统一监管平台的组件、颜色、密度、排版、状态、操作和视觉资源。
- 支持任意 AI 读取 `compiler/`、`knowledge/`、`data/`、`ai-guides/` 后使用。
- Codex 可额外安装两个 skill：
  - `dorami-ui-protocol`：基础组件协议，约束按钮、表格、弹窗、抽屉、表单等控件。
  - `supervision-page-builder`：监管平台页面生成规则，负责页面理解、业务语义、字段映射和视觉规范。
- 支持改造已有后台 demo，但建议谨慎使用，优先从产品文档或功能提示词生成。

## 推荐用法

### 方式一：根据产品文档或功能提示词生成页面

适合从 0 生成页面 demo，推荐优先使用。

```text
请先阅读 Supervision-KB/compiler/system-prompt.md、
compiler/validation-checklist.md、knowledge/、data/ 和 ai-guides/。

请根据以下页面功能提示词 / 产品文档，生成符合监管平台规范的页面 demo：
[粘贴页面功能提示词或产品文档]

页面功能提示词格式：
- 页面名称：
- 页面类型：列表页 / 详情页 / 弹窗 / 看板 / 空状态 / 混合流程
- 业务对象：
- 使用对象：
- 核心目标：
- 主要模块：
- 关键字段：
- 主要操作：
- 状态类型：
- 特殊说明：

要求：
- 先输出页面理解、结构规划、组件映射。
- 使用监管平台统一的组件、颜色、密度、排版规则。
- 输出页面 demo、关键样式和自检结果。
- 不要生成营销页、大屏风或通用 SaaS 风格。
```

### 方式二：改造现有 demo

适合已有后台页面，但要谨慎使用，避免旧 demo 的视觉风格影响输出。

```text
请先阅读 Supervision-KB/compiler/system-prompt.md、
compiler/validation-checklist.md、knowledge/、data/ 和 ai-guides/。

请将以下已有 demo 改造成符合监管平台规范的页面：
[粘贴 demo 代码、截图说明或页面结构]

要求：
- 保留原业务流程、字段、筛选项、表格列和操作入口。
- 只调整页面结构、组件样式、视觉密度和交互呈现。
- 使用监管平台组件和 token，不要自创组件。
- 信息不足处写 TODO，不要编造。
```

## 任意 AI 使用

ChatGPT、Claude、Cursor、Gemini、通义、豆包等工具都可以使用本包。

推荐让 AI 先读：

```text
compiler/system-prompt.md
compiler/validation-checklist.md
knowledge/
data/
ai-guides/
```

可直接复制的提示词在：

```text
ai-prompts/page-refactor-prompt.md      通用页面生成 / 重构
ai-prompts/list-page.prompt.md          列表页
ai-prompts/detail-page.prompt.md        详情页
ai-prompts/dialog.prompt.md             弹窗 / 抽屉
ai-prompts/dashboard.prompt.md          看板
ai-prompts/empty-state.prompt.md        空状态
ai-prompts/mixed-workflow.prompt.md     混合流程
ai-prompts/component-style-prompt.md    组件样式优化
ai-prompts/validation-prompt.md         页面校验
```

## Codex Skill 安装

如果使用 Codex，可以额外安装 `codex-skills/` 下的两个 skill。

复制：

```text
codex-skills/dorami-ui-protocol/
codex-skills/supervision-page-builder/
```

到：

```text
~/.codex/skills/
```

然后重启 Codex。

安装后目录类似：

```text
~/.codex/skills/dorami-ui-protocol/
~/.codex/skills/supervision-page-builder/
```

非 Codex 工具不能自动触发这些 skill，但可以直接阅读 `SKILL.md` 当作高级说明文档使用。

## 目录说明

```text
compiler/      AI 总提示词、页面编译流程、校验清单
knowledge/     设计原则、页面模式、组件规则、视觉规则、反例
data/          token、组件库、页面配方、业务语义、字段组件映射
ai-guides/     给任意 AI 阅读的通用指南
ai-prompts/    可复制给任意 AI 的提示词
codex-skills/  Codex 可选安装的 skill
assets/        背景图、平台 Logo、图标、D-DIN-PRO 字体
examples/      页面结构示例
docs/          使用补充说明
```

## AI 工作流程

1. 输出页面理解：页面类型、业务对象、使用角色、核心目标、字段、操作、状态和 TODO。
2. 输出结构规划：选择 Page Recipe、阅读顺序、页面区域和状态覆盖。
3. 输出组件映射：字段、操作、状态映射到监管平台组件和 Dorami 基础控件。
4. 生成页面 demo：使用统一 token、组件协议和监管平台视觉规则。
5. 一致性自检：按 `compiler/validation-checklist.md` 和反例规则检查。

## 资源使用

本包内置监管平台常用资源：

```text
assets/bg.jpg                 页面顶部背景图
assets/supervision-platform-logo-2x.png  平台 Logo
assets/icons/                 功能图标 SVG
assets/组件库icon.zip          Dorami 原始 icon 包
assets/fonts/D-DIN-PRO-*.otf  英文和数字字体
```

示例：

```css
background-image: url("./assets/bg.jpg");
```

```css
@font-face {
  font-family: "D-DIN-PRO-Alphanumeric";
  src: url("./assets/fonts/D-DIN-PRO-400-Regular.otf") format("opentype");
  font-weight: 400;
}
```

如果公开发布，请先确认字体、图标、背景图的分发授权。

## 更新方式

首次下载：

```bash
git clone git@github.com:Monanom/supervision-platform-ui.git
```

后续更新：

```bash
git pull
```

如果安装了 Codex skill，更新仓库后需要重新复制 `codex-skills/` 下两个目录到 `~/.codex/skills/`，并重启 Codex。

版本记录见：

```text
VERSION
CHANGELOG.md
```

## 不要做什么

- 不要改成官网、营销页、电商后台或其他产品主题。
- 不要新增通用设计系统。
- 不要新增与监管平台无关的组件。
- 不要使用 Hero Banner、大渐变、胶囊按钮、大圆角、彩色阴影。
- 不要把一次性 demo、预览 HTML、本机临时文件放回仓库。
