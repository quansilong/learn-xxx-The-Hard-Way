# 蒙特卡洛计算pi
#     https://blog.csdn.net/Daniel960601/article/details/79121055
from random import random
from math import sqrt
from time import process_time
DARTS = 12000
hits = 0
process_time()
for i in range(1, DARTS):
    x, y = random(), random();
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print('Pi的值是 %s' % pi)
print('程序的运行时间是 %-5.5ss' % process_time())