# PyPI 镜像使用帮助

## 临时使用
```bash
pip install -i https://mirror.lzu.edu.cn/pypi/web/simple package-to-install
```
## 设为默认
```bash
python3 -m pip install -i https://mirror.lzu.edu.cn/pypi/web/simple --upgrade pip # 使用本镜像站来升级 pip
```
```bash
pip config set global.index-url https://mirror.lzu.edu.cn/pypi/web/simple
```