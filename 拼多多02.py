# encoding: utf-8
"""
@author: zxf_要努力
@file: 拼多多.py
@time: 2022/4/10 19:14
"""
import sys

class Node:
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step


def get_min_count_by_dfs(matrx, startX, startY, sourceX, sourceY,haveGo):
    go = [[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2]]
    check = [[0,-1],[1,0],[1,0],[0,1],[0,1],[-1,0],[-1,0],[0,-1]]
    queue = []
    flag = True
    queue.append(Node(startX,startY,0))
    while queue and flag:
        node = queue.pop(0)
        for i in range(8):
            if check_is_go(matrx,haveGo,node.x+go[i][0],node.y+go[i][1],node.x+check[i][0],node.y+check[i][1]):
                if node.x+go[i][0] == sourceX and node.y+go[i][1] == sourceY:
                    print(node.step+1)
                    flag = False
                    break
                queue.append(Node(node.x+go[i][0],node.y+go[i][1],node.step+1))
    if flag:
        print(-1)


def check_is_go(matrx,haveGo,tx,ty,checkx,checky):
    n, m = len(matrx), len(matrx[0])
    if tx < 0 or ty < 0 or tx >= n or ty >= m or haveGo[tx][ty]:
        return False
    else:
        if matrx[checkx][checky] != '0' and matrx[tx][ty] != '0':
            haveGo[tx][ty] = True
            return True
        else:
            return False


def get_min_count(matrx, startX, startY, sourceX, sourceY):
    memo = []
    n, m = len(matrx), len(matrx[0])

    def dp(i, j):
        if matrx[i][j] == "0":
            return float("inf")
        if i == sourceX and j == sourceY:
            return 0
        if i >= n or j >= m or i < 0 or j < 0:
            return float("inf")
        if (i, j) in memo:
            return float("inf")

        memo.append((i, j))
        temp = float("inf")
        # if i == n-1 and j == m-1:
        #     if matrx[i-1][j] == '0' and matrx[i][j-1] == '0' :
        #         re = float("inf")
        #     elif matrx[i-1][j] == '0':
        #         re = min(temp, dp(i - 1, j - 2) + 1)
        #     elif matrx[i][j-1] == '0':
        #         re = min(temp, dp(i -2, j - 1) + 1)
        #     else:
        #         re = min(temp, dp(i -2, j - 1) + 1,dp(i - 1, j - 2) + 1)
        #
        # elif i == 0 and j == 0:
        #     if matrx[i+1][j] == '0' and matrx[i][j+1] == '0' :
        #         re = float("inf")
        #     elif matrx[i+1][j] == '0':
        #         re = min(temp, dp(i + 1, j + 2) + 1)
        #     elif matrx[i][j+1] == '0':
        #         re = min(temp, dp(i + 2, j + 1) + 1)
        #     else:
        #         re = min(temp, dp(i + 2, j + 1) + 1,dp(i + 1, j + 2) + 1)
        # elif i == n-1 and j == 0:
        #     if matrx[i-1][j] == '0' and matrx[i][j+1]=='0' :
        #         re = float("inf")
        #     elif matrx[i-1][j] == '0':
        #         re = min(temp, dp(i - 1, j + 2) + 1)
        #     elif matrx[i][j+1]:
        #         re = min(temp, dp(i - 2, j + 1) + 1)
        #     else:
        #         re = min(temp, dp(i - 1, j + 2) + 1,dp(i - 2, j + 1) + 1)
        # elif i == 0 and j == m-1:
        #     if matrx[i + 1][j] == '0' and matrx[i][j - 1] == '0':
        #         re =  float("inf")
        #     elif matrx[i + 1][j] == '0':
        #         re = min(temp, dp(i + 1, j - 2) + 1)
        #     elif matrx[i][j - 1] == '0':
        #         re = min(temp, dp(i + 2, j - 1) + 1)
        #     else:
        #         re = min(temp, dp(i + 1, j - 2) + 1,dp(i + 2, j - 1) + 1)
        # else:
        #     if matrx[i + 1][j] == '0' and matrx[i][j + 1] == '0' and matrx[i-1][j] == '0' and matrx[i][j-1] == '0':
        #         re = float("inf")
        re = min(temp, dp(i - 2, j + 1) + 1, dp(i - 2, j - 1) + 1, dp(i + 2, j + 1) + 1, dp(i + 2, j - 1) + 1,
                 dp(i - 1, j + 2) + 1, dp(i - 1, j - 2) + 1, dp(i + 1, j + 2) + 1, dp(i + 1, j - 2) + 1)
        return re

    return dp(startX, startY)

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    matrx = []
    startX, startY, sourceX, sourceY = 0, 0, 0, 0
    for _ in range(T):
        N, M = list(map(int, sys.stdin.readline().strip().split(" ")))
        haveGo = [[False] * M for _ in range(N)]
        for i in range(N):
            temp = list(sys.stdin.readline().strip())
            for j in range(M):
                if temp[j] == "K":
                    haveGo[i][j] = True
                    startX, startY = i, j
                if temp[j] == "T":
                    sourceX, sourceY = i, j
            matrx.append(temp)
        get_min_count_by_dfs(matrx, startX, startY, sourceX, sourceY,haveGo)

