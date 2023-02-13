---
category: help
layout: help
mirrorid: archlinux
---

# Arch Linux 软件仓库镜像使用帮助

>  A lightweight and flexible Linux® distribution that tries to Keep It Simple.

编辑 `/etc/pacman.d/mirrorlist`，在文件的最顶端添加：

```
Server = https://{{ site.hostname }}/archlinux/$repo/os/$arch
```

更新软件包缓存：

```bash
sudo pacman -Syy
```
