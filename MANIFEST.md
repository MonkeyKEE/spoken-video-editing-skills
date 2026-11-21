# 文件清单与校验

- 项目：口播剪辑与可扩展视觉风格包（文档 + YAML 规范，不附带可执行渲染脚本；品牌技能含只读依赖预检脚本）
- 许可：MIT License，Copyright (c) 2026 MonkeyKEE
- 配置模式：`config_schema_version: "1.0"`
- 清单生成时间：2026-11-17 13:16 CST（Asia/Shanghai）

## 仓库文件

相对本目录：

- `LICENSE` — MIT 许可协议
- `README.md` — 项目介绍、目录、安装配套与能力边界
- `CHANGELOG.md` — 版本与迁移说明
- `contracts/config-contract.yaml` — 输入输出契约、合并优先级、必填项与报错规则
- `config/optional-presets.yaml` — 可选起始预设
- `examples/project.example.yaml` — 项目配置示例
- `styles/catalog.yaml` — 风格注册清单
- `styles/README.md` — 新增风格的方法
- `styles/black-neon-talking-head/style.yaml` — 唯一已验证样片风格
- `styles/_blank-template/style.yaml` — 空白风格模板
- `skills/spoken-video-editing-qc/SKILL.md` — 口播剪辑与音画同步质检
- `skills/talking-head-style-packaging/SKILL.md` — 口播视觉包装（多风格）
- `skills/black-neon-talking-head/SKILL.md` — 旧路径兼容引导，仅指向新包装技能，不含旧逻辑
- `docs/operations.md` — 安装、跨宿主与跨系统注意事项、离线迁移与 QA 清单
- `skills/wenceafeng-koubocut/` — 文策阿峰竖屏工作流、验收规则及保留许可的上游快照
- `skills/qingnian-cichang-koubocut/` — 青年磁场 MC 横屏工作流、品牌及验收规则
- `MANIFEST.md` — 本文件
- `CHECKSUMS.sha256` — 内容文件校验和（在本清单之后生成，不含压缩包）

本目录用于发布时，不应包含压缩包、渲染运行器、令牌、账号或私人路径。

## 校验说明

- 所有 YAML 可被解析。
- 风格注册清单与目录、`id` / `version` / `status` 一致；`verified-sample` 仅有 `black-neon-talking-head`；项目示例未选择模板风格。
- 项目示例包含契约中的必填项，且未削弱安全底线。
- Frontmatter：三份通用技能含且仅含 `name`、`description`；品牌入口另含 `metadata` 记录版本。兼容引导不含包装流程。
- 本地相对链接可解析。
- `LICENSE` 为标准 MIT 文本，版权行为 `Copyright (c) 2026 MonkeyKEE`。
- 敏感内容扫描：正文不含私人姓名、职务、本机或云盘绝对路径、真实视频文件名、令牌或账号。
- 换行均为 LF，无 UTF-8 BOM。

各内容文件的 SHA256 见 `CHECKSUMS.sha256`。
