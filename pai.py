#pai.py
from random import random
from math import sqrt
from time import perf_counter
date=100000
d=0.0
count=0
T=perf_counter()
for i in range(1,date+1):
    x,y=random(),random()
    d=sqrt(x**2+y**2)
    if(d<=1.0):
        count+=1
pai=4*(count/date)
print("pai的值是{}".format(pai))
print("所用的时间为:{:.5f}s".format(perf_counter()-T))