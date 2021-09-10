# -*- coding:utf-8 -*-
#@Time : 2021/9/2 19:16
#@Author: zxf_要努力
#@File : 福途.py

#编辑距离

# "abc","adc",5,3,2

# class Solution:
#     def minEditCost(self , str1 , str2 , ic , dc , rc ):
#         #超时
#         # if len(str2) == 0:
#         #     return len(str1) * rc
#         # if len(str1) == 0:
#         #     return len(str2) * ic
#         # def backtrack(i,j):
#         #     if i == -1 : return ic * (j+1)
#         #     if j == -1 : return dc * (i+1)
#         #     if str1[i] == str2[j]:
#         #         return backtrack(i-1, j-1)
#         #     res = min( backtrack(i-1,j ) + dc,
#         #                backtrack(i,j-1) + ic,
#         #                backtrack(i-1,j-1) + rc
#         #               )
#         #     return res
#         # res = backtrack(len(str1)-1,len(str2)-1)
#         # return res
#
#         if len(str2) == 0:
#             return len(str1) * rc
#         if len(str1) == 0:
#             return len(str2) * ic
#         m,n = len(str1), len(str2)
#         #memo 二维数组保存状态
#         memo = [[0]*(n+1) for _ in range(m+1)]
#         #这个两个代表两种初始状态 对应上面 i=-1 j=-1
#         for i in range(1,n+1):
#             memo[0][i] = ic * i
#         for j in range(1,m+1):
#             memo[j][0] = dc * j
#         #
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 if str1[i-1] == str2[j-1]:
#                     memo[i][j] = memo[i-1][j-1]
#                 else:
#                     memo[i][j] = min(memo[i-1][j-1] + rc,memo[i-1][j]+dc,memo[i][j-1]+ic)
#
#         return memo[-1][-1]

class Solution:
    def solve(self , a):
        # write code here
        n = len(a)
        stack = []
        res = []
        #从左到右的最大值  [2,1,5,3,4] 转化为 [5,5,5,4,4]
        dp = [0] * n
        dp[n-1] = a[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(a[i],dp[i+1])
        for i in range(n):
            #栈顶元素判断 是否为这个数以后的最大值 如果是放到res 中
            while len(stack) > 0 and stack[-1] >= dp[i]:
                res.append(stack.pop())
            stack.append(a[i])
        #剩余的依次出栈
        while len(stack) > 0:
            res.append(stack.pop())
        return res

if __name__ == '__main__':
    nums = [2,1,4,7,4]
    print(Solution().solve(nums))