---
category: help
layout: help
mirrorid: anaconda
---

# Anaconda 镜像使用帮助

> Anaconda offers the easiest way to perform Python/R data science and machine learning on a single machine.

Anaconda 是一个用于科学计算的 Python 发行版，支持 Linux, Mac, Windows, 包含了众多流行的科学计算、数据分析的 Python 包。

Anaconda 安装包可以到 https://{{ site.hostname }}/anaconda/archive/ 下载。

兰州大学开源社区镜像站还提供了 `Anaconda` 仓库与第三方源（`conda-forge`、`msys2`、`pytorch`等）的镜像，各系统都可以通过修改用户目录下的 `.condarc` 文件。Windows 用户无法直接创建名为 `.condarc` 的文件，可先执行 `conda config --set show_channel_urls yes` 生成该文件之后再修改。

> [!tip] 由于更新过快难以同步，我们不同步 `pytorch-nightly`, `pytorch-nightly-cpu`, `ignite-nightly` 这三个包。

```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://{{ site.hostname }}/anaconda/pkgs/main
  - https://{{ site.hostname }}/anaconda/pkgs/r
  - https://{{ site.hostname }}/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://{{ site.hostname }}/anaconda/cloud
  msys2: https://{{ site.hostname }}/anaconda/cloud
  bioconda: https://{{ site.hostname }}/anaconda/cloud
  menpo: https://{{ site.hostname }}/anaconda/cloud
  pytorch: https://{{ site.hostname }}/anaconda/cloud
  pytorch-lts: https://{{ site.hostname }}/anaconda/cloud
  simpleitk: https://{{ site.hostname }}/anaconda/cloud
```

即可添加 Anaconda Python 免费仓库。

运行 `conda clean -i` 清除索引缓存，保证用的是镜像站提供的索引。

运行 `conda create -n myenv numpy` 测试一下吧。

## Miniconda 镜像使用帮助

`Miniconda` 是一个 `Anaconda` 的轻量级替代，默认只包含了 `python` 和 `conda`，但是可以通过 `pip` 和 `conda` 来安装所需要的包。

`Miniconda` 安装包可以到 https://{{ site.hostname }}/anaconda/miniconda/ 下载。