#  -*- coding: utf-8 -*-
"""
   Date: 2018/11/22
   By Fargo
   二分查找
"""

def Binary_search(x, B_S):
    n = len(B_S)
    value = x
    return _binary_search(B_S, 0, n-1, value)

def _binary_search(B_S, low, high, value):

    while low<=high:
        mid = low + (high-low)//2
        if B_S[mid] == value:
            return mid
        elif B_S[mid] < value:
            low = mid +1
        else:
            high = mid -1

    return -1


# def Bucket_sort(A):
#     n = len(A)
#     m = 50         # 桶数
#     buckets = [ [] for _ in range(m)]   # m 个空桶
#
#     for a in A :
#         k = a // 200
#         buckets[k].append(a)
#
#     B = []
#     for b in buckets:
#         B.extend(insertion_sort(b))
#     return B
#
# def insertion_sort(A):
#     n = len(A)
#     if n <=1 : return
#     B = []
#     for a in A :
#         i = len(B)
#         while i > 0 and B[i-1] >a :
#             i = i-1
#         B.insert(i,a)
#     return B

if __name__ == "__main__":
    import numpy as np
    import time

    start = time.clock()
    # A = np.random.randint(10000,size=2000)
    # B = Bucket_sort(A)
    B_S = [1,3,4,7,9,22,26,33,39,44,47,55,54,61,64,66,72,77,81,88,99,103,107]
    search_x = 88
    c = Binary_search(search_x, B_S)
    print(c)