import sys


# def get_max_nums(target, nums):
#     # 动态规划求解
#     memo = dict()
#
#     def dp(total):
#         if total in memo:
#             return memo[total]
#         if total == 0:  # 刚好花完
#             return 0
#         if total < 0:
#             return -1
#         res = float('inf')
#         for num in nums:
#             if num != target:
#                 sub = dp(total - num)
#                 if sub == -1: continue
#             # 代表最少得
#             res = min(res, 1 + sub)
#         memo[total] = res if res != float('inf') else -1
#         return memo[total]
#
#     return dp(target)

def change_max_nums(target, nums):
    result = list()
    for _ in range(target + 1):
        result.append(target+1)
    result[0] = 0
    #遍历所有的取值
    for i in range(len(result)):
        #遍历物品的价值
        for num in nums:
            #无解剩余价值 小于单个物品价值
            if i < num: continue
            if num == target:continue
            result[i] = min(result[i],1+result[i-num])
    return -1 if result[target] == target+1 else result[target]


if __name__ == "__main__":
    # 读取第一行的n 猪的价值
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split(" ")))
    res = change_max_nums(n, nums)
    print(res)
