# encoding: utf-8
"""
@author: zxf_要努力
@file: 位运算学习.py
@time: 2022/3/21 15:57
"""
import heapq

'''
& 与运算 两位为1 才为1
| 或运算 两位为0 才问0
^ 异或运算 两位相同为 0 否则为1
~ 取反0变1 1变0
<< 左移 高位丢弃 地位补0
>> 右移 各二进位全部右移若干位，对无符号数，高位补0，有符号数，各编译器处理方法不一样，有的补符号位（算术右移），有的补0（逻辑右移）
'''


#左移
#左移n位 代表乘以 2^n
#右移n为 代表除以 2^n
# print(8>>2)

#两个数 进行交换

def swap(a,b):
    a ^= b
    b ^= a
    a ^= b
    return a,b

def get_abs(a):
    return ~a +1

class Income:
    def __init__(self,cost,profit):
        self.cost = cost
        self.profit = profit

def cmp(a,b):
    if a.cost > b.cost:
        return 1
    elif a.cost < b.cost:
        return -1
    else:
        if a.profit < b.profit:
            return 1
        else:
            return -1

class Solution:
    def get_max(self,N,K,W,cost,profit):
        q = []
        while K > 0:
            for i in range(len(cost)):
                if cost[i] < W :
                    #优先队列
                    heapq.heappush(q,-profit[i])
            if not q:
                return W
            else:
                #获取最大的
                max_=-heapq.heappop(q)
                index = profit.index(max_)
                cost.pop(index)
                W += max_
            K -= 1
        return W








if __name__ == '__main__':
    a = 4
    b = 9
    N, W, K = 5,3,2
    cost = [5,4,1,2,2,3]
    profit = [3,5,3,2,7,7]
    print(Solution().get_max(N, K, W, cost, profit))
    # #print(swap(a,b))
    # print(get_abs(-a))
    #rint(b)
