#  -*- coding: utf-8 -*-
"""
   Date: 2018/11/22
   By Fargo
   二分查找 变形1：有序数据集合中存在重复的数据，找到第一个值等于给定值的数据
            变形2：有序数据集合中存在重复的数据，找到最后一个值等于给定值的数据

"""

def Binary_search_1(value , B):# 找到第一个值等于给定值的数据
    n = len(B)
    low, high = 0, n-1
    while low <= high:
        mid = low + (high - low) //2
        if B[mid] > value:
            high = mid - 1
        elif B[mid] < value:
            low = mid + 1
        else:
            if B[mid-1] != value or mid == 0 : return mid
            else : high = mid-1
    return -1


def Binary_search_2(value , B):   # 找到最后一个值等于给定值的数据
    n = len(B)
    low, high = 0, n-1
    while low <= high:
        mid = low + (high - low) //2
        if B[mid] > value:
            high = mid - 1
        elif B[mid] < value:
            low = mid + 1
        else:
            if B[mid+1] != value or high == n-1 : return mid
            else : low = mid+1
    return -1

def Binary_search_3(value, B):      # 第一个大于等于给定值的元素
    n = len(B)
    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low)//2
        if B[mid] < value:
            low = mid +1
        else :             # B[mid] >= mid
            if B[mid-1] < value or mid ==0 : return mid
            else: high = mid -1
    return -1

def Binary_search_4(value, B):
    n = len(B)
    low, high = 0, n-1
    while low <= high:
        mid = low + (high - low) //2
        if B[mid] <= value:
            if B[mid+1] > value or mid == n-1 : return mid
            else: low = mid +1
        else:
            high = mid -1
    return -1


if __name__ == "__main__":
    B = [2,3,4,7,9,22,26,33,39,44,47,55,54,61,61,61,64,66,72,77,81,88,99,103,107]
    search_x1 = 61
    c = Binary_search_1(search_x1, B)
    print('查找第一个等于给定值的数',c , B[c] , B[c-1])

    search_x2 = 61
    d = Binary_search_2(search_x2, B)
    print('查找最后一个等于给定值的数',d, B[d], B[d+1])

    search_x3 = 1
    e = Binary_search_3(search_x3, B)
    print('查找第一个大于等于给定值的数',e, B[e], B[e-1])

    search_x4 = 98
    f = Binary_search_4(search_x4, B)
    print('查找最后一个小于等于给定值的数',f, B[f], B[f+1])





