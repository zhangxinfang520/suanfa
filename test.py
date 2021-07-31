# import sys
# if __name__ == "__main__":
#     # 读取第一行的T 表示有T组数据
#     T = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(T):
#         # 读取n 表示长度
#         n = int(sys.stdin.readline().strip())
#         # 读取数组的值
#         nums = list(map(int, sys.stdin.readline().strip().split()))
#         #获取长度操作
#         dp = [0] * n
#         index = nums.index(max(nums))
#         if index == len(nums)-1:
#             print(index)
#         else:
#             for i in range(1,n):
#                 for j in range(0,i):
#                     if dp[j] == 1:
#                         continue
#                     if nums[i] > nums[j]:
#                         dp[j] = 1
#             print(sum(dp))

#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
#
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         n = values[0]
#         x_1, y_1, z_1, x_2, y_2 , z_2 = values[1:]
#         a = [x_2,y_2,z_2]
#         flag = a
#         def dp(x,y,z):
#             temp = [x,y,z]
#             temp.sort()
#
#             if temp == a:
#                 return True
#             if (x > n) or (y > n) or (z > n) or (x < 0) or (y < 0) or (z < 0) :
#                 return False
#             if dp( 2*y - x+ 1, 2*x-y-1,z) or dp(y,x,z) or dp(x,z,y) or dp(z,y,x)   :
#                 return True
#         b = [x_1,z_1,y_1]
#         b.sort()
#         if a == b :
#             print('Yes')
#         elif dp(x_1,y_1,z_1):
#             print('Yes')
#         else:
#             print('No')


# #coding=utf-8
# # # 本题为考试多行输入输出规范示例，无需提交，不计分。
# # import sys
# # if __name__ == "__main__":
# #     # 读取第一行的n
# #     n,m = sys.stdin.readline().strip().split()
# #     n,m = int(n), int(m)
# #     a_nums = list(map(int,sys.stdin.readline().strip().split()))
# #     b_nums = list(map(int,sys.stdin.readline().strip().split()))
# #
# #     def fx(x,sum_):
# #         sum_ += int(x)
# #         fla = 1
# #         for i in range(m):
# #             fla = int(fla *(b_nums[i] - x))
# #         sum_ += fla
# #         return sum_ - x
# #     dp = 0
# #     for coin in range(n):
# #         if fx(a_nums[coin],0) > 0:
# #             dp +=1
# #     print(dp)

import sys

if __name__ == "__main__":
    # 读取第一行的n
    n, m = sys.stdin.readline().strip().split()
    n, m = int(n), int(m)
    a_nums = list(map(int, sys.stdin.readline().strip().split()))
    b_nums = list(map(int, sys.stdin.readline().strip().split()))


    def fx(x, sum_):
        sum_ += int(x)
        fla = 1
        for i in range(m):
            fla *= (b_nums[i] - x)
        sum_ += fla
        return sum_ - x
    dp = 0
    memo = dict()
    for coin in a_nums:
        if coin in memo.keys():
            if memo[coin] > 0:
                dp += 1
        else:
            memo[coin] = fx(coin,0)
            if memo[coin] > 0:
                dp += 1
    print(dp)

