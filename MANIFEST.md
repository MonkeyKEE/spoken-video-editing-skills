# 文件清单与校验

- 项目：口播剪辑与可扩展视觉风格包（文档 + YAML 规范，不附带可执行渲染脚本）
- 许可：MIT License，Copyright (c) 2026 MonkeyKEE
- 配置模式：`config_schema_version: "1.0"`；可选扩展契约1.1；黑绿样式1.1.0
- 清单生成时间：2026-11-17 23:02 CST（Asia/Shanghai）

## 仓库文件

相对本目录：

- `LICENSE` — MIT 许可协议
- `README.md` — 项目介绍、目录、安装配套与能力边界
- `CHANGELOG.md` — 版本与迁移说明
- `contracts/config-contract.yaml` — 输入输出契约、合并优先级、必填项与报错规则
- `config/optional-presets.yaml` — 可选起始预设
- `examples/project.example.yaml` — 默认按场景计划的项目配置示例
- `examples/full-bleed-clean.project.example.yaml` — 明确选择后才使用的可选满屏/干净偏好项目覆盖
- `examples/style-profile.example.yaml` — 旧结构兼容参考，不作为新项目入口
- `styles/catalog.yaml` — 风格注册清单
- `styles/README.md` — 新增风格的方法
- `styles/black-neon-talking-head/style.yaml` — 唯一已验证样片风格
- `styles/_blank-template/style.yaml` — 空白风格模板
- `skills/spoken-video-editing-qc/SKILL.md` — 口播剪辑与音画同步质检
- `skills/talking-head-style-packaging/SKILL.md` — 口播视觉包装（多风格）
- `skills/black-neon-talking-head/SKILL.md` — 旧路径兼容引导，仅指向新包装技能，不含旧逻辑
- `docs/operations.md` — 安装、跨宿主与跨系统注意事项、离线迁移与 QA 清单
- `MANIFEST.md` — 本文件
- `CHECKSUMS.sha256` — 内容文件校验和（在本清单之后生成，不含压缩包）

本目录用于发布时，不应包含压缩包、可执行运行器、令牌、账号或私人路径。

## 校验说明

- 所有 YAML 可被解析。
- 风格注册清单与目录、`id` / `version` / `status` 一致；`verified-sample` 仅有 `black-neon-talking-head`；项目示例未选择模板风格。
- 项目示例包含契约中的必填项，且未削弱安全底线。
- Frontmatter：三份 `SKILL.md` 均含且仅含 `name`、`description`；`name` 为英文 kebab；`description` 为中文触发说明。兼容引导技能不含包装流程。
- 本地相对链接可解析。
- `LICENSE` 为标准 MIT 文本，版权行为 `Copyright (c) 2026 MonkeyKEE`。
- 敏感内容扫描：正文不含私人姓名、职务、本机或云盘绝对路径、真实视频文件名、令牌或账号。
- 换行均为 LF，无 UTF-8 BOM。

各内容文件的 SHA256 见 `CHECKSUMS.sha256`。

## 本次规范变更验证范围

- 两份通用技能正文与获确认正文逐字节匹配，保留原frontmatter；不包含具体项目身份、绝对路径或素材。
- YAML解析、样式版本/目录一致性、示例合并、可选字段枚举/条件约束、原锁定键、正文/本地链接及校验和检查；正反例由包外临时检查脚本执行，不把该脚本宣传为仓库已有自动验证器。
- 验证纯视觉修订可复用未变终速字幕的语义，不降低首次/改变干声后重新对齐要求；满屏和干净偏好都不成为全局强制。
- 未为这次文档/YAML变更重新做视频端到端渲染或新审片，也未对所有平台、系统或运行器作兼容保证。
