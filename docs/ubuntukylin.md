---
category: help
layout: help
mirrorid: ubuntukylin
---

# 优麒麟软件源镜像使用帮助

- [官方网址](https://www.ubuntukylin.com/)

以 20.04 Pro 为例，配置方法：

```bash
cp -a /etc/apt/sources.list /etc/apt/sources.list.bak
cat <<-EOF >> /etc/apt/sources.list

deb https://{{ site.hostname }}/ubuntukylin/ focal main
deb https://{{ site.hostname }}/ubuntukylin/ focal-partner main

EOF
```