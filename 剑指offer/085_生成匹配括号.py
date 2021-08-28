# -*- coding:utf-8 -*-
#@Time : 2021/8/26 21:15
#@Author: zxf_要努力
#@File : 085生成匹配括号.py
'''
正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：
输入：n = 1
输出：["()"]
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(back_str, left, right):
            if left== n and right== n:
                res.append(back_str)
                return
            if left < n:
                dfs(back_str + "(", left+1, right)
            if left > right:
                dfs(back_str + ")", left, right+1)
        dfs("",0,0)
        return res

    def generateParenthesis1(self, n: int) -> List[str]:
        res = []

        def dfs(back_str, idx,left,right):
            if left > n or right > left:return
            if idx == 2*n:
                res.append(back_str)
                return
            dfs(back_str+"(", idx+1,left+1,right)
            dfs(back_str+")", idx+1,left,right+1)

        dfs("", 0,0,0)
        return res
if __name__ == '__main__':
    print(Solution().generateParenthesis1(4))




