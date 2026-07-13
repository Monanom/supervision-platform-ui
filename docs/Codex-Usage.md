# Codex Usage

本文说明在 Codex 中如何使用 Supervision KB。

## 推荐工作方式

1. 把 KB 仓库和业务项目放在同一个工作区。
2. 在 Codex 中明确要求先读取 KB。
3. 给 Codex 一个具体页面或 Demo，不要一次要求重构整个系统。
4. 让 Codex 先输出页面理解、结构规划、组件映射。
5. 确认页面方向后再修改页面文件。

## 推荐 Prompt

```text
你现在是 监管平台页面重构工程实现者。

请先阅读：
- Supervision-KB/compiler/system-prompt.md
- Supervision-KB/compiler/validation-checklist.md
- Supervision-KB/knowledge/
- Supervision-KB/data/

然后重构当前 Demo 页面。

约束：
- 保留业务结构、字段、流程和操作。
- 先输出页面理解、结构规划和组件映射。
- 使用 KB 中已有 Page Recipe、组件和 Token。
- 使用 business-semantics 和 field-component-map 处理业务语义。
- 不要新增通用设计系统。
- 不要自创组件。
- 信息不足处写 TODO。

输出：
1. 页面理解
2. 结构规划
3. 组件映射
4. 修改文件清单
5. 校验结果
```

## Codex 执行建议

- 一次只处理一个页面。
- 不让 Codex 删除业务字段，除非人工明确确认。
- 不让 Codex 改设计规则文件，除非任务目标就是维护 KB。
- 发现冲突时，先让 Codex 列冲突，不要直接改规则。

## 交付检查

Codex 完成后，应检查：

- 页面是否仍然表达原业务。
- 是否使用正确 Page Recipe。
- 是否只使用 KB 已有组件。
- 是否按业务语义映射字段、状态和操作。
- 是否符合圆角、间距、高度和背景规则。
- 是否没有出现 Anti Patterns。
