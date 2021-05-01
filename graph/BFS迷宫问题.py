# -*- coding:utf-8 -*-
#@Time : 2021-04-26 20:37
#@Author: zxf_要努力
#@File : BFS迷宫问题.py
import queue
print("Please input the size of the square:")
n = int(input())
map_ = [([0]*n) for i in range(n)] #创建地图
vis = [([0]*n) for i in range(n)] #访问标记
front = [([0]*n) for i in range(n)] #路径
s,t = [0,0],[n-1,n-1] #初始化猫(s)鼠(t)位置
xPos = [1,0,-1,0] # x坐标方向
yPos = [0,1,0,-1] # y坐标方向

def bfs(x,y):
    q = queue.Queue()
    q.put([x,y])
    vis[x][y]=1
    while q.qsize() != 0:
        now = q.get()
        if now == [n-1,n-1]:
            return
        for i in range(0,4):
            xx = now[0] + xPos[i]
            yy = now[1] + yPos[i]
            if xx<0 or xx>n-1 or yy<0 or yy>n-1:
                continue
            elif map_[xx][yy] == 1 or vis[xx][yy]==1:
                continue
            else:
                q.put([xx,yy])
                vis[xx][yy]=1
                front[xx][yy]=now # 记录上一次的位置
    return
def printRoad():
    q = queue.LifoQueue() #栈
    now=[n-1,n-1]
    while now != [0,0]:
        # print(now)
        q.put(now)
        now = front[now[0]][now[1]]
    print("The road：")
    while q.qsize():
        temp = q.get()
        print(temp)

for i in range(n):
    map_[i] = input().split(" ")
map_[0][0]='S' #标记猫位置
map_[n-1][n-1]='T' #标记鼠位置

bfs(0,0)
printRoad()