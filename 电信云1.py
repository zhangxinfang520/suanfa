# -*- coding:utf-8 -*-
#@Time : 2021/9/11 14:25
#@Author: zxf_要努力
#@File : 电信云1.py

#最长子串

#滑动窗口

import sys

def get_len_str(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    n = len(s)
    rk,ans= -1,0
    occ = set()
    for i in range(0,n):
        if i!= 0:
            occ.remove(s[i-1])
        while rk+1<n and s[rk+1] not in occ:
            occ.add(s[rk+1])
            rk +=1
        ans = max(ans,len(occ))
    return ans


if __name__ == "__main__":
    # 读取第一行的n
    s = sys.stdin.readline().strip()
    print(get_len_str(s))