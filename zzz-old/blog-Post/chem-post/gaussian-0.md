---
title: Gaussian-000：第一次Gaussian计算
date: 2018-02-08 11:09:19
tags: 
- Gaussian入门
categories:
- Gaussian学习
---

<font  size=4 face="黑体">更新日志</font> 

> 2018-02-08: 创建
> 2019-04-01: 更新版面

---


# Gaussian 的输入文件（water.gjf）
> GaussView 使用[教程](https://www.baidu.com/s?wd=GaussView%20%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B&rsv_spt=1&rsv_iqid=0xa91889190003e46e&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=sitehao123&rsv_enter=1&rsv_n=2&rsv_sug3=1)
![](https://chem.liugaoyong.top/2018-02-08-gaussian-0/1.png)
# 输入文件实例剖析
> 如上图所示，四个空行隔开了以下 **四个部分**：
>
> 第一部分：Link部分。该部分可分为 **%行**和 **#行**两部分，其中 **%行**是对Gaussian程序的IO路径、调用系统资源等的规定；而 **#行**是对计算使用的化学模型（见下部分 **计算模型**），详见[使用说明书](https://www.baidu.com/s?wd=g09%20%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E%E4%B9%A6&rsv_spt=1&rsv_iqid=0xce519ed00005c3d7&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=sitehao123&rsv_enter=0&oq=g09%2520%25E4%25BD%25BF%25E7%2594%25A8%25E8%25AF%25B4%25E6%2598%258E%25E4%25B9%25A6&rsv_t=b5f7Sm7aKLp818iBSOkNaOHkUav6%2BKuVRyRjEvgG2xQUNzgF8chxoeDJrvjkNO2WUw&rsv_pq=eafaf8810004c4d3);
>
> 第二部分：对计算体系的文字描述，可以随意书写；
>
> 第三部分：对计算体系的笛卡尔坐标； 
>
> 第四部分：对计算体系的内坐标（**可省略**）。

# 计算模型（Model Chemistries）
> 关于 Model Chemistries 的描述如下：![](https://chem.liugaoyong.top/2018-02-08-gaussian-0/2.png)即，Gaussian的全部哲学就是：**理论模型的选择**应该既要适用于**分子体系的大小和类型**，也要考虑**计算资源的可用性**。
> 常见的模型如下图示：
> ![](https://chem.liugaoyong.top/2018-02-08-gaussian-0/3.png)


# Gaussian 的执行
> 本例子采用 B3LYP/6-31G* 计算：
> Linux 系统 `go9 < water.gjf &> water.log`
> Windows 系统类似


# Gaussian 的输出（water.out 或者 water.log）
> 以文本方式打开，尾行出现 Normal termination 字样则表示程序正常运行完毕
![](https://chem.liugaoyong.top/2018-02-08-gaussian-0/4.png)


# 尾语

计算机程序可以弥补人类数学计算能力的不足，但是**对现实问题的抽象建模**以及**对程序输出的分析总结**，仍然需要人脑的参与（这也是人类现在不会被计算机替代的结果）。

有关人工智能应用在化学问题的研究正在积极研究中，未来我们能否实现**提出问题即可得到答案**的超级懒人目标仍有待社会进一步的发展。

