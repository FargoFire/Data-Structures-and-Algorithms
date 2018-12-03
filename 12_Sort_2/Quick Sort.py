# -*- coding:utf-8 -*-

"""
    Date: 2018/11/17
    By Fargo
    快速排序：如果要排序数组中下标从 p 到 r 之间的一组数据，我们选择p 到 r 之间的任意一个数据作为 pivot（分区点）。

    快速排序算法虽然最坏情况下的时间复杂度是 O(n2)，但是平均情况下时间复杂度都是 O(nlogn)。不仅如此，
    快速排序时间复杂度退化到 O(n2) 的概率非常小，我们可以通过合理地选择 pivot 来避免这种情况

"""


# 快速排序，a 是数组，n 表示数组的大小
def Quick_sort(a):
    n = len(a)
    _quick_sort_c(a, 0 ,n-1)

# 快速排序递归函数，p,r 为下标
def _quick_sort_c(a, p , r ):
    if p >= r: return

    q = _partition(a, p, r)  # 获取分区点 a[q] 是最后一项
    _quick_sort_c(a, p, q-1)
    _quick_sort_c(a, q+1 , r)


def _partition(a, p, r):
    pivot = a[r]
    i = p
    for j in range(p,r):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i +=1
    a[i], a[r] = a[r], a[i]
    return i

if __name__ == "__main__":
    a1 = [4, 2, 6, 3, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    Quick_sort(a1)
    print(a1)




















