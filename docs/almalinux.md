---
category: help
layout: help
mirrorid: almalinux
---

# AlmaLinux 镜像使用帮助

> AlmaLinux OS is an open-source, community-driven Linux operating system that fills the gap left by the discontinuation of the CentOS Linux stable release. AlmaLinux OS is an Enterprise Linux distro, binary compatible with RHEL®, and guided and built by the community.

> [!tip] 本镜像站不同步 Sources 和 Debug-info。

AlmaLinux 使用 yum/dnf 包管理器下载软件包，可通过以下命令设置 {{ site.org.nameUpper }} 的镜像源。

> [!tip] 命令在 AlmaLinux 8.9/9.3 上测试成功，在其他版本上可能会有不同。

```bash
sed -e 's|^mirrorlist=|#mirrorlist=|g' \
    -e 's|^#\s*baseurl=https://repo.almalinux.org/almalinux|baseurl=https://{{ site.hostname }}/almalinux|g' \
    -i.bak \
    /etc/yum.repos.d/almalinux*.repo
```

