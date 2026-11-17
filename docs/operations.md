# 安装、迁移与验收

本文说明如何在其他电脑和其他智能体中使用本仓库，以及如何做能力检查、离线迁移和质检。它不是渲染教程，也不提供一键命令。

## 1. 安装时要复制的目录

推荐始终复制整个仓库。若必须拆开安装，最低配套是：

- 使用 [口播剪辑与音画同步质检](../skills/spoken-video-editing-qc/SKILL.md)：一并提供 `skills/spoken-video-editing-qc/`、`contracts/`、`config/`、`examples/` 和本文件。
- 使用 [口播视觉包装（多风格）](../skills/talking-head-style-packaging/SKILL.md)：在上一套基础上再提供 `skills/talking-head-style-packaging/` 和整个 `styles/`。
- 若目录中仍有 [旧路径兼容引导](../skills/black-neon-talking-head/SKILL.md)，它只用于覆盖旧文件并指向新包装技能，不能单独当作包装流程，也不要和它并行执行另一套旧逻辑。
- 还要新增风格：必须保留完整的 `styles/`，并按 [styles/README.md](../styles/README.md) 登记。

只安装一份 `SKILL.md`、却没有契约和风格包时，智能体应先索取完整仓库或让用户把配套 YAML 贴进对话，不能凭记忆补造风格参数。

### 通用 SKILL.md 宿主

把两个技能目录放到宿主的技能搜索路径中，并保证相对仓库根目录仍能解析到 `styles/`、`contracts/`、`config/`、`examples/` 和 `docs/`。若宿主只能看到技能目录、看不到仓库其余部分，应在项目对话里明确给出本仓库在该电脑上的根位置，或把所需 YAML 作为附件提供。共享文件里不要写死该电脑的绝对路径。

### 仅能接收聊天提示词的智能体

在一次任务中至少提供：两个技能的 `SKILL.md`、[contracts/config-contract.yaml](../contracts/config-contract.yaml)、[styles/catalog.yaml](../styles/catalog.yaml)、所选风格的 `style.yaml`、[examples/project.example.yaml](../examples/project.example.yaml) 或当次项目配置，以及本文件中与审片、路径和 QA 有关的章节。不要假设它拥有 `watchVideo`、`videoReview` 或其他宿主专有工具。

## 2. 路径、字体与系统差异

共享配置只使用相对仓库根目录的路径，分隔符统一为 `/`。本机媒体、缓存和字体文件位置放到不共享的本地定位文件中，不要提交进风格包。

字体在风格包里只写字体族名称和 fallback 列表。由当次环境把字体族解析成可用字体；解析失败应记录并按风格中的 `on_missing_*` 规则处理，缺全部字体则报错，而不是改写风格包为某台电脑的字体文件路径。

下列命令用于检查当前环境是否具备常见能力。其中 Linux 命令在本仓库整理时，于 Linux x86_64 环境实际运行过，只能证明「这些检查命令在该环境可执行」，**不代表已在 Windows、macOS 或所有发行版上测试，也不代表必须使用当时见到的软件版本**。

在 Linux 上可运行：

```bash
ffmpeg -hide_banner -version
ffprobe -hide_banner -version
python3 --version
python3 -c "import yaml; print(yaml.__version__)"
python3 -c "import faster_whisper; print('faster-whisper-import-ok')"
ffmpeg -hide_banner -filters
```

若系统提供字体族查询，还可检查风格里的字体族是否存在，但查询工具本身不是本规范的必装依赖。

Windows 与 macOS 上的等价检查（**本版本未实测**，仅作提示）：

- 确认 `ffmpeg`、`ffprobe` 已进入 PATH 后，同样运行 `ffmpeg -hide_banner -version` 与 `ffprobe -hide_banner -version`。
- Python 可能叫 `python3`、`python` 或 `py -3`。先确认解释器，再检查 `yaml` 与（如需转写）`faster_whisper` 能否导入。
- 不要把盘符路径或用户主目录写进共享 YAML。`ffmpeg` 的 `fontfile=` 若必须使用本机路径，只应出现在本机渲染实现里，不应回写到风格包。

