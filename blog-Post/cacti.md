---
title: Linux监控——cacti
date: 2018-04-27 18:09:19
tags: 
- Linux
- cacti
categories:
- Liunx运维
- 系统监控
---

<font  size=4 face="黑体">更新日志</font> 

> 2018-04-27: 创建
  2018-04-28: 添加cacti安装
  
---

## cacti 的安装

### 预安装环境
属性 | 客户端 | 被监控端 | cacti服务器
---|---|---|---
系统    | Windows 10 Chrome| CentOS 6.9         | Apache虚拟主机
IP/MASK | 192.168.1.119/24 | 192.168.1.125/24  | 192.168.1.200/24 
GATEWAY | 192.168.1.1      | 192.168.1.1       | 192.168.1.1
DNS     | 59.49.49.49      |  59.49.49.49      |59.49.49.49         
> LAMP环境
> 防火墙配置
```bash
vim /etc/sysconfig/iptables
# 添加以下内容到22端口之后
-A INPUT -m state --state NEW -m tcp -p tcp --dport 3306 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 161 -j ACCEPT

# 重启防火墙
/etc/init.d/iptables restart  
#service iptables restart
```

### 安装rrdtool、net-snmp以及相关依赖包
```bash
yum install rrdtool net-snmp rrdtool-devel net-snmp-devel \
            net-snmp-utils net-snmp-python net-snmp-perl \ 
            lm_sensors-devel file-devel rpm-devel file intltool \
            libart_lgpl libart_lgpl-devel elfutils pango-devel* \ 
            cairo-devel* mysql-devel Mod_auth_mysql php-mysql \
            cairo dejavu-fonts-common.noarch \
            dejavu-lgc-sans-mono-fonts.noarch dejavu-sans-mono-fonts.noarch \
            fontpackages-filesystem.noarch libXft libXrender libthai pango \
            pixman perl-rrdtool net-snmp net-snmp-utils tcp_wrappers-devel
```

### 下载安装cacti
```bash
wget http://www.cacti.net/downloads/cacti-0.8.8f.tar.gz
tar zxvf cacti-0.8.8f.tar.gz
mv cacti-0.8.8f /usr/local
ln -s /usr/local/cacti-0.8.8f/ /var/www/html/cacti
```

### 配置cacti的MySQL数据库
```bash
# 输入密码进入MySQL控制台
mysql -u root -p 

# MySQL控制台操作
Create DATABASE IF NOT EXISTS cactidb default charset utf8 COLLATE utf8_general_ci; #创建数据库cactidb
insert into mysql.user(Host,User,Password) values('localhost','cactiuser',password('123456')); #创建数据库用户cactiuser 密码 123456
grant all on cactidb.* to 'cactiuser'@'%' identified by '123456' with grant option; #授权用户cactiuser对数据库cactidb完全访问
flush privileges; #刷新系统授权表，使设置生效
use cactidb
source /usr/local/nginx/html/cacti.sql #导入cacti数据库文件
exit; #退出MySQL控制台


vi /usr/local/nginx/html/include/config.php #配置数据库连接
$database_type = "mysql";
$database_default = "cactidb"; #数据库名称
$database_hostname = "localhost"; #主机名称，默认即可
$database_username = "cactiuser"; #数据库用户名
$database_password = "123456"; #数据库密码
$database_port = "3306"; #MySQL数据库默认连接端口
$database_ssl = false;
```

### 客户端浏览器配置cacti


### 配置计划任务

```bash
#安装计划任务软件包
yum install -y vixie-cron 
#设为开机启动
chkconfig crond on 

#设置每隔5分钟Cacti采集一次数据
crontab -e  
*/5 * * * * php   /usr/local/nginx/html/poller.php  &> /dev/null

#启动crond
service crond start 
#手动刷新数据
/usr/bin/php  /usr/local/nginx/html/poller.php
```




## 待添加





