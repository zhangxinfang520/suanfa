# -*- coding:utf-8 -*-
#@Time : 2021/9/8 9:02
#@Author: zxf_要努力
#@File : 进制反转.py
import sys

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

def get_sum(nums,index,mode="H"):
    '''

    @param nums:
    @param index:
    @param mode: H 代表是行 V代表是列
    @return:
    '''
    n,m = len(nums), len(nums[0])
    if mode == "H":
        if index == 0 or index == n-1:
            return [index, get_part_sum(nums)]
        else:
            return [index,abs(get_part_sum(nums[0:index+1]) - get_part_sum(nums[index+1:n]))]
    else:
        pass


def main(n,m):
    dp = [[0]*m for _ in n]
    temp = 1
    for i in range(n):
        for j in range(m):
            dp[i][j] = temp
            temp +=1

if __name__ == '__main__':
    n,m = list(map(int,sys.stdin.readline().split()))

