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
    print([heapq.heappop(heap) for _ in range(len(nums))])
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
    # print(heapq.nlargest(3, nums))
    # print(heapq.nsmallest(3, nums))


class Create_Small_Heap:
    def __init__(self,k):
        '''建立小顶堆'''
        self.val = []
        self.k = k

    def get_left(self,idx):
        return idx * 2 + 1 if len(self.val) > (idx * 2 + 1) else None

    def get_right(self,idx):
        return idx * 2 + 2 if len(self.val) > (idx * 2 + 2) else None

    def get_parent(self,idx):
        return (idx - 1) // 2 if idx > 0 else None

    def sift_up(self,idx):
        cur = idx
        parent = self.get_parent(idx)
        while parent is not None and self.val[cur] < self.val[parent]:
            self.val[cur], self.val[parent] = self.val[parent], self.val[cur]
            cur = parent
            parent = self.get_parent(cur)

    def insert(self,value):

        if len(self.val) < self.k:
            self.val.append(value)
            idx = len(self.val) - 1
            self.sift_up(idx)
        else:
            if value > self.val[0]:
                self.delete()
                self.val.append(value)
                idx = len(self.val) - 1
                self.sift_up(idx)
        return

    def sift_down(self,idx):
        l = self.get_left(idx)
        r = self.get_right(idx)
        cur = idx
        if not l:
            min_child = r
        elif not r:
            min_child = l
        else:
            min_child = l if self.val[l] < self.val[r] else r

        while cur is not None and min_child is not None and self.val[cur] > self.val[min_child]:
            self.val[cur], self.val[min_child] = self.val[min_child], self.val[cur]
            cur = min_child
            l = self.get_left(cur)
            r = self.get_right(cur)
            if not l:
                min_child = r
            elif not r:
                min_child = l
            else:
                min_child = l if self.val[l] < self.val[r] else r

    def delete(self):
        if self.val:
            self.val[0], self.val[-1] = self.val[-1], self.val[0]
            values = self.val.pop()
            self.sift_down(0)
            return values
        return None

    def traver(self):
        #遍历
        res = []
        while len(self.val):
            res.append(self.delete())
        return res


class Create_Big_Heap:

    def __init__(self,k):
        self.val = []
        self.k = k

    def get_left(self,idx):
        return 2 * idx + 1 if len(self.val) > ( 2 * idx + 1) else None

    def get_right(self,idx):
        return 2 * idx + 2 if len(self.val) > ( 2 * idx + 2) else None

    def get_parent(self,idx):
        return (idx - 1) // 2 if idx > 0 else None

    def sift_up(self,idx):
        '''一般在插入数据的时候使用'''
        cur = idx
        parent = self.get_parent(idx)
        while parent is not None and self.val[cur] > self.val[parent]:
            self.val[cur], self.val[parent] = self.val[parent], self.val[cur]
            cur = parent
            parent = self.get_parent(cur)

    def sift_down(self,idx):
        '''一般在删除数据的时候使用'''
        cur = idx
        l = self.get_left(idx)
        r = self.get_right(idx)
        if not l:
            max_child = r
        elif not r :
            max_child = l
        else:
            max_child = l if self.val[l] > self.val[r] else r
        while cur is not None and max_child is not None and self.val[cur] < self.val[max_child]:
            self.val[cur], self.val[max_child] = self.val[max_child], self.val[cur]
            cur = max_child
            l = self.get_left(cur)
            r = self.get_right(cur)
            if not l :
                max_child = l
            elif not r :
                max_child = r
            else:
                max_child = l if self.val[l] > self.val[r] else r

    def delete(self):
        if self.val:
            self.val[0], self.val[-1] = self.val[-1], self.val[0]
            values = self.val.pop()
            self.sift_down(0)
            return values
        return

    def insert(self,value):
        if len(self.val) < self.k:
            self.val.append(value)
            idx = len(self.val) -1
            self.sift_up(idx)
        else:
            if value < self.val[0]:
                self.delete()
                self.val.append(value)
                idx = len(self.val) - 1
                self.sift_up(idx)

    def traver(self):
        res = []
        while len(self.val):
            res.append(self.delete())
        return res

if __name__ == '__main__':
    # heapq_op()
    # arr = [8,7,5,6,1,2,8]
    heap = Create_Big_Heap(4)
    #heap = Create_Small_Heap(10)
    heap.insert(1)
    heap.insert(3)
    heap.insert(5)
    heap.insert(6)
    heap.insert(4)
    heap.insert(2)
    heap.insert(8)
    heap_list = heap.val
    temp = heap_list.copy()
    print(heap.traver())

