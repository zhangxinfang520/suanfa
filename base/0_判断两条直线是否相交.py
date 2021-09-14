# -*- coding:utf-8 -*-
#@Time : 2021/9/14 13:38
#@Author: zxf_要努力
#@File : 0_判断两条直线是否相交.py

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Solution:
    def is_cross(self,points_list):
        point_a,point_b,point_c,point_d = points_list
        c_fc = self.get_fx(point_c,point_a,point_b)
        d_fc = self.get_fx(point_d,point_a,point_b)
        if c_fc * d_fc > 0:
            return True
        else:
            return False


    def get_fx(self,ponitx,pointa,pointb):
        return (ponitx.x-pointa.x)*(pointa.y-pointb.y) - (ponitx.y-pointa.y) * (pointa.x - pointb.x)

if __name__ == '__main__':
    point_a = Point(0,0)
    point_b = Point(2,2)
    point_c = Point(0,-2)
    point_d = Point(1,0)
    print(Solution().is_cross([point_a, point_b, point_c, point_d]))