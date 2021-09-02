# -*- coding:utf-8 -*-
class Solution:
    # s, patternattern都是字符串
    def match(self, s, pattern):
        # write code here
        m, n = len(s), len(pattern)
        if m ==0 or n==0:
            return False
        def matches(i, j):
            if i == 0:
                return False
            if pattern[j - 1] == ".":
                return True
            return s[i - 1] == pattern[j - 1]

        f = [[False] * (n + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if pattern[j - 1] == "*":
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

if __name__ == '__main__':
    s = "aaa"
    p = "ab*ac*a"
    print(Solution().match(s, p))