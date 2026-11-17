# 风格包说明

风格包是自包含的视觉与声音语言定义，位于 `styles/<id>/`。核心工作流技能不把某一种样式写死在正文里，而是读取 [catalog.yaml](catalog.yaml) 再加载对应的 `style.yaml`。

## 已注册风格

- `black-neon-talking-head`：`verified-sample`。当前唯一已验证样片风格。
- `_blank-template`：`template`。空白模板，不能直接用于出片。

不要在没有经过样片验证和用户确认时，把新风格写成 `verified-sample`。

## 新增风格

1. 复制整个 `styles/_blank-template/` 目录，改名为新的稳定 id。id 使用英文小写 kebab，例如 `warm-paper-talking-head`，且不得以下划线开头（下划线前缀留给模板）。
2. 打开新的 `style.yaml`，把 `id` 改成与目录名一致，将 `status` 设为 `draft`，保留或更新 `version`（建议从 `1.0.0` 起）和 `compatible_config_versions`。
3. 填完必填项：适用边界、颜色与 fallback、字体族与 fallback、相对坐标布局、手机安全区、字幕、人物窗、卡片、动效、音效、BGM、结尾，以及参考资产的版权与来源。只写字体族名称，不写本机字体文件路径。
4. 在 [catalog.yaml](catalog.yaml) 增加一条登记，`path` 指向新的 `style.yaml`。
5. 用一份项目配置将 `style.id` 指向新风格。若该风格尚未验证，交付时必须标明 `draft`，不能宣传为本仓库已验证样片。
6. 按 [docs/operations.md](../docs/operations.md) 的 QA 清单做安全区与直接视听验收。通过并经使用方确认后，可将项目侧状态写为 `confirmed`；只有在本仓库确实有可复核的样片依据时，才考虑登记为 `verified-sample`。

## 自包含规则

- 风格包优先把参数写进 `style.yaml`，不依赖宿主特定路径。
- 如需图片、音乐或字体文件，放在同一风格目录内，并在 `assets` 里写明许可证与来源；未附带二进制文件时，也要声明是程序化参数还是外部需自行取得的资源。
- 共享文件中的路径一律相对仓库根目录，使用 `/` 分隔。
- 风格可以提供推荐画幅或推荐动效时长，但不能覆盖同步、隐私和直接视听验收的安全底线，也不能规定「每隔固定秒数必须弹卡」。

## 可选镜头语言与素材说明
可提供窗口/满屏B-roll、多种人物布局和步骤/横向/循环/分组MG能力，但是否启用由内容计划和项目选择决定；不能把某个9:16样片的满屏偏好升级为所有品牌默认。参数以项目目标画布与逐镜主体锚点为准，记录裁切取舍，不给出跨项目固定头像坐标或镜头数。
通用库存/抽象图形不默认强加素材性质标签。来源与许可证据/局限必须进manifest，干净偏好不得关闭法律、平台或避免实质误导所需的披露；不得冒充用户活动、官方界面或统计事实。定义/验证规则见[契约](../contracts/config-contract.yaml)，可选项目覆盖见[满屏示例](../examples/full-bleed-clean.project.example.yaml)。
