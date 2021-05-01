# -*- coding:utf-8 -*-
#@Time : 2021-03-04 13:22
#@Author: zxf_要努力
#@File : 354.py
'''
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，
这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）
输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

出二维数组的一个排列，使得其中有最长的单调递增子序列（两个维度都递增）
定义 dp[i]dp[i] 表示以 ii 结尾的最长递增子序列的长度。对每个 ii 的位置，遍历 [0, i)[0,i)，
对两个维度同时判断是否是严格递增（不可相等）的，如果是的话，dp[i] = max(dp[i], dp[j] + 1)dp[i]=max(dp[i],dp[j]+1)


'''
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes = sorted(envelopes,key=lambda x:(x[0],-x[1]))
        N = len(envelopes)

        dp = [1]*N
        for i in range(N):
            for j in range(i):
                if envelopes[j][1] <envelopes[i][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return  max(dp)



envelopes =[[5,4],[6,4],[6,7],[2,3]]
a = Solution().maxEnvelopes(envelopes)
print(a)


# def maxEnvelopes(envelopes):
#     a = sorted(envelopes,key=lambda x:(-x[0],x[1]),reverse=False)
#     #a = sorted(envelopes)
#     print(a)
# envelopes = [[5,4],[6,4],[6,7],[6,5],[2,3]]
# maxEnvelopes(envelopes)