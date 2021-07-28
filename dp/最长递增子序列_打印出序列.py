# -*- coding:utf-8 -*-
#@Time : 2021-07-28 10:19
#@Author: zxf_要努力
#@File : 最长递增子序列_打印出序列.py
import copy
class Solution:
    def LIS(self , arr ):
        n = len(arr)
        if n == 1:
            return arr
        result = list()
        for i in range(n):
            result.append([arr[i]])
        for i in range(1,n):
            for j in range(0,i):
                if arr[i] > arr[j]:
                    if (len(result[j]) + 1) >= len(result[i]) :
                        result[i] = list(set(result[j] + result[i]))
        if len(result) == 1:
            return result[0]
        dict_re = {}
        for i in range(len(result)):
            dict_re[i] = len(result[i])
        re = sorted(dict_re.items(),key=lambda x:-x[1])
        max_same_index = []
        max_length = re[0][1]
        for index,val in re:
            if val == max_length:
                max_same_index.append(index)
            else:
                break
        sum_re = float('inf')
        re_index = 0
        for index in max_same_index:
            if sum(result[index]) < sum_re:
                re_index = index
                sum_re = sum(result[index])
        return result[re_index]

    def get_len_DIL(self,arr):
        n = len(arr)
        if n == 0:
            return []

        dp = [1] * n
        for i in range(1,n):
            for j in range(0,i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)


nums = [1,8,9,3,2,4,9,44,55,3,9,9,10,4,5,6,1,2,3]
print(Solution().get_len_DIL(nums))
print(Solution().LIS(nums))