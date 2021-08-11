# -*- coding:utf-8 -*-
#@Time : 2021-08-10 17:57
#@Author: zxf_要努力
#@File : 堆排序.py
import heapq

'''堆是二叉树，最大堆中父节点大于或等于两个子节点，
最小堆父节点小于或等于两个子节点。'''

def heapq_op():
    #创建堆
    # 一种是使用一个空列表，然后使用heapq.heappush()函数把值加入堆中，
    # 另外一种就是使用heap.heapify(list)转换列表成为堆结构
    #第一种
    heap = []
    nums = [2, 3, 5, 1, 54, 23, 132]
    for i,num in enumerate(nums):
        heapq.heappush(heap,num)
    # print(heap)
    # print([heapq.heappop(heap) for _ in range(len(nums))])
    #第二种
    # nums = [2,3,5,1,54,23,132]
    # heapq.heapify(nums)
    # print([heapq.heappop(nums) for _ in range(len(nums))])
    #合并多个排序后的序列成一个排序后的序列
    # num1 = [32, 3, 5, 34, 54, 23, 132]
    # num2 = [23, 2, 12, 656, 324, 23, 54]
    # num1 = sorted(num1)
    # num2 = sorted(num2)
    # res = heapq.merge(num1, num2)
    # print(list(res))
    #查找最小值
    #print(heapq.heappop(heap))
    #如果需要删除堆中最小元素并加入一个元素，可以使用heapq.heaprepalce() 函数
   # print([heapq.heappop(heap) for _ in range(len(nums))])
   #  heapq.heapreplace(heap, 500)
   #  print([heapq.heappop(heap) for _ in range(len(nums))])
   #如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或
    # heapq.nsmallest() 函数
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

if __name__ == '__main__':
    heapq_op()


