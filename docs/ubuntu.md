# Ubuntu 镜像使用帮助

## 地址

[Ubuntu](https://mirror.lzu.edu.cn/ubuntu/)

## 描述

Ubuntu 是一个基于 Debian 的 Linux 发行版，它以桌面用户为主要目标，但也可以用于服务器和嵌入式系统。Ubuntu 的官方网站是 [ubuntu.com](https://ubuntu.com/)。
!> 本镜像仅仅包含 i386 和 amd64 架构的软件包。

## 使用方法

### 手动替换

Ubuntu 的软件源地址位于 `/etc/apt/sources.list` 文件中，将其中的 `archive.ubuntu.com` 替换为 `mirror.lzu.edu.cn` 即可。

### 使用脚本

Ubuntu 的软件源地址位于 `/etc/apt/sources.list` 文件中，使用下面的脚本可以自动替换为兰州大学开源社区镜像站的地址。

```bash
sudo sed -i "s@http://.*archive.ubuntu.com@https://mirror.lzu.edu.cn@g" /etc/apt/sources.list
sudo sed -i "s@http://.*security.ubuntu.com@https://mirror.lzu.edu.cn@g" /etc/apt/sources.list
```

### 使用图形界面工具

当使用内建 Gnome 桌面时，可以使用图形界面工具 `Software & Updates` 进行配置。在 'Software & Updates' 中，选择 'Other Software' 选项卡，点击 'Add' 按钮，输入 `https://mirror.lzu.edu.cn/ubuntu` 作为软件源地址，点击 'Add Source' 按钮，即可添加兰州大学开源社区镜像站的 Ubuntu 软件源。或直接在下拉菜单中选择 '下载自' 选项卡，选择 '中国' 中 'mirror.lzu.edu.cn' 作为软件源地址。
