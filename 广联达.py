# import math
# import sys
#
# while True:
#     n,m = sys.stdin.readline().strip().split()
#     sum_ = int(n)
#     if int(n) < 0 or int(m) < 0:
#         print(0)
#     res = []
#     for i in range(0,int(m)):
#         res.append(sum_)
#         sum_ = round(math.sqrt(sum_),2)
#
#     re = sum(res)
#     print(round(re,2))

import sys

def get_dict(nums):
    memo = dict()
    n = len(nums)
    for i in range(n):
        memo[i] = len(set(nums[i:]))
    return memo

def get_count(x,memo):
    return memo[x]


def get_laste_count(x,y,X,Y):

    def dp(i,j):
        if i == X and j == Y:
            return 0
        if i > X or j > Y :
            return float("inf")
        re = float("inf")
        re = min(re,dp(i+1,j+1)+1)
        re = min(re,dp(i*2,j*2)+1)
        return re
    return dp(x,y)


if __name__ == '__main__':
    # n,m = list(map(int,sys.stdin.readline().rstrip().split()))
    # nums = list(map(int,sys.stdin.readline().rstrip().split()))
    # memo = get_dict(nums)
    # for _ in range(m):
    #     x = int(sys.stdin.readline().rstrip())
    #     print(get_count(x-1,memo))
    print(get_laste_count(1,2,4,6))







