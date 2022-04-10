# encoding: utf-8
"""
@author: zxf_要努力
@file: 字节跳动1.py
@time: 2022/4/10 10:25
"""
import sys


def change(results,i,j):
    #判断四周
    n,m = len(results),len(results[0])
    count = 0
    if i == 0 and j == 0:
        if i < n and j+1 < m and results[i][j+1] == 0:
            count +=1
        if i+1 < n and j<m and results[i+1][j] == 0:
            count += 1
    elif i == 0:
        if j+1 < m and results[i][j+1] == 0:
            count +=1
        if results[i][j-1] == 0:
            count +=1
        if i+1 < n and results[i+1][j] == 0:
            count +=1
    elif j == 0:
        if i+1 < n and results[i+1][j] == 0:
            count +=1
        if results[i-1][j] == 0 :
            count +=1
        if j + 1 < m and results[i][j + 1] == 0:
            count += 1
    else:
        if results[i-1][j] == 0:
            count +=1
        if i+1 < n and results[i+1][j] == 0:
            count +=1
        if results[i][j-1] == 0:
            count +=1
        if j+1 < m and results[i][j+1] == 0:
            count += 1
    if count > 1:
        return True
    return False


def get_decrease(results):
    n,m = len(results),len(results[0])
    res = []
    for i in range(n):
        for j in range(m):
            if results[i][j] == 1:
                if change(results,i,j):
                    res.append((i,j))
    for r,c in res:
        results[r][c] = 0
    return results


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n,m = list(map(int,sys.stdin.readline().strip().split(" ")))
        results = []
        for i in range(n):
            temp = list(map(int,list(sys.stdin.readline().strip())))
            results.append(temp)
        results = get_decrease(results)
        for i in range(n):
            row = results[i]
            print("".join(str(i) for i in row))




