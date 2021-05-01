# -*- coding:utf-8 -*-
#@Time : 2021-04-26 19:30
#@Author: zxf_要努力
#@File : asda.py
result =  []

m=3
n=5
def go_on(x1,y1,x2,y2):
    if x1==x2 and y1==y2:
        return True
    if y1+1 < n and x1+1<m:
        go_on(x1+1,y1,x2,y2)
        result.append([x1+1,y1])
    if x1+1<m and y1+1 < n:
        go_on(x1,y1+1,x2,y2)
        result.append([x1, y1+1])
    if x1==m and y1==n:
        result.remove([(x1,y1)])
        go_on(x1-1,y1,x2,y2)
        go_on(x1-1,y1-1,x2,y2)
        go_on(x1-1,y1-1,x2,y2)
    else:
        go_on(x1+1,y1,x2,y2)
        go_on(x1,y1+1,x2,y2)
        go_on(x1+1,y1+1,x2,y2)
go_on(1,1,5,5)