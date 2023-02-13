---
category: help
layout: help
mirrorid: elrepo
---

# ELRepo 镜像使用帮助

> ELRepo is an RPM repository for Enterprise Linux packages. 

## 配置 ELRepo

首先按照[官网的安装说明](https://elrepo.org/tiki/tiki-index.php)进行配置：

```bash
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
```

接着，按照你的系统版本，执行下列命令: 

<!-- tabs:start -->

### **RHEL-8 / CentOS-8**

```bash
yum install https://www.elrepo.org/elrepo-release-8.el8.elrepo.noarch.rpm
```

### **RHEL-7 / SL-7 / CentOS-7**

```bash
yum install https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm
```

### **RHEL-6 / SL-6 / CentOS-6**

```bash
yum install https://www.elrepo.org/elrepo-release-6.el6.elrepo.noarch.rpm
```

<!-- tabs:end -->

## 更换镜像源

建议先备份 `/etc/yum.repos.d/elrepo.repo` ：

```bash
sudo cp /etc/yum.repos.d/elrepo.repo /etc/yum.repos.d/elrepo.repo.bak
```

然后编辑 /etc/yum.repos.d/elrepo.repo 文件，在 `mirrorlist=` 开头的行前面加 `#` 注释掉；并将 `elrepo.org/linux` 替换为 `{{ site.hostname }}/elrepo`。

最后，更新软件包缓存

```bash
sudo yum makecache
```
