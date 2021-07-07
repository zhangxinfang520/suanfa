# -*- coding:utf-8 -*-
#@Time : 2021-07-05 20:28
#@Author: zxf_要努力
#@File : 372_超级次方.py
'''
你的任务是计算 a^b(a的b次方) 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

输入：a = 2, b = [3]
输出：8
输入：a = 2, b = [1,0]
输出：1024
现在 b 是一个数组，不能表示成整型，而且数组的特点是随机访问，删除最后一个元素比较高效。
b = [1,5,6,4]
a^b = a^4 x (a^[1,5,6])^10

另外一个技巧 (a * b) % k = (a % k)(b % k) % k

'''
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        base = 1337
        if not b:return 1
        temp = b.pop()
        #将原问题化简，缩小规模递归求解
        part1 = self.mypow(a,temp)
        part2 = self.mypow(self.superPow(a,b),10)

        return (part1 * part2) % base

    def mypow(self,a,k):
        #计算 a 的 k 次方然后与 base 求模的结果
        a %= 1337
        res = 1
        for _ in range(0,k):
            #这里有乘法，是潜在的溢出点
            res *= a
            #对乘法结果求模
            res %= 1337

        return res


print(Solution().superPow(2, [5,6,4,3]))
