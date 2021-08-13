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

# import sys
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n, m = sys.stdin.readline().strip().split()
#     n, m = int(n), int(m)
#     a_nums = list(map(int, sys.stdin.readline().strip().split()))
#     b_nums = list(map(int, sys.stdin.readline().strip().split()))
#
#
#     def fx(x, sum_):
#         sum_ += int(x)
#         fla = 1
#         for i in range(m):
#             fla *= (b_nums[i] - x)
#         sum_ += fla
#         return sum_ - x
#     dp = 0
#     memo = dict()
#     for coin in a_nums:
#         if coin in memo.keys():
#             if memo[coin] > 0:
#                 dp += 1
#         else:
#             memo[coin] = fx(coin,0)
#             if memo[coin] > 0:
#                 dp += 1
#     print(dp)
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# nums1 = set(nums1)
# nums2 = set(nums2)
#
# print(nums1.intersection(nums2))


class Solution:
    def Solve1(self , s ):
        # write code here
        if len(list(s)) == len(list(set(list(s)))) or len(s) == 1 or len(s) ==0:
            return ""
        res = ""
        list_str = list(s)
        n = len(list_str)
        for i in range(1,n):
            for j in range(i):
                if s[i] == s[j]:
                    res = res if len(res) > len(s[j:i+1]) else s[j:i+1]
        return res

    def Solve(self , s ):
        # write code here
        if len(list(s)) == len(list(set(list(s)))) or len(s) == 1 or len(s) ==0:
            return ""
        res = []
        list_str = list(s)
        n = len(list_str)
        rk = -1
        occ = list()
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.append(s[rk + 1])
                rk += 1
            if rk + 1 < n and s[rk + 1] == occ[0]:
                res = res if len(res) > len(occ) else occ + list(s[rk + 1])
        re = ""
        if len(res):
            for x in res:
                re +=str(x)
        return re


class Solution1:
    def largestNumber(self , nums ):
        if len(nums)==0:
            return 0
        nums.sort()
        nums1 = []
        nums2 = []
        zero_nums = 0
        n = len(nums)
        for i in range(n):
            if nums[i] >= 10 :
                nums2.append(nums[i])

            elif nums[i] < 10 and nums[i]!=0 :
                nums1.append(nums[i])
            else:
                zero_nums +=1
        s = ""
        nums2.sort(reverse=True)
        nums1.sort(reverse=True)
        for x in nums1+nums2:
            s += str(x)
        if zero_nums !=0:
            for x in range(zero_nums):
                s +="0"
        return s
S = [10,20,0,0,0]
print(Solution1().largestNumber(S))

# S = "banawawrghljanswa"
# print(Solution().Solve(S))




