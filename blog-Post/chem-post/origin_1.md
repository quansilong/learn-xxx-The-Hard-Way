---
title: Origin打开文件时出现错误的解决办法
date: 2018-05-29 18:09:19
tags: 
- Origin
- 科研绘图
categories:
- OriginFAQ
---

<font  size=5 face="黑体">更新日志</font> 

> 2018-05-29: 创建
> 2019-04-01：更新标题字号

  
---

# 问题描述：
> 打开以前保存过的.opj格式图形文件，提示“向程序发送命令时出现问题”


# 问题解决
> 1. 打开Origin
> 2. 打开 Windows菜单下的Script Window 脚本窗口。
> 3. 在脚本窗口里面输入引号内的代码：“doc -ddde 1”，回车后关闭Origin。如下图所示。
> 4. 用管理员身份，再次打开Origin软件，即解决，再双击打开.opj文件的时候不会再有错误提示了。

---

# 参考网址
[解决每次打开origin都会提醒“向程序发送命令时出现问题”](http://blog.sciencenet.cn/blog-357977-948525.html)
