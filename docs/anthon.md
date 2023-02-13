---
category: help
layout: help
mirrorid: anthon
---

# AOSC OS（安同 OS）镜像使用帮助

> AOSC OS is a general purpose Linux distribution that strives to simplify user experience and improve free and open source software for day-to-day productivity.

AOSC OS 是一个由[安同开源社区](<https://aosc.io>)开发的半滚动 Linux 发行版，支持多种处理器架构。

AOSC OS 内置 `apt-gen-list` 工具来切换社区提供的可用镜像源。要启用 {{ site.org.nameUpper }} 源，执行：

```bash
sudo apt-gen-list add-mirror {{ site.org.nameLower }}
```

要仅启用 {{ site.org.nameUpper }} 源，执行：

```bash
sudo apt-gen-list set-mirror {{ site.org.nameLower }}
```

若要启动 TUNA 源，将上述命令的 `{{ site.org.nameLower }}` 改为 `tuna` 即可。

关于 `apt-gen-list` 的语义和详细用法，请执行 `apt-gen-list help` 查看帮助。
