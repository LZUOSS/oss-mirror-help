---
layout: help
category: help
mirrorid: epel
---

## EPEL 镜像使用帮助

EPEL(Extra Packages for Enterprise Linux)是由Fedora Special Interest Group维护的Enterprise Linux（RHEL、CentOS）中经
常用到的包。


下面以CentOS 7为例讲解如何使用本镜像站的epel镜像。CentOS 8同样可用该方法。

首先从CentOS Extras这个源（[本镜像站](https://{{ site.hostname }}/help/centos)也有镜像）里安装epel-release：

```
yum install epel-release
```

<!-- 当前{{ site.org.nameLower }}已经在epel的官方镜像列表里，所以不需要其他配置，mirrorlist机制就能让你的服务器就近使用{{ site.org.nameLower }}的镜像。-->
修改`/etc/yum.repos.d/epel.repo`，将`mirrorlist`和`metalink`开头的行注释掉。

接下来，取消注释这个文件里`baseurl`开头的行，并将其中的`http://download.fedoraproject.org/pub`替换成`https://{{ site.hostname }}`。

可以用如下命令自动替换：

```
sed -e 's!^metalink=!#metalink=!g' \
    -e 's!^#baseurl=!baseurl=!g' \
    -e 's!//download\.fedoraproject\.org/pub!//{{ site.hostname }}!g' \
    -e 's!//download\.example/pub!//{{ site.hostname }}!g' \
    -e 's!http://mirrors!https://mirrors!g' \
    -i /etc/yum.repos.d/epel*.repo
```

修改结果如下：（仅供参考，不同版本可能不同）

```
[epel]
name=Extra Packages for Enterprise Linux 7 - $basearch
baseurl=https://{{ site.hostname }}/epel/7/$basearch
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=$basearch
failovermethod=priority
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

[epel-debuginfo]
name=Extra Packages for Enterprise Linux 7 - $basearch - Debug
baseurl=https://{{ site.hostname }}/epel/7/$basearch/debug
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-debug-7&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1

[epel-source]
name=Extra Packages for Enterprise Linux 7 - $basearch - Source
baseurl=https://{{ site.hostname }}/epel/7/SRPMS
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-source-7&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1
```

运行 `yum update` 测试一下吧。
