# -*- coding:utf-8 -*-
#@Time : 2021-07-02 23:11
#@Author: zxf_要努力
#@File : 172_阶乘后的0.py
'''
给定一个整数 n，返回 n! 结果尾数中零的数量。
两个数相乘结果末尾有 0，一定是因为两个数中有因子 2 和 5，因为 10 = 2 x 5。
主要取决于能分解出几个因子 5，因为每个偶数都能分解出因子 2，因子 2 肯定比因子 5 多得多。
我们假设 n = 125，来算一算 125! 的结果末尾有几个 0：
首先，125 / 5 = 25，这一步就是计算有多少个像 5，15，20，25 这些 5 的倍数，它们一定可以提供一个因子 5。
但是，这些足够吗？刚才说了，像 25，50，75 这些 25 的倍数，可以提供两个因子 5，那么我们再计算出 125!
 中有 125 / 25 = 5 个 25 的倍数，它们每人可以额外再提供一个因子 5。
够了吗？我们发现 125 = 5 x 5 x 5，像 125，250 这些 125 的倍数，可以提供 3 个因子 5，
那么我们还得再计算出 125! 中有 125 / 125 = 1 个 125 的倍数，它还可以额外再提供一个因子 5。
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        divisor = 5
        while divisor <= n:
            res += n // divisor
            divisor *=5
        return res


print(Solution().trailingZeroes(100))