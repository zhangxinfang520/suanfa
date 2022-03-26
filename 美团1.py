# encoding: utf-8
"""
@author: zxf_要努力
@file: 美团1.py
@time: 2022/3/26 16:06
"""
import sys

res = 0

def get_max(n, result):
    result.sort()
    res = []
    def dp(track,idx):
        if len(track) > 0 and  sum(track) % 7 == 0:
           res.append(track[:])
           return
        if idx == n:
            return
        for i in range(idx,n):
            if idx > i and result[i-1] == result[i]:
                continue
            track.append(result[i])
            dp(track,i+1)
            track.pop()
    dp([],0)
    return res

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    matrix = list(map(int, sys.stdin.readline().strip().split(" ")))
    print(get_max(n, matrix))
