# -*- coding:utf-8 -*-
#@Time : 2021/9/18 12:52
#@Author: zxf_要努力
#@File : 1209_删除字符串中的所有相邻重复项II.py
'''
给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。
你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。
在执行完所有删除操作后，返回最终得到的字符串

输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。

输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释：
先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
再删除 "bbb"，得到 "dddaa"
最后删除 "ddd"，得到 "aa"

输入：s = "pbbcggttciiippooaais", k = 2
输出："ps"
'''

class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return  s
        res = []
        for c in s:
            if not res:
                res.append([c,1])
            else:
                if res[-1][0] == c:
                    if res[-1][1] + 1 < k:
                        res[-1][1] +=1
                    else:
                        res.pop()
                else:
                    res.append([c,1])
        ans = ""
        for s ,time in res:
            ans +=s * int(time)
        return ans

    #贼蠢的办法
    def removeDuplicates2(self, s: str, k: int) -> str:
        pre = s
        post = self.removeDuplicates1(pre,k)
        while len(pre) != len(post):
            pre = post
            post = self.removeDuplicates1(pre,k)
        return post

    def removeDuplicates1(self, s: str, k: int) -> str:
        n = len(s)
        if n == 1 or n == 0:
            return s
        s_list = list(s)
        stack = []
        while len(s_list):
            if not stack:
                stack.append(s_list.pop(0))
            else:
                if stack[-1] == s_list[0]:
                    temp = stack[-1]
                    if len(s_list) >= k-1:
                        flag = True
                        for i in range(k-1):
                            if s_list[i] != temp:
                                flag = False
                        if flag:
                            stack.pop()
                            s_list = s_list[k-1:]
                        else:
                            stack.append(s_list.pop(0))
                    else:
                        stack.append(s_list.pop(0))
                else:
                    stack.append(s_list.pop(0))
        return "".join(stack)



if __name__ == "__main__":
    s = "deeedbbcccbdaa"
    print(Solution().removeDuplicates(s, 3))
