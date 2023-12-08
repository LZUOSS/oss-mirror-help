---
category: help
layout: help
mirrorid: deepin
---

# deepin 软件仓库镜像使用帮助

- [官方网址](https://www.deepin.org)

```bash
sed -e 's|community-packages.deepin.com/deepin|{{ site.hostname }}/deepin|g' \
    -i.bak \
    /etc/apt/sources.list
```