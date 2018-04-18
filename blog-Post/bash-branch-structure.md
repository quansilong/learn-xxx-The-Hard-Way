---
title: Bash脚本编程——分支结构
date: 2018-04-15 17:16:26
tags: 
- Linux
- Shell
- bash
- 分支结构
categories:
- Liunx运维
- Bash编程
---

### Bash条件测试

#### 条件测试种类

##### 整数测试（双目操作符）

符号 | 数学符号 |含义
---  |---|---
-eq  | = | 相等测试
-ne  | ≠ | 不等测试
-gt  | > | 大于测试
-ge  | ≥ | 大于等于
-lt  | < | 小于测试
-le  | ≤ | 小于等于测试

##### 字符串测试（双目单目都有）

符号|含义
--- |---
==  | 判断两个字符串是否相等
!=  | 判断两个字符串是否相等
<  | 按照字符ASCII数字从前向后比较，数值大的大
\>  |
-n  | 判断字符串是不是为空串
-z  | 判断字符串是不是为空串

##### 文件测试（单目操作符）

符号|含义
--- |---
-e $FILENAME | 是否存在
-f $FILENAME | 是否是文件
-d $FILENAME | 是不是目录
-r $FILENAME | 有没有读权限
-w $FILENAME | 有没有写权限
-x $FILENAME | 有没有执行权限

#### 条件测试表达式

```sh
[ expression ]

[[ expression ]]

test expression  # test 是一个Bash命令
```

#### 算术运算的实现方式

```sh
let $A+$B

$[ $A+$B ]

$(( $A+$B ))

expr ` $A + $B `   	# 注：表达式中各操作数及运算符之间要有空格
                        # 而且要使用命令引用
```


### 分支结构（if语句）

#### 单分支的if语句

```sh
if 条件判断表达式; then
  expression1
  expression2
  ...
fi
```

#### 双分支的if语句

```sh
if 条件判断表达式; then
  expression1
  ...
else
  expression2
  ...
fi
```

#### 多分支的if语句

```bash
if 条件判断表达式1; then
  expression1
  ...
elif 条件判断表达式2; then
  expression2
  ...
  
... ...

elif 条件判断表达式4; then
  expression4
  ...
else
  expression5
  ...
fi
```

### 实例练习

#### 给定一个用户：如果其UID为0，就显示此为管理员；否则，就显示其为普通用户；

```bash
#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

USER_UID=$(id -u $1)  # $1为脚本所带的第一个参数，类似的$2,$3...

if [ $USER_UID -eq 0 ]; then
  echo "This is administration."
else
  echo "This is a commen user."
fi
```

#### 判断系统上是否有用户的默认shell为bash；如果有，就显示有多少个；否则，就显示没有这类用户；

```sh
#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

BASH_USER_NUMBER=$( grep "bash$" /etc/passwd | wc -l )
if [ $? -eq 0 ]; then  # $？为其前一行命令的执行状态返回值（ 0=True, 1...=False ）
  echo "There are $BASH_USER_NUMBER user(s) which use(s) bash."
else
  echo "There aren't any users which use bash."
fi

#	命令执行结果 ≠ 命令执行状态
#		1.  A=`ls`	 # 引用执行结果
#		2.  ls; A=$? # 引用执行状态

```

#### 给定一个文件，判断这个文件中是否有空白行；如果有，则显示其空白行数；否则，显示没有空白行。

```sh
#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

BLANK_LINE_NUMBER=$( grep "^$" $1 | wc -l )
if [ $BLANK_LINE_NUMBER -ne 0 ]; then
  echo "There are $BLANK_LINE_NUMBER blank line(s)."
else
  echo "There aren't any blank lines."
fi
```

#### 判断给定用户UID与GID是否一样。如果一样，就显示“good guy”；否则，就显示“bad guy”。

```sh
#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

USER_UID=`id -u $1`
GROUP_ID=`id -g $1`
if [ $USER_UID -eq $GROUP_ID ]; then
  echo "good guy"
else
  echo "bad guy"
fi
```

#### (不使用id命令)判断给定用户UID与GID是否一样。如果一样，就显示“good guy”；否则，就显示“bad guy”。

```sh
#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

USER_UID=`grep "^$1:" /etc/passwd | cut -d: -f3`
GROUP_ID=`grep "^$1:" /etc/passwd | cut -d: -f4`
if [ $USER_UID -eq $GROUP_ID ]; then
  echo "good guy"
else
  echo "bad guy"
fi

#	cut命令：字符串剪切
#		-d ：指定剪切的定位字符
#		-f ：指定剪切的字段数

```

#### 如果是一个普通文件，就显示之；如果是一个目录，亦显示之；否则，此为无法识别之文件；

```sh
#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

if [ ! -e $1 ]; then
  echo "Can't dentified."
elif [ -f $1 ]; then 
  echo "$1 is a file."
elif [ -d $1 ]; then 
  echo "$1 is a directory."
else
  echo "Can't dentified."
fi
```


