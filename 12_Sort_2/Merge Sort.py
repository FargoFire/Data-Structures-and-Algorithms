# -*- coding:utf-8 -*-

"""
    Date: 2018/11/17
    By Fargo
    归并排序：先把数组从中间分成前后两部分，然后对前后两部分分别排序，再将排好序的两部分合并在一起

    非原地排序，稳定排序，最好、最坏、平均时间复杂度O(nlogn), 空间复杂度O(n)

"""
import time
import numpy as np

def Merge_Sort(a):
    _merge_sort_between(a, 0 , len(a)-1)


# 递归调用函数
def _merge_sort_between(a, low, high):
    # 递归终止条件
    if low >= high: return
    # 取中间位置
    mid = low + (high - low) //2
    # 分治递归
    _merge_sort_between(a, low, mid)
    _merge_sort_between(a, mid+1, high)
    # 合并
    _merge(a, low, mid, high)


def _merge(a, low, mid, high):
    i, j= low, mid+1
    temp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            temp.append(a[i])
            i +=1
        else:
            temp.append(a[j])
            j +=1
    # 判断哪个子数组中有剩余的数据
    start = i if i <= mid else j
    end = mid if i <= mid else high
    # 将剩余的数据拷贝到临时数组 tmp
    temp.extend(a[start:end+1])
    # 将 tmp 中的数组拷贝回 原数组
    a[low: high+1] = temp


if __name__ == "__main__":
    a1 = [4, 2, 6, 3, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    start = time.clock()
    m = np.random.randint(100000, size=2000)
    Merge_Sort(m)
    print(m)
    # Merge_Sort(a1)
    # print(a1)
    # Merge_Sort(a2)
    # print(a2)
    # Merge_Sort(a3)
    # print(a3)
    # Merge_Sort(a4)
    # print(a4)
    end = time.clock()
    print(end - start)




