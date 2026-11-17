---
name: black-neon-talking-head
description: 兼容引导：旧的黑底荧光绿包装技能已迁移到 talking-head-style-packaging；发现本路径时请改用新技能和风格包，不要沿用旧的单风格逻辑。
---
# 已迁移：请改用多风格包装技能

本路径只为兼容旧仓库中的 `skills/black-neon-talking-head/SKILL.md` 而保留，**不再包含任何包装流程，也不得再按「技能名即风格、技能内嵌一套完整视觉规则」的旧逻辑执行**。

请立即改用：

- 包装工作流：[talking-head-style-packaging](../talking-head-style-packaging/SKILL.md)
- 黑底荧光绿样片风格定义：从包根目录读取 `styles/black-neon-talking-head/style.yaml`（本引导页不是风格配置）

执行顺序仍然是：先完成 `spoken-video-editing-qc`，再由 `talking-head-style-packaging` 按 `styles/catalog.yaml` 加载风格。若项目需要黑底荧光绿，在项目配置中设置 `style.id: black-neon-talking-head`，而不是继续使用本文件。

如果本文件与新包装技能同时存在，只遵循新技能和风格包；出现冲突时以新技能为准。不要并行执行两套包装规则。
