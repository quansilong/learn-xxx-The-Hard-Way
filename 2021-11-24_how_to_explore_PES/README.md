# 如何对势能面进行有效的探索？

理论上，量子化学计算之**结构优化**以及**过渡态搜索**。其本质均为，由初始构型$\vec{R_0}$，经一系列中间结构$\vec{R_i}$，到达目标结构【$\vec{R_{min}}$是结构优化；$\vec{R_{TS}}$是过渡态搜索】。故而，如何有效的探索势能面是理论模拟的核心所在！

- 多原子体系的自由度【$3N-6(/-5)$ 】



## 1 Grid-Based Search(网格搜索)

即对一个多原子的多个自由度里面的每一个自由度进行间隔取值，对形成的高维度网格进行遍历搜索。这是一种暴力破解的方法，其算法复杂度是$O(a^N)$，即指数增长级别。这种方案，几乎只适用于原子数在个位数的多原子体系。纯网格的方法显然不适用作为大自由度体系的搜索方法，但是在小自由度体系的搜索全面性是其他算法所不具备的。



## 2 Forces-Based Search

对于一个确定的结构(即，给定坐标$\vec{R_0}$)，通过单点能(SPE)计算，既可以获取力(即，$E$ 对坐标 $\vec{R_0}$ 的一阶偏导)。基于力可以做很多结构的改变，如<u>结构优化，也就是使用多元函数的一阶偏导求函数极值点</u>；而<u>MD也就是基于经典力学求其运动轨迹</u>。

### 2.1 Local Optimization(局部结构优化)



- #### 最速下降法

- #### 牛顿法

  牛顿法是一种应用广泛的数值优化算法。其基本思想是：利用迭代点 $x_i$ 处的一阶导数(梯度)和二阶导数(Hessian矩阵)对目标函数进行二次函数近似，然后把二次模型的极小点作为新的迭代点，并不断重复直至找到精度收敛的极小值。

  **算法过程**：对目标函数 $E=E(\vec{R})$ 在 $\vec{R_i}$ 处进行二阶泰勒展开，有
  $$
  \begin{align}
  E(\vec{R}) &= E(\vec{R_i}) + \vec{g_i}^T (\vec{R}-\vec{R_i}) + \frac{1}{2}(\vec{R}-\vec{R_i})^T \vec{H_0} (\vec{R}-\vec{R_i})  \\
  &= C + \vec{B}^T\vec{R} + \vec{R}^T\vec{A}\vec{R}
  
  \end{align}
  $$
  其中，$A=\frac{1}{2}\vec{H_i}$,    $B=\vec{g_i}^T-\vec{H_i} \vec{R}$,   $C=E(\vec{R_i})-\vec{g_i}^T \vec{R_i}+\frac{1}{2}\vec{R_i}^T \vec{H_0}\vec{R_i}$

  二次函数的极小点取 $x=-\frac{b}{2a}$，则每次**结构的变化**为 ==$  \vec{R}=\vec{R_i}-\vec{H_i}^{-1}\vec{g_i} $==

- #### Quasi-Newton(准牛顿)类方法

  准牛顿法则是使用近似的Hessian矩阵，而不直接计算Hessian矩阵，故称为准牛顿法。而Hessian矩阵的近似算法不同，也就有了不同的准牛顿算法，比较有名的有BFGS，LBFGS，GPmin等等

  **GPmin**是使用高斯过程(Gaussian Process, GP)来生成一个势能面的机器学习预测模型，并使用该模型加速BFGS算法的一种优化方法。值得注意的是，在进行GP训练的过程中，程序需要保留以往所有的单点计算结果，因此需要的内存量很大【内存占用量复杂度$O(n^2N^2)$，n步N原子体系】。

- #### MDmin(基于MD方法的最小化算法)

- #### FIRE

  参见[Structural Relaxation Made Simple](https://doi.org/10.1103/PhysRevLett.97.170201)
  
  

### 2.2 Molecular Dynamics(分子动力学)







## 3 Randomness-Based Search

### 3.1 Basic Metropolis MC

基本的Metropolis算法是用于 $NVT$ 系综统计采样的算法，其基本思想为：给体系坐标 $\vec{R}$ 一个随机移动 $d\vec{R}$ ，移动的接受概率为
$$
P_{acc}(o\rightarrow n) = min[1, exp(-\frac{U(n)-U(o)}{k_B T})]
$$
随机位移 $d\vec{R}$ 的生成决定BMMC的搜索效率，不适当的随机位移会浪费大量的算力在无用的高能结构上。

### 3.2 Off-Lattice KMC(aKMC by Henkelman)

动态的搜索过渡态，并记录事件表格。





## 4 Forces-Randomness-Mixing-Based Search

### 4.1 Stochastic Surface Walk(SSW)

SSW算法包含两个循环：外循环是Metropolis MC算法，内循环是一个爬坡的过程。具体算法如下：

1. 生成当前极小点 $\vec{R_i^m}$ 随机初始方向 $\vec{N_i^0}$，设置爬坡计数$n=1$和初始爬坡位置$\vec{R_t^0}= \vec{R_i^m}$；
2. 开始进行爬坡循环， 



















