缺少某一依赖时，应在 QA 记录里标明，并停止声称该步骤已经完成。例如没有转写工具就不能假装已经交叉转写。

## 3. 审片能力

`watchVideo` 和 `videoReview` 是部分宿主提供的看片/审片能力，不是本仓库附带的公开命令行工具。宿主没有这些能力时，必须用系统播放器或其他可播放的成片/代理，做等价的人工视听审片。不得跳过，也不得在未看未听时声称已经审过。换到另一台电脑或另一个智能体后，不能继承上一处的「已审」结论，需要重新视听。

## 4. 从早期单风格配置迁移

1. 把原来写在项目文件里的颜色、字体、人物窗、卡片、音效和结尾参数，迁入一个风格目录；若仍是黑底荧光绿样片，直接对照 [styles/black-neon-talking-head/style.yaml](../styles/black-neon-talking-head/style.yaml)，不要把旧的绝对像素坐标原样照搬。
2. 项目文件只保留 `style.id`、当次 `overrides`、单一 `SPEED`、输出预设和内容计划。
3. 编码、画幅、响度若仍采用旧示例值，应标明这是可选预设，见 [config/optional-presets.yaml](../config/optional-presets.yaml)。
4. 包装技能改用 `talking-head-style-packaging`，不再假设技能名等于风格名。 若仍看到 `skills/black-neon-talking-head/SKILL.md`，只把它当作跳转到新技能的引导页。
5. 在新环境做能力检查和直接视听验收，不要沿用旧环境的「已通过」记录。

## 5. 离线迁移清单

在电脑 A 整理、到电脑 B 或另一个智能体继续工作时：

- 复制整个仓库，不要只复制技能正文。
- 不要复制凭证、账号、本机媒体原片（除非用户明确要求并使用安全传输）。
- 不要复制含绝对路径的本地定位文件；在新电脑上重新填写媒体定位。
- 用新电脑上的 `ffmpeg` / `ffprobe` / Python / 字体解析做能力检查。
- 按宿主类型安装或粘贴技能与配套 YAML。
- 确认所选 `style.id` 仍在 `styles/catalog.yaml` 中，且 `style.yaml` 一起被复制。
- 重新解析字体 fallback，不要沿用上一台电脑的字体文件路径。
- 重新做直接视听审片后再交付。
- 不自动发布，不改未授权的共享权限。

## 6. QA checklist

交付前至少核对：

- 项目配置、风格包和可选预设均可解析，并按契约完成合并；没有锁定规则被削弱。
- 所选风格已注册，且不是 `_blank-template`。
- 共享文件不含绝对路径、字体文件路径或私人信息。
- 已探测源旋转、VFR 与音轨 PTS，人声音轨经过确认。
- 内容剪辑计划完整，切点在能量低点附近，包装卡片均能回溯到该计划。
- 音画共用一个 `SPEED`，各自只变速一次；存在统一的 `segments` / `frame_map`。
- 终速干声已重新转写字幕，没有把旧字幕按比例拉伸了事。
- 有效人声时长与画面时间轴相符，没有用静音 padding 把错误语速撑到容器等长。
- 已测综合响度与真峰值；音乐和音效不盖人声。
- 标题和关键文字按相对坐标放置，并在目标手机的留边与铺满两种模式下检查安全区；完整保留头顶，卡片不压脸。
- 素材来源诚实，没有循环或倒放人物来凑时长，也没有把示意图冒充现场。
- 已直接视听片头、片中、片尾、接缝、字幕、安全区、声音和结尾。若未视听，状态只能是待审预览。
- 交付物含版本化成片或预览、合并后的配置快照和 QA 记录；未自动发布。
