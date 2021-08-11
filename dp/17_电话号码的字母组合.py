# -*- coding:utf-8 -*-
# @Time : 2021-08-11 13:37
# @Author: zxf_要努力
# @File : 17_电话号码的字母组合.py
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
from typing import List

num_2_str = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
             7: "pqrs", 8: "tuv", 9: "wxyz"}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 0:
            return []

        if len(digits) == 1:
            digits = int(digits[0])
            return list(num_2_str[digits])
        else:
            def backtrack(str_):
                if len(str_) == 0:
                    return []
                if len(str_) == 1:
                    digits = int(str_[0])
                    return list(num_2_str[digits])
                n = len(str_)
                mid = n // 2
                left = n % 2
                str_1 = backtrack(str_[0:mid])
                str_2 = backtrack(str_[mid:2 * mid])
                res = self.meger_two_one(str_1, str_2)
                if left:
                    res = self.meger_two_one(res, list(num_2_str[int(str_[-1])]))
                return res

            return backtrack(digits)

    def meger_two_one(self, digits_str_1, digits_str_2):
        res = []
        for i in range(len(digits_str_1)):
            for j in range(len(digits_str_2)):
                res.append(digits_str_1[i] + digits_str_2[j])
        return res


if __name__ == '__main__':
    digits ='234'
    print(Solution().letterCombinations(digits))
    #print(Solution().meger_two_one('2', '3'))
