# -*- coding:utf-8 -*-
#@Time : 2021/9/10 17:30
#@Author: zxf_要努力
#@File : 网易2.py

#输出最长连续1的长度
import sys

def get_max_len(s,k):
    #滑动窗口
    list_number = list(map(int,list(s)))
    n = len(list_number)
    left = lsum = rsum = 0
    ans = 0
    for right in range(n):
        rsum += 1 - list_number[right]
        while lsum<rsum-k:
            lsum+=1-list_number[left]
            left+=1
        ans = max(ans,right-left+1)
    return ans
if __name__ == "__main__":
    # 读取第一行的n
    str_, k = sys.stdin.readline().strip().split()
    # str_ = "111000111110"
    # k = 2
    res = get_max_len(str_,k)
    print(res)