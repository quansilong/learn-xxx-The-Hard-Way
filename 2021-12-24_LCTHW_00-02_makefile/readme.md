C语言是一种比Python更底层的语言。正所谓“不推公式不可称之为理论、不写代码不可称之为计算”，因此，对这样一门可以写操作系统的编程语言，有必要进行学习。【其实，对科学计算领域，Fortran是更好的选择】

### 参考书籍

https://docs.kilvn.com/lcthw-zh/



### Ex-00  准备

安装必要的**编译器**是学习C的第一步。

`sudo apt-get install build-essential`

使用**文本编辑器**，而不要使用IDE。



### Ex-01  使用编辑器

```bash
$ make ex01
cc     ex01.c   -o ex01
ex01.c: In function ‘main’:
ex01.c:3:9: warning: implicit declaration of function ‘puts’ [-Wimplicit-function-declaration]
    3 |         puts("Hello world.");
      |         ^~~~
ex01.c:1:1: note: include ‘<stdio.h>’ or provide a declaration of ‘puts’
  +++ |+#include <stdio.h>
    1 | int main(int argc, char *argv[])
```

这是由于使用标准输入输出，需要包含头文件`stdio.h`



### Ex-02  使用make

输入`make ex01`之后，`make`会进行以下过程：

1. 文件`ex1`存在吗？
2. 没有。好的，有没有其他文件以`ex1`开头？
3. 有，叫做`ex1.c`。我知道如何构建`.c`文件吗？
4. 是的，我会运行命令`cc ex1.c -o ex1`来构建它。
5. 我将使用`cc`从`ex1.c`文件来为你构建`ex1`。

`CFLAGS=-Wall`可以显示所有的警告。

