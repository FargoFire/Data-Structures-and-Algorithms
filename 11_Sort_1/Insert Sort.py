# -*- coding:utf-8 -*-

"""
    Date: 2018/11/16
    By Fargo
    插入排序
    原地排序，稳定排序，最好时间复杂度O(n)，最坏时间复杂度O(n2)，平均时间复杂度O(n2)
"""
import numpy as np
import time

start = time.clock()
def Insert_Sort(a):
    n = len(a)
    if n <=1 : return
    for i in range(0,n):
        value = a[i]
        j = i -1
        for j in range(j,0,-1):
            if a[j] > value : a[j+1] = a[j]
            else : break
        a[j+1] = value
    return a

a = np.random.randint(100000, size=2000)
print(Insert_Sort(a))

end = time.clock()
print(end - start)















