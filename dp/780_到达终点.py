# encoding: utf-8
"""
@author: zxf_要努力
@file: 780_到达终点.py
@time: 2022/4/9 10:57
"""
'''
给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，
则返回 true，否则返回 false。 从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。

如果从 (sx,sy) 开始正向计算，则可能的情况非常多，会超出时间限制。注意到sx,sy,tx,ty 都是正整数，因此对于给定的状态 (tx,ty)，只有当ty 不等于 tx 
时才存在上一个状态，且上一个状态唯一，可能的情况如下：
如果 tx=ty，不存在上一个状态，状态 (tx,ty) 即为起点状态；
如果 tx>ty，则上一个状态是(tx−ty,ty)；
如果 tx<ty，则上一个状态是 (tx,ty−tx)。
因此可以从 (tx,ty) 开始反向计算，判断是否可以到达状态(sx,sy)。当 tx>sx,ty>sy,tx不等于ty 三个条件同时成立时，执行反向操作，每一步操作更新 (tx,ty) 的值，
直到反向操作的条件不成立。
由于每一步反向操作一定是将 tx 和 ty 中的较大的值减小，因此当 tx>ty 时可以直接将tx 的值更新为txmodty，当tx<ty 时可以直接将 ty 的值更新为 tymodtx。
当反向操作的条件不成立时，根据tx 和 ty 的不同情况分别判断是否可以从起点转换到终点。
如果 ty=sy，则已经到达起点状态，因此可以从起点转换到终点。
如果 tx=sx 且 ty!=sy，则 tx 不能继续减小，只能减小ty，因此只有当ty>sy 且 (ty−sy)modtx=0 时可以从起点转换到终点。
如果 ty=sy 且 tx!=sx，则 ty 不能继续减小，只能减小tx，因此只有当tx>sx 且(tx−sx)modty=0 时可以从起点转换到终点。
如果 tx!=sx 且 ty!=sy，则不可以从起点转换到终点。
'''

class Solution(object):
    def reachingPoints1(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        #正向计算 会超时
        def dp(i,j):
            if i == tx and j == ty:
                return True
            if i > tx or j > ty:
                return False
            return dp(i,i+j) or dp(i+j,j)
        return dp(sx,sy)

    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        #反向计算
        while sx < tx != sy < ty:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if sx == tx and sy == ty:
            return True
        elif tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        elif ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        else:
            return False




if __name__ == '__main__':
    sx = 35
    sy = 13
    tx = 455955547
    ty = 420098884
    print(Solution().reachingPoints(sx, sy, tx, ty))