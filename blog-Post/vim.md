---
title: VIM 编辑器
date: 2018-04-23 12:00:56
tags: 
- Linux
- Shell
- vi
- vim
categories:
- Liunx运维
- 系统管理
---

<font  size=4 face="黑体">更新日志</font> 

> 2018-04-21: 创建
  
---

### 简介

> vi:  Visual Interface
  vim: VI Improved

#### 特性

> 1. 全屏编辑器
> 2. 模式化编辑器(不同模式下敲击键盘的意义不同)

#### 模式

<img src="http://p7b7this6.bkt.clouddn.com/18-4-21/72518673.jpg" width="330" height="220" />


### 用法详解

#### 打开文件

> 1. vim FILENAME
    打开文件，不存在就创建
> 2. vim +12 FILENAME
    打开文件，并定位到第12行
> 3. vim + FILENAME
    打开文件，并定位到最后一行
> 4. vim +\RegExp FILENAME
    打开文件，并定位到被RegExp第一次匹配到的行

#### 关闭文件

字符|意义
---|---
:q  |   直接退出
:wq |   保存后退出
:q! |   强制退出（不保存修改内容）
:w  |   保存
:w! |   强制保存（管理员权限）
:x  |   =:wq
ZZ  |   保存后退出

#### 移动光标（普通模式）






























