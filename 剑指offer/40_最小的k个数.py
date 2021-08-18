'''
输入整数数组
arr ，找出其中最小的
k
个数。例如，输入4、5、1、6、2、7、3、8
这8个数字，则最小的4个数字是1、2、3、4。
heapq 是构建小根堆的库
最大 top k 问题用最小堆，求最小 top k 问题用最大堆
'''
from typing import List
import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k < 0:
            return
        heap = []
        for num in arr:
            heapq.heappush(heap, num)
        res = [heapq.heappop(heap) for _ in range(k)]
        return res

    def getLeastNumbers1(self, arr: List[int], k: int) -> List[int]:
        # #只建立k数量的小根堆
        if k < 0:
            return
        heap = [-x for x in arr[:k]]
        heapq.heapify(heap)
        print([heapq.heappop(heap) for _ in range(k)])
        for i in range(k,len(arr)):
            if -heap[0] > arr[i]:
                heapq.heappop(heap)
                heapq.heappush(heap,-arr[i])
        res = [-hp for hp in heap]
        return res


class Heap:
    def __init__(self, k):
        self.val = []
        self.k = k

    def get_left(self, idx):
        return idx * 2 + 1 if len(self.val) > idx * 2 + 1 else None

    def get_right(self, idx):
        return idx * 2 + 2 if len(self.val) > idx * 2 + 2 else None

    def get_parent(self, idx):
        return (idx - 1) // 2 if idx > 0 else None

    def sift_up(self, idx):
        cur = idx
        parent = self.get_parent(idx)
        while parent is not None and self.val[cur] < self.val[parent]:
            # print(parent, cur, self.val[parent], self.val[cur])
            temp = self.val[cur]
            self.val[cur] = self.val[parent]
            self.val[parent] = temp
            cur = parent
            parent = self.get_parent(cur)

    def insert(self, n):
        if len(self.val) < self.k:
            self.val.append(n)
            idx = len(self.val) - 1
            self.sift_up(idx)
        else:
            if n > self.val[0]:
                self.delete()
                self.val.append(n)
                idx = len(self.val) - 1
                self.sift_up(idx)
        return

    def sift_down(self, idx):
        l = self.get_left(idx)
        r = self.get_right(idx)
        cur = idx
        if not l:
            min_child = r
        elif not r:
            min_child = l
        else:
            min_child = l if self.val[l] == min(self.val[l], self.val[r]) else r

        while cur is not None and min_child is not None and self.val[cur] > self.val[min_child]:
            # print(cur, min_child, self.val[cur], self.val[min_child])
            temp = self.val[cur]
            self.val[cur] = self.val[min_child]
            self.val[min_child] = temp
            cur = min_child
            l = self.get_left(cur)
            r = self.get_right(cur)
            if not l:
                min_child = r
            elif not r:
                min_child = l
            else:
                min_child = l if self.val[l] == min(self.val[l], self.val[r]) else r

    def delete(self):
        if self.val:
            temp = self.val[0]
            self.val[0] = self.val[-1]
            self.val[-1] = temp
            n = self.val.pop()
            self.sift_down(0)
            return n
        return None

if __name__ == '__main__':
    arr = [3,2,1]
    k = 2
    print(Solution().getLeastNumbers1(arr, k))

