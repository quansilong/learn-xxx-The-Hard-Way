---
title: Linux服务——web（LAMP）
date: 2018-04-26 18:09:19
tags: 
- Linux
- LAMP
- Web
categories:
- Liunx运维
- 服务
---

<font  size=4 face="黑体">更新日志</font> 

> 2018-04-26: 创建
  
---


### 预安装环境
属性 |   服务端  | 客户端
---|---|---
系统    | CentOS 6.9  | Windows 10 Chrome
IP/MASK | 192.168.1.125/24 | 192.168.1.119/24
GATEWAY | 192.168.1.1      | 192.168.1.1
DNS     ||                   59.49.49.49
#### 配置防火墙
```bash
vim /etc/sysconfig/iptables
# 添加以下内容到22端口之后
-A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT

# 重启防火墙
/etc/init.d/iptables restart  
#service iptables restart
```
#### 关闭SELinux
```bash
vi /etc/selinux/config

#SELINUX=enforcing #注释掉
#SELINUXTYPE=targeted #注释掉
SELINUX=disabled #增加

setenforce 0 # 或者重启
```

### Apache
```bash
# 安装
yum -y install httpd
# 开机自启动httpd
chkconfig httpd on
# 开启服务httpd
/etc/init.d/httpd start #或者 service httpd start

# 安装一些Apache扩展
yum -y install httpd-manual mod_ssl mod_perl mod_auth_mysql
```
> 测试方法
  Windows主机浏览器输入 http://192.168.1.125


### MySQL
```bash
# 安装
# mysql         客户端
# mysql-server  服务端
# mysql-devel   开发库
yum -y install mysql mysql-server mysql-devel
# 开机自启动mysqld
chkconfig mysqld on
# 开启mysqld服务
/etc/init.d/mysqld start #或者 service mysqld start
# 进行一些安全性配置
/usr/bin/mysql_secure_installation
```
> 测试方法` netstat -tulpn | grep -i mysql`

### PHP
```bash
# 安装
yum -y install php php-mysql
# 安装一些常用PHP扩展
yum search php
yum -y install gd php-gd gd-devel php-xml php-common \
               php-mbstring php-ldap php-pear php-xmlrpc php-imap

# 重启httpd服务，这一步很重要
/etc/init.d/httpd restart #或者 service httpd restart
```
> 测试方法
```bash
cd /var/www/html
vim index.php

# 输入以下内容，保存退出
<?php
    phpinfo();
?>
```
> Windows主机浏览器输入 http://192.168.1.125

### PhpMyAdmin——MySQL的前端工具
```bash
# 下载
# 4.8.0.1 需要 php5.3+
wget https://files.phpmyadmin.net/phpMyAdmin/4.8.0.1/phpMyAdmin-4.8.0.1-all-languages.zip
wget https://files.phpmyadmin.net/phpMyAdmin/4.0.10.20/phpMyAdmin-4.0.10.20-all-languages.zip

# 安装
unzip phpMyAdmin-4.2.6-all-languages.zip
mv phpMyAdmin-4.2.6-all-languages /usr/local
ln -s /usr/local/phpMyAdmin-4.2.6-all-languages /var/www/html/phpmyadmin
cd /var/www/html/phpmyadmin

#  更改phpmyadmin配置文件
cp libraries/config.default.php config.inc.php
vi cnfig.inc.php
# 更改以下内容
$cfg['PmaAbsoluteUri'] = '';这里填写 phpMyAdmin 的访问网址。
$cfg['Servers'][$i]['host'] = 'localhost'; // MySQL hostname or IP address
$cfg['Servers'][$i]['port'] = ''; // MySQL port - leave blank for default port
$cfg['Servers'][$i]['user'] = 'root'; // 填写 MySQL 访问 phpMyAdmin 使用的 MySQL 用户名，默认为 root。
fg['Servers'][$i]['password'] = ''; // 填写对应上述 MySQL 用户名的密码。

# 重启httpd服务，这一步很重要
/etc/init.d/httpd restart #或者 service httpd restart
```
> 测试方法
> Windows主机浏览器输入 http://192.168.1.125/phpmyadmin


### 一些报错
> [php扩展报错mcrypt](https://blog.csdn.net/baiquan17/article/details/53216175)




