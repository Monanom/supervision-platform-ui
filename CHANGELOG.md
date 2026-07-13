# CHANGELOG

## v1.1.0 - 2026-07-13

升级为更稳定的 AI 页面生成设计资产。

包含内容：
- 新增页面编译流程：页面理解、结构规划、组件映射、生成结果、一致性自检。
- 新增 `data/business-semantics.json`，沉淀监管业务对象、操作、状态和优先级。
- 新增 `data/field-component-map.json`，沉淀字段、状态、操作到组件的映射规则。
- 新增列表页、详情页、弹窗、看板、空状态、混合流程 Prompt 模板。
- 强化 `compiler/system-prompt.md` 和 `compiler/validation-checklist.md`。
- 同步更新 Codex skills 的职责边界和输出契约。

## v1.0.0 - 2026-07-10

首次发布 Supervision KB。

包含内容：
- 监管平台页面规范知识库。
- 任意 AI 可读的 `ai-guides/`。
- 可复制使用的 `ai-prompts/`。
- Codex 可选安装的 `codex-skills/`。
- 监管平台常用视觉资源 `assets/`。

使用者更新方式：
- 已 clone 仓库的用户执行 `git pull`。
- 使用 Codex skill 的用户重新复制 `codex-skills/` 下的两个 skill 到 `~/.codex/skills/`。
- 重启 Codex 后生效。
