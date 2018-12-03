# -*- coding:utf-8 -*-

"""
    Date: 2018/11/16
    By Fargo
    冒泡排序
    原地排序，稳定排序，最好时间复杂度O(n)，最坏时间复杂度O(n2)，平均时间复杂度O(n2)

"""
import numpy as np
import time

start = time.clock()

def Bubble_sort(a):
    n = len(a)
    if n <= 1: return
    for i in range(0, n):
        flag = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True

        if not flag:
            break
    return a


# a = [24,5,1,44,2,78,5,2]
a = np.random.randint(100000, size=2000)
print(Bubble_sort(a))

end = time.clock()
print(end - start)