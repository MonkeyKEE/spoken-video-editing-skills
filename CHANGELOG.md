# 版本与迁移说明

当前配置模式版本为 `config_schema_version: "1.0"`。风格包使用自己的 `version`（SemVer），并用 `compatible_config_versions` 声明可兼容的配置模式范围。

## 2026-11-21：同步品牌工作流

- 文策阿峰 v2.2.0：真人开口、无标点字幕、语义动效和 B-roll 验收。
- 青年磁场 MC v1.3.0：定稿对照、首秒口播、字幕净尾、默认配乐和独立品牌片尾。
- 保留通用技能、风格注册表和配置契约。

## 1.0.1（发布前兼容补充）

- 增加 `skills/black-neon-talking-head/SKILL.md` 作为兼容引导，用于覆盖旧仓库中的同名文件，避免网页更新后残留旧技能与新的多风格流程并存。该文件只指向 `skills/talking-head-style-packaging/SKILL.md`，不再包含旧包装逻辑。
- 黑底荧光绿的完整风格定义只在 `styles/black-neon-talking-head/style.yaml`。

## 1.0.0（多风格架构）

相对早期「单一包装技能内嵌一种视觉样式、项目示例里直接写死视觉参数」的版本，本版本做了这些迁移：

- 核心工作流与风格包分离。剪辑与同步质检不再绑定某一种视觉样式。
- 原包装技能从绑定「黑底荧光绿」改为通用的 `talking-head-style-packaging`，按 `styles/catalog.yaml` 加载风格。
- `black-neon-talking-head` 迁入 `styles/black-neon-talking-head/style.yaml`，状态为 `verified-sample`，是当前唯一已验证样片风格。
- 新增 `styles/_blank-template/`。复制该模板可追加风格；模板本身不能直接出片，也不能被标记成已验证样片。
- 项目配置改为选择 `style.id`，必要时只用 `overrides` 覆盖当次项目，不再把完整风格复制进每个项目文件。
- 布局改为相对坐标（相对画幅的比例）加手机安全区策略，不再把某次样片的绝对像素位置当成可复用规范。
- 明确合并优先级、必填项、无效配置报错，以及风格不得覆盖的安全底线。
- 明确内容剪辑计划优先于包装，卡片出现与否由内容决定。
- 安装说明改为「技能 + 配套目录」一起提供，以便其他电脑和其他智能体使用。

若你手头还有早期的单文件风格配置（把颜色、标题、人物窗和编码写在同一份项目文件里），迁移步骤见 [docs/operations.md](docs/operations.md) 中的「从早期单风格配置迁移」和「离线迁移清单」。不要把早期示例里的 `1.1`×、约 `18Mbps` 或约 `−16LUFS` 当成新版本的硬要求。
