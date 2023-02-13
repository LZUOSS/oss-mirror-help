---
category: help
layout: help
mirrorid: pypi
---

# PyPI 镜像使用帮助

<!-- tabs:start -->

## **临时使用**

```bash
pip install -i https://mirror.lzu.edu.cn/pypi/web/simple package-to-install
```

## **设为默认**

使用本镜像站来升级 pip：

```bash
python3 -m pip install -i https://mirror.lzu.edu.cn/pypi/web/simple --upgrade pip #
```

设置 pip 镜像源：

```bash
pip config set global.index-url https://mirror.lzu.edu.cn/pypi/web/simple
```

<!-- tabs:end -->