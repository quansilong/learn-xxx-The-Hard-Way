---
title: Bash脚本编程——循环结构
date: 2018-04-21 10:00:56
tags: 
- Linux
- Shell
- bash
- 循环结构
categories:
- Liunx运维
- Bash编程
---

<font  size=4 face="黑体">更新日志</font> 

> 2018-04-21: 创建
  
---


### 循环结构
 
#### for语句

```sh
for I in 1 2 3 4 5 6 7 8 9; do
    exp1
    exp2
    ...
done
    #   I       循环变量
    #   1-9     列表
    #   do与for若不在同一行，则‘;’可省略
```


### 实例练习

#### 输出100以内所有能被3整除的正整数的和；

```bash
#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-21

for I in {1..100}; do
    let YUSHU=$I%3
    if [ $YUSHU -eq 0 ]; then
        echo " $I 可以被 3 整除。"
    fi
done


    # {1..100}  1-100的整数列表
    # seq [ 起始数字(默认1) [ 步长(默认1) ] ] 结束数字
    #   seq 100
    #   seq 1 100
    #   seq 1 2 100
```

#### 计算100以内所有奇数的和以及所有偶数的和；分别显示之；

```bash
#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-21

let SUM_QISHU=0
let SUM_OUSHU=0
for I in {1..100}; do
    let YUSHU=I%2
    if [ $YUSHU -eq 0 ]; then
        let SUM_OUSHU=$SUM_OUSHU+$I
    else
        let SUM_QISHU=$SUM_QISHU+$I
    fi
done
echo "1-100的奇数和为$SUM_QISHU，偶数和为$SUM_OUSHU"
```