---
title: Amber 14 单核版+并行版安装
date: 2017-05-19 18:09:19
tags: 
- Cal-Chem-Software
- Amber
categories:
- 计算化学软件安装
---

<font  size=4 face="黑体">更新日志</font> 

> 2017-02-19: 创建
> 2019-04-01：更新标题字号

---


# **需要的东西：** ##
 - 一些底层的函数库
 - Amber 14 
 - AmberTools 14
 - openMPI （安装并行版所需）
 - linux环境（例如：CentOS 6.8）


# **安装步骤：** 
## 1. 安装底层函数库
```
yum install libXt-devel libXext-devel libX11-devel \
            libICE-devel libSM-devel fftw.x86_64
```
## 2. 安装Amber单核版
- 解压Amber14和AmberTools14安装包`tar zxcf 文件名`
- 添加以下内容到 `.bashrc`文件
```
# Amber14 setup
export AMBERHOME="Amber所在的目录"
```
- 编译，终端下执行
```sh
cd $AMBERHOME
./configure gnu
make install
```

## 3. 安装 openMPI
- 解压openMPI安装包 `tar zxcf 文件名`
- 编译，终端输入
```sh
cd /home/当前用户名
mkdir openmpi_after_compile
cd "openMPI所在的目录"
./configure --prefix=/home/当前用户名/openmpi_after_compile
make install
```

- 添加以下内容到 `.bashrc`文件
```sh
# openMPI setup
export MPI_HOME=/home/当前用户名/openmpi_after_compile
export PATH=$PATH:$MPI_HOME/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MPI_HOME/lib
```

## 4. 安装Amber并行版
- 编译，终端输入
```sh
cd $AMBERHOME
make clean
./configure -mpi gnu
make install
```
- 添加以下内容到 `.bashrc`文件
```sh
# Amber14 setup
export AMBERHOME="Amber所在的目录"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$AMBERHOME/lib
export PATH=$PATH:$AMBERHOME/bin
export DO_PARARRLE="mpirun -np 8"
```

## 5. 对Amber运行情况进行测试（可选）
- 终端输入
```
cd $AMBERHOME/test
make
# 测试Amber单核版
./test_amber_serial.sh >&test_serial.log&
# 测试Amber并行版
./test_amber_clean.sh
./test_amber_parallel.sh >&test_parallel.log&

cd $AMBERHOME/AmberTools/test
# 测试AmberTools单核版
./test_at_serial.sh >&test_serial.log&
# 测试AmberTools并行版
./test_at_parallel.sh >&test_parallel.log&

```

- 查看生成的4个`.log`文件，获取Amber运行情况
