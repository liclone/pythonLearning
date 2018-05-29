# -*- coding: utf-8 -*-
# 用马青公式求pi
# pi=16*arctan(1/5) - 4*arctan(1/239)
# 位数多了后时间较长
import time 


n = int(input("输入想计算圆周率的位数："))

time1 = time.time()
#多计算10位
m = n + 10
#计算到小数点后m位
b = 10**m
#求含4/5的首项
x1 = b*4//5
#求含1/239的首项
x2 = b//-239
#求第一大项
he = x1 + x2
#设置下面循环终点，共计算n项
n *= 2
j = 0
for i in range(3,n,2):
    j += 1
    if j % 1000 == 0:
        print(j)
    x1 //= -25
    x2 //= -57121
    x = (x1 + x2)//i
    he += x
pi = he*4
#舍掉后10位
pi //=10**10
pi = str(pi)
#print((pi)[0]+str('.')+(pi)[1:len(pi)])
time2 = time.time()
print("Done!")
print("计算共耗时：" + str(time2 - time1) + 's')

with open('pi.txt','w') as f:
    f.write(pi)
