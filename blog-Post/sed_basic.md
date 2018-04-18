---
title: 流编辑器 sed 的使用（基础篇）
date: 2018-04-17 19:58:44
tags: 
- Linux
- Shell
- bash
- sed
categories:
- Liunx运维
- Bash编程
---

### 命令简介

#### sed特性
> 1. 流编辑器（Stream EDiter）
> 2. 行编辑器

#### sed工作模式
> 1. 每次读取指定文件中和Pattern相匹配的行到内存（模式空间）中；
> 2. 而后根据指定的命令对模式空间的文本进行编辑；
> 3. 最后输出整个模式空间中的内容。

### 用法详解

#### 命令格式
```sh
sed [options] 'AddressCommand' FILENAME
```
  



