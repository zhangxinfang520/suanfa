
#堆排序的联系
from typing import List


class Create_Small_heap:

    def __init__(self,k):
        #求最大的几个数
        self.val = []
        self.k = k

    def get_left(self,idx):
        return (2 * idx + 1) if len(self.val) >  (2 * idx + 1) else None

    def get_right(self, idx):
        return (2 * idx + 2) if len(self.val) > (2 * idx + 2) else None

    def get_parent(self,idx):
        return (idx - 1) // 2 if idx > 0 else None

    def sift_down(self,idx):
        cur = idx
        l = self.get_left(cur)
        r = self.get_right(cur)
        if not l:
            min_child = r
        elif not r:
            min_child = l
        else:
            min_child = l if self.val[l] < self.val[r] else r
        while cur is not None and min_child is not  None and self.val[cur] > self.val[min_child]:
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

    def sift_up(self,idx):
        cur = idx
        parent = self.get_parent(cur)
        while cur is not None and parent is not None and self.val[cur] < self.val[parent]:
            self.val[cur], self.val[parent] = self.val[parent], self.val[cur]
            cur = parent
            parent = self.get_parent(cur)

    def insert_one(self,values):
        if len(self.val) < self.k:
            self.val.append(values)
            idx = len(self.val) -1
            self.sift_up(idx)
        elif values > self.val[0]:
            self.delete()
            self.insert(values)
        else:
            return

    def insert(self,values):
        if isinstance(values,list):
            for value in values:
                self.insert_one(value)
        elif isinstance(values,int):
            self.insert_one(values)

    def delete(self):
        if self.val:
            self.val[0], self.val[-1] = self.val[-1], self.val[0]
            value = self.val.pop()
            self.sift_down(0)
            return value
        return

    def traver(self):
        res = []
        for i in range(self.k):
            value = self.delete()
            res.append(value)
        return res


if __name__ == '__main__':
    val = [1,2,3,4,5,6,8]
    heap = Create_Small_heap(5)
    heap.insert(val)
    print(heap.traver())