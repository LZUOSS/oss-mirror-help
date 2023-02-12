---
category: help
layout: help
mirrorid: debian
---

Debian 镜像使用帮助
===================

Debian 的软件源配置文件是
`/etc/apt/sources.list`。将系统自带的该文件做个备份，将该文件替换为下面内容，即可使用
{{ site.org.nameUpper }} 的软件源镜像。

如果遇到无法拉取 https 源的情况，请先使用 http 源并安装：

```
$ sudo apt install apt-transport-https ca-certificates
```

再使用 {{ site.org.nameUpper }} 的软件源镜像。

### 配置文件清单

<!-- tabs:start -->

#### **sid**

```shell
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://{{ site.hostname }}/debian/ sid main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ sid main contrib non-free
```

#### **testing**

```shell
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://{{ site.hostname }}/debian/ testing main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ testing main contrib non-free
deb https://{{ site.hostname }}/debian/ testing-updates main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ testing-updates main contrib non-free

deb https://{{ site.hostname }}/debian/ testing-backports main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ testing-backports main contrib non-free

deb https://{{ site.hostname }}/debian-security testing-security main contrib non-free
# deb-src https://{{ site.hostname }}/debian-security testing-security main contrib non-free
```

#### **bullseye**

```shell
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://{{ site.hostname }}/debian/ bullseye main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ bullseye main contrib non-free
deb https://{{ site.hostname }}/debian/ bullseye-updates main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ bullseye-updates main contrib non-free

deb https://{{ site.hostname }}/debian/ bullseye-backports main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ bullseye-backports main contrib non-free

deb https://{{ site.hostname }}/debian-security bullseye-security main contrib non-free
# deb-src https://{{ site.hostname }}/debian-security bullseye-security main contrib non-free
```

#### **buster**

```shell
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://{{ site.hostname }}/debian/ buster main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ buster main contrib non-free
deb https://{{ site.hostname }}/debian/ buster-updates main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ buster-updates main contrib non-free

deb https://{{ site.hostname }}/debian/ buster-backports main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ buster-backports main contrib non-free

deb https://{{ site.hostname }}/debian-security buster/updates main contrib non-free
# deb-src https://{{ site.hostname }}/debian-security buster/updates main contrib non-free
```

#### **stretch**

```shell
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://{{ site.hostname }}/debian/ stretch main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ stretch main contrib non-free
deb https://{{ site.hostname }}/debian/ stretch-updates main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ stretch-updates main contrib non-free

deb https://{{ site.hostname }}/debian/ stretch-backports main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ stretch-backports main contrib non-free

deb https://{{ site.hostname }}/debian-security stretch/updates main contrib non-free
# deb-src https://{{ site.hostname }}/debian-security stretch/updates main contrib non-free
```

#### **jessie**

```shell
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://{{ site.hostname }}/debian/ jessie main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ jessie main contrib non-free
deb https://{{ site.hostname }}/debian/ jessie-updates main contrib non-free
# deb-src https://{{ site.hostname }}/debian/ jessie-updates main contrib non-free

deb https://{{ site.hostname }}/debian-security jessie/updates main contrib non-free
# deb-src https://{{ site.hostname }}/debian-security jessie/updates main contrib non-free
```

<!-- tabs:end -->