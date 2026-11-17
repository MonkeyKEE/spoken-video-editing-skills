# 文件清单与校验

- 项目：口播剪辑与黑底荧光绿视觉包装技能（流程/模板，不附带可执行渲染脚本）
- 许可：MIT License，Copyright (c) 2026 MonkeyKEE
- 清单生成时间：2026-11-17 12:55 CST（Asia/Shanghai）

## 仓库文件

相对本目录：

- `LICENSE` — MIT 许可协议
- `README.md` — 项目介绍、依赖、使用顺序与能力边界
- `examples/style-profile.example.yaml` — 项目配置示例，不含姓名、职务、品牌或私有路径
- `skills/spoken-video-editing-qc/SKILL.md` — 口播剪辑与音画同步质检
- `skills/black-neon-talking-head/SKILL.md` — 黑底荧光绿口播视觉包装
- `MANIFEST.md` — 本文件
- `CHECKSUMS.sha256` — 内容文件校验和（在本清单之后生成，不含压缩包）

本目录用于开源发布时，不应包含压缩包、令牌、账号或私人路径。

## 校验说明

- Frontmatter：两份 `SKILL.md` 均含且仅含 `name`、`description`；`name` 为英文 kebab；`description` 为中文触发说明。
- 本地链接：README、许可协议、技能互引与示例配置的相对链接均可解析。
- `LICENSE` 为标准 MIT 文本，版权行为 `Copyright (c) 2026 MonkeyKEE`。
- 敏感内容扫描：正文不含私人姓名、职务、本机或云盘绝对路径、真实视频文件名、令牌或账号。
- 示例配置可被 YAML 解析，只含占位与可选预设。
- 换行均为 LF，无 UTF-8 BOM。
- 技能正文声明：本仓库不附带可直接执行的渲染脚本，也不构成一键剪辑；`watchVideo` / `videoReview` 是宿主能力而非公开命令行工具，缺失时必须做等价人工视听审片，不得跳过或声称已看。

各内容文件的 SHA256 见 `CHECKSUMS.sha256`。
