# -*- coding:utf-8 -*-
#@Time : 2021/9/8 9:02
#@Author: zxf_要努力
#@File : 进制反转.py
import sys
#quick sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)




# def get_bin(n,k):
#     bin_ = lambda x : "" if x == 0 else bin_( x//k ) + str( x % k )
#     return bin_(n)
#
#
# def get_number(bin_list,k):
#     n = len(bin_list)
#     if n == 0:
#         return 0
#     j = 0
#     number = 0
#     for i in range(n-1,-1,-1):
#         number += int(bin_list[i])*k**j
#         j +=1
#     return number
# def main(n,k):
#     bin_str = get_bin(n,k)
#     bin_list = list(bin_str)
#     bin_list.reverse()
#     return get_number(bin_list,k)

def get_part_sum(nums):
    n = len(nums)
    total = 0
    for i  in range(n):
        total +=sum(nums[i])
    return total



def main(n,m):
    dp = [[0]*m for _ in n]
    temp = 1
    for i in range(n):
        for j in range(m):
            dp[i][j] = temp
            temp += 1

if __name__ == '__main__':
    n,m = list(map(int,sys.stdin.readline().split()))

