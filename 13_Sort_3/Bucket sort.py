# -*- coding:utf-8 -*-

"""
    Date: 2018/11/19
    By Fargo
    桶排序：核心思想是将要排序的数据分到几个有序的桶里，每个桶里的数据再把每个桶里的数据按照顺序依次取出，
    组成的序列就是有序的了。
    桶排序比较适合用在外部排序中.
    首先，要排序的数据需要很容易就能划分成 m 个桶，并且，桶与桶之间有着天然的大小顺序。
    这样每个桶内的数据都排序完之后，桶与桶之间的数据不需要再进行排序。
    其次，数据在各个桶之间的分布是比较均匀的。如果数据经过桶的划分之后，有些桶里的数据非常多，
    有些非常少，很不平均，那桶内数据排序的时间复杂度就不是常量级了。在极端情况下，如果数据都被
    划分到一个桶里，那就退化为 O(nlogn) 的排序算法.
    非原地排序，稳定排序，时间复杂度O(n*log(n/m)),当桶的个数 m 接近数据个数 n 时时间复杂度O(n)
"""
import numpy as np
import time

def Bucket_sort(A):
    n = len(A)
    m = 50         # 桶数
    buckets = [ [] for _ in range(m)]   # m 个空桶

    for a in A :
        k = a // 200
        buckets[k].append(a)

    B = []
    for b in buckets:
        B.extend(insertion_sort(b))
    return B

def insertion_sort(A):
    n = len(A)
    if n <=1 : return
    B = []
    for a in A :
        i = len(B)
        while i > 0 and B[i-1] >a :
            i = i-1
        B.insert(i,a)
    return B


if __name__ == "__main__":
    start = time.clock()

    A = np.random.randint(10000, size=2000)
    print(Bucket_sort(A))

    end = time.clock()
    print(end - start)


