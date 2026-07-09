# Dorami 组件协议通用指南

这份指南把 Codex skill 中的 Dorami 组件规则改写成任何 AI 都能读取的说明。

## 组件定位

Dorami 在这里不是必须安装的前端依赖，而是一套基础组件协议。AI 生成静态 Demo、Figma 风格稿或真实 Vue 代码时，都应先遵守这套组件结构和状态规则。

## 输出模式

- `static-demo`：默认模式。使用 HTML/CSS/JS 复现组件外观和状态，不引入 Vue 或 Dorami。
- `figma-like`：用于可编辑视觉稿，保留组件结构、层级和状态。
- `vue-dorami`：只有明确要求真实 Vue/Dorami 生产代码时使用。

## 基础组件范围

适用于：

- Button
- Tag
- Modal
- Drawer
- Select
- Dropdown
- Pagination
- Table
- Form
- Input
- Tooltip
- Popconfirm

## 生成规则

1. 基础控件要有稳定结构、状态和交互语义。
2. 业务页面只决定内容、字段、操作优先级，不重新发明基础控件。
3. 静态 Demo 可使用 `dcp-*` 类名表达组件协议，例如 `dcp-button`、`dcp-table`、`dcp-modal`。
4. 主题使用三层 token：Raw tokens、Theme tokens、Component tokens。
5. 页面布局使用 `--theme-*`，组件样式使用 `--dcp-*`。
6. 不要在组件里随手写一次性颜色、圆角和高度。

## 与监管平台规则配合

生成监管平台页面时，先遵守 Dorami 组件协议，再叠加 `ai-guides/supervision-page-builder-guide.md` 中的业务视觉规则。

