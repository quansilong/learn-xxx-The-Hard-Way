---
title: GaussView 5 基于Linux的安装
date: 2017-05-18 18:09:19
tags: 
- Cal-Chem-Software
- GaussView
- Gaussian入门
categories:
- 计算化学软件安装
---

<font  size=4 face="黑体">更新日志</font> 

> 2017-02-18: 创建

---

## **需要的东西：** ##
- gv5安装包
- linux环境（例如：CentOS 6.8）

## **安装步骤：** ##
1. 解压安装包
```sh
tar -zxcf gv5.tar.gz
```
2. 把g09移动到某文件夹下（比如， /usr/local）
```sh
mv gv5 /usr/local
```
3. 将下列内容加到==本用户==的`.bashrc`文件尾部
```sh
# GaussView Setup
export GV_DIR=/usr/local/gv
export LIBPATH=/usr/local/gv
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/gv/lib
alias gv='/usr/local/gv/gview.exe'
```

----
##  注：关于如何启用其他用户使用gv5
- 重复上面的 3 步骤
