# -*- coding:utf-8 -*-
#@Time : 2021/8/21 15:29
#@Author: zxf_要努力
#@File : 22_括号生成.py
'''
数字 n 代表生成括号的对数，请你设计一个函数，
用于能够生成所有可能的并且 有效的 括号组合。
有效括号组合需满足：左括号必须以正确的顺序闭合。

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
输入：n = 1
输出：["()"]
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        res = []

        def dp(A:List):
            if len(A) == 2 * n:
                if is_Valid(A):
                    res.append("".join(A))
            else:
                A.append("(")
                dp(A)
                A.pop()
                A.append(")")
                dp(A)
                A.pop()

        def is_Valid(A:List):
            bal = 0
            for c in A:
                if c == "(":
                    bal +=1
                else:
                    bal -=1
                if bal < 0: return False
            return bal==0
        dp([])
        return res
