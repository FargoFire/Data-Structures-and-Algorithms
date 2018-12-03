# -*- coding:utf-8 -*-

"""
    Date: 2018/11/16
    By Fargo
    选择排序
    原地排序，不稳定排序，最好时间复杂度O(n2)，最坏时间复杂度O(n2)，平均时间复杂度O(n2)
"""

import numpy as np
import time

start = time.clock()
def Select_Sort(a):
    n = len(a)
    for i in range(0,n):
        min_num = i
        for j in range(i+1,n):
            if a[min_num] > a[j]:
                min_num = j
            a[min_num], a[i] = a[i], a[min_num]
    return a

a = np.random.randint(100000, size=2000)
print(Select_Sort(a))

end = time.clock()
print(end - start)


