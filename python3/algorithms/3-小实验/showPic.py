#!/bin/env python
# -*- coding:utf-8 -*-
#------------------------------------------------------------------------------
# Author: LiuGaoyong                                                          |
# E-mail: liugaoyong_88@163.com, liugaoyong88@gmail.com                       |
# Description:                                                                 
#                            
                             
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np

#png=read()


lena = mpimg.imread(r'/mnt/c/User/LiuGaoyong/Pictures/o9.jpg') 
lena.shape #(512, 512, 3)

plt.imshow(lena) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()




