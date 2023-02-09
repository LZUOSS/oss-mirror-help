---
category: help
layout: help
mirrorid: alpine
---

Alpine 镜像使用帮助
===================

> Alpine Linux is a security-oriented, lightweight Linux distribution based on musl libc and busybox.

Alpine Linux 是一个面向安全，轻量级的基于musl libc与busybox项目的Linux发行版。

在终端输入以下命令以替换{{ site.org.nameUpper }}镜像源：
```
sed -i 's/dl-cdn.alpinelinux.org/{{ site.hostname }}/g' /etc/apk/repositories
```
