---
title: Linux网络管理基础
date: 2018-04-24 18:09:19
tags: 
- Linux
- Network
categories:
- Liunx运维
- 网络管理
---

<font  size=4 face="黑体">更新日志</font> 

> 2018-04-25: 创建
  
---

### 网络协议

#### 网络四层模型

![](http://p7b7this6.bkt.clouddn.com/18-4-25/79196621.jpg)

#### 报文首部

![](http://p7b7this6.bkt.clouddn.com/18-4-25/38309777.jpg)
![](http://p7b7this6.bkt.clouddn.com/18-4-25/35269192.jpg)

#### TCP的三次握手和四次握手

![](http://p7b7this6.bkt.clouddn.com/18-4-25/52246500.jpg)


### 网络配置

#### 命令管理（==立即生效，重启网络后失效==）

##### ifconfig
##### ip(属于iptable2包)

#### 修改配置文件管理（==重启网络后生效==）

##### 网络配置文件
```sh
vim /etc/sysconfig/network
```

##### 网络接口配置文件
```sh
vim /etc/sysconfig/network-scripts/ifcfg-eth0
```

##### 路由配置文件
```sh
vim /etc/sysconfig/network-scripts/route-eth0
```

