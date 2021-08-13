# -*- coding:utf-8 -*-
#@Time : 2021-08-13 15:34
#@Author: zxf_要努力
#@File : 14_剪绳子.py
'''
给你一根长度为 n 的绳子，
请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
用一个dp数组记录从0到n长度的绳子剪掉后的最大乘积，也就是dp[i]表示长度为i的绳子剪成m段后的最大乘积，初始化dp[2] = 1
我们先把绳子剪掉第一段（长度为j），如果只剪掉长度为1，对最后的乘积无任何增益，所以从长度为2开始剪
剪了第一段后，剩下(i - j)长度可以剪也可以不剪。如果不剪的话长度乘积即为j * (i - j)；
如果剪的话长度乘积即为j * dp[i - j]。取两者最大值max(j * (i - j), j * dp[i - j])
第一段长度j可以取的区间为[2,i)，对所有j不同的情况取最大值，因此最终dp[i]的转移方程为
dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
最后返回dp[n]即可

'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(2,i):
                dp[i] = max(dp[i],max(j*(i-j),j * dp[i-j]))
        return dp[n]

    def cuttingRope1(self, n: int) -> int:
        if n < 4:
            return n - 1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n

if __name__ == '__main__':
    print(Solution().cuttingRope(10))