#!/bin/bash
# Get some information of this system.
# Author: LiuGaoyong (e-mail: liugaoyong_88@163.com)


cpunum=$(cat /proc/cpuinfo | grep processor | wc -l)  #获取CPU逻辑核心数
echo cpu num: $cpunum

tmem=$(free -h | sed -n '2p'| awk '{print $2}')       #获取总内存大小
echo memory total: $tmem 

umem=$(free -h | sed -n '2p'| awk '{print $4}')       #获取当前可用内存大小
echo memory free: $umem 

ds=$(df -h | sed -n 3p | awk '{print $1}')            #获取/挂载硬盘大小
echo disk size: $ds

sysbit=$(getconf LONG_BIT) #获取系统位数
echo syatem bit: $sysbit

process=$(ps aux | wc -l)  #当前系统运行进程数
echo process: $process

snum=$(rpm -qa | wc -l)    #当前系统安装软件包数量（ubuntu： dpkg -l）
echo software num: $snum

ip=$(ifconfig | grep 'inet addr:' | sed -n 1p | awk '{print $2}'| awk -F ':' '{print $2}') #获取当前系统ip
echo ip: $ip
