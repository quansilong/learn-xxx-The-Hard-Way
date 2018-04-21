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

#### Address

> 1. StartLine,EndLine
    比如： 1,100 （第1行到第100行）$=最后一行

> 2. /RegExp/
    被正则表达式匹配的行

> 3. /RegExp1/,/RegExp2/
    从==第一次==被RE1匹配的行，到==第一次==被RE2匹配的行

> 4. LineNumber
    指定的行

> 5. StartLine, +N
    从StartLine开始，向后的N行

#### Command

字符|意义
---|---
d  |删除符合条件的行
p  |显示符合条件的行
a \STRING|在指定行==后面==追加新行，内容为STRING【\n可以用于换行】
i \STRING|在指定行==前面==追加新行，内容为STRING【\n可以用于换行】
r FIEL| 将指定文件的内容添加至符合条件的行处
w FILE| 将地址指定的范围内的行另存为到指定文件中
s/RegExp/STRING/x | 查找指定行中符合RegExp匹配的字符串并用STRING替换，默认仅替换每行中第一次被匹配的字符串。【x=修饰符：g=全局替换；i=忽略大小写】【可以使用后向引用\\\(\\),\1】【&=引用被RegExp匹配到的整个字符串】
s###,s@@@,s%%%...|=s///【大多数字符都可以用来分割】



### 用法练习

#### 删除/etc/grub.conf文件中行首的空白符；

```sh
sed 's/^[[:space:]]*//' /etc/grub.conf
```

#### 替换/etc/inittab文件中"id:3:initdefault:"一行中的数字为5；

```sh
sed 's/id:[[:digit:]]*:initdefault:/id:5:initdefault:/' /etc/inittab
```

#### 删除/etc/inittab文件中的空白行；

```sh
sed '/^$/d' /etc/inittab
```

#### 删除/etc/inittab文件中开头的#号; 

```sh
sed 's/^#//' /etc/inittab
```

#### 删除某文件中开头的#号及后面的空白字符，但要求#号后面必须有空白字符;

```sh
sed 's/^#[[:space:]]\{1,\}//' /etc/inittab
```

#### 删除某文件中以空白字符后面跟#类的行中的开头的空白字符及#

```sh
sed 's/^[[:space:]]\{1,\}#//' /etc/inittab
```













  



