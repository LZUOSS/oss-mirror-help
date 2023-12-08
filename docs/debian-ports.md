---
category: help
layout: help
mirrorid: debian-ports
---

# debian-ports 镜像使用帮助

> debian-ports 将 Debian 发行版移植到 riscv64、loong64 等架构上，[官方网站](https://www.debian.org/ports/)。

{{ site.org.nameUpper }} 提供了 ia64、riscv64、loong64 等架构 Debian 发行版的软件包仓库。以 riscv64 为例，编辑 `/etc/apt/sources.list`，注释所有内容，添加以下几行保存：

```bash
deb [arch=riscv64] http://{{ site.hostname }}/debian-ports unstable main
deb [arch=riscv64] http://{{ site.hostname }}/debian-ports unreleased main
```

> [!tip] 其他架构类似，可能会有一些变化。