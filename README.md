# Spoken Video Editing Skills

口播剪辑与可扩展视觉风格包的流程规范。

本仓库把**核心工作流**和**风格包**分开：先按统一时间映射完成剪辑与音画质检，再加载一个已注册的风格包做包装。它是文档与 YAML 规范，**不附带可直接执行的渲染脚本**，也**不是一键剪辑或一键渲染工具**。把仓库复制到其他电脑、交给其他智能体后，应能按同一套契约工作，并继续添加新风格。

当前唯一已验证的样片风格是 `black-neon-talking-head`（近黑点阵底、荧光绿人物窗、句级白字幕）。它只是已验证样片，不是所有项目的默认风格。仓库同时提供空白风格模板，供后续追加风格；不要把空白模板直接当作成片风格，也不要杜撰第二个「已验证」风格。

许可协议见 [LICENSE](LICENSE)（MIT，Copyright (c) 2026 MonkeyKEE）。

完整配套包的发布地址：<https://github.com/MonkeyKEE/spoken-video-editing-skills>。

## 目录

| 路径 | 作用 |
|---|---|
| [skills/spoken-video-editing-qc/SKILL.md](skills/spoken-video-editing-qc/SKILL.md) | 核心工作流：探测、交叉转写、内容剪辑、统一变速与时间映射、终速字幕、混音、同步质检、交付 |
| [skills/talking-head-style-packaging/SKILL.md](skills/talking-head-style-packaging/SKILL.md) | 核心工作流：在时间轴对齐后，按风格包做人物窗、字幕、卡片、动效与安全区包装 |
| [skills/black-neon-talking-head/SKILL.md](skills/black-neon-talking-head/SKILL.md) | 兼容引导：旧路径仅指向新包装技能，不再包含旧的单风格逻辑 |
| [styles/catalog.yaml](styles/catalog.yaml) | 风格注册清单 |
| [styles/README.md](styles/README.md) | 如何新增风格 |
| [styles/black-neon-talking-head/style.yaml](styles/black-neon-talking-head/style.yaml) | 唯一已验证样片风格 |
| [styles/_blank-template/style.yaml](styles/_blank-template/style.yaml) | 空白风格模板，不可直接用于出片 |
| [contracts/config-contract.yaml](contracts/config-contract.yaml) | 输入输出契约、合并优先级、必填项与报错规则 |
| [config/optional-presets.yaml](config/optional-presets.yaml) | 可选起始预设（语速、画幅、编码、响度），不是硬规范 |
| [examples/project.example.yaml](examples/project.example.yaml) | 项目配置示例 |
| [docs/operations.md](docs/operations.md) | 安装配套目录、跨宿主与跨系统注意事项、能力检查、离线迁移与 QA 清单 |
| [CHANGELOG.md](CHANGELOG.md) | 版本与迁移说明 |
| [MANIFEST.md](MANIFEST.md) | 文件清单与校验说明 |
| [CHECKSUMS.sha256](CHECKSUMS.sha256) | 内容文件 SHA256 |

## 使用顺序

1. 复制本仓库到目标电脑，或把完整目录提供给智能体。不要只复制一份 `SKILL.md` 却丢掉 `styles/`、`contracts/`。
2. 先复制 [examples/project.example.yaml](examples/project.example.yaml) 为当次项目配置，填写项目 ID、所选风格 ID、单一 `SPEED` 和输出预设。媒体定位符只放在本机不共享的本地配置里，不要写进风格包或共享项目文件。
3. 执行 `spoken-video-editing-qc`，产出内容剪辑计划、统一 `segments` / `frame_map`、终速干声和逐句字幕。
4. 时间轴对齐后，再执行 `talking-head-style-packaging`。包装必须依据内容计划，而不是按风格固定弹卡频率。
5. 完成直接视听审片后再交付；未经授权不自动发布。

## 配置合并与安全底线

合并顺序（后者覆盖前者，但不能削弱安全底线）：

1. [config/optional-presets.yaml](config/optional-presets.yaml) 中的可选起始预设
2. 所选风格包 `styles/<id>/style.yaml`
3. 项目配置中的覆盖项

同步、隐私、直接视听验收和「不自动发布」是锁定规则，风格包和项目覆盖都不能关闭。完整规则见 [contracts/config-contract.yaml](contracts/config-contract.yaml)。语速、画幅、码率和响度都是可配置预设，例如 `1.1`× 或 `9:16` / `1440×2560` / `30fps` 只是可选起点，不是永久硬要求。

## 可选镜头语言与纯视觉修订

按参考风格须动态比较镜头角色、占屏、布局、MG和声音，不只仿配色。B-roll按语义选镜并检查可见动作去重；窗口/满屏均可选，参见[满屏干净画面项目示例](examples/full-bleed-clean.project.example.yaml)。它是明确选择的项目覆盖，不是所有品牌默认，不是自动profile加载功能；满屏等比主体锚定覆盖目标画布并保留必要标题/字幕/头像，不用窗框、底纹、拉伸或模糊补边伪装。

通用库存/抽象图形不默认强加解释标签；来源/许可局限、性质及事实限制始终保留在manifest。干净偏好不豁免必要披露，也不允许伪造经历、官方界面或统计背书。仅改画面且声音/文案/时间轴未变时可复用已对齐终速字幕、音轨与映射，不能再变速。每个新终版仍需完整动态直接审片，不继承旧PASS。

契约规范版本1.1增加可选字段，项目配置模式仍为1.0、原必填项及安全底线不变；所选黑绿风格更新为1.1.0。旧项目不必开启新选项。规则见[配置契约](contracts/config-contract.yaml)和[操作/验收](docs/operations.md)。这些仍是文档/YAML规范，不附渲染器，也不代表已有自动运行时验证。

## 旧路径兼容

若更新仓库时仍看到 `skills/black-neon-talking-head/SKILL.md`，那是为了覆盖旧版同名文件而保留的兼容引导，不是第二套包装技能。遇到该路径时，改用 `skills/talking-head-style-packaging/SKILL.md`，并从包根读取 `styles/black-neon-talking-head/style.yaml`。不要同时执行两套逻辑。

## 安装时要复制什么

推荐：整仓复制，再按宿主注册两个技能。最低配套如下。

| 目的 | 必须一起提供 |
|---|---|
| 只做剪辑与同步质检 | `skills/spoken-video-editing-qc/`、`contracts/`、`config/`、`examples/`、`docs/operations.md` |
| 做视觉包装 | 上一行全部，外加 `skills/talking-head-style-packaging/` 与整个 `styles/` |
| 以后还要加风格 | 整个仓库，尤其是 `styles/` 与 `styles/README.md` |

支持两类智能体：能读取通用 `SKILL.md` 的宿主，以及只能接收聊天提示词的智能体。后一类要把技能正文、契约、所选风格包和项目示例一并提供。路径、字体与 ffmpeg 的系统差异见 [docs/operations.md](docs/operations.md)。

## 能力边界

- 不保证按规范操作后一定得到可发布成片，也不提供一键渲染。
- 不得把一次样片的坐标、电平、字体替代或导出参数，写成所有品牌、所有系统的强制规范。
- 图库、生成图或示意动画不能冒充真实现场记录。
- `watchVideo` / `videoReview` 只是部分宿主的看片能力，不是公开命令行工具；没有它们时必须做等价人工视听审片，不得跳过或声称已看。
- 许可证按「原样」提供，详见 [LICENSE](LICENSE)。
