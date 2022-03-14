# -*- coding:utf-8 -*-
#@Time : 2021/9/10 17:30
#@Author: zxf_要努力
#@File : 网易2.py

#在两个升序列表中找到第K小的数

class Solution:
    def find_kth(self , arr1 , arr2 , k ):
        # write code here 时间复杂度为log（m）
        #中位数 选出两个数组的 前 K/2 大小的部分进行比较
        m, n = len(arr1),len(arr2)
        if(m == 0):
            return arr2[k-1]
        if k == 0:
            return 0
        if n == 0:
            return arr1[k-1]
        return self.find(arr1,0,m-1,arr2,0,n-1,k-1)

    def find(self,arr1,l1,r1,arr2,l2,r2,k):
        if l1 > r1:
            return arr2[l2+k]
        if l2 > r2:
            return arr1[l1+k]
        if k == 0:
            return min(arr1[l1],arr2[l2])
        md1 = l1+k//2 if l1 +k//2 < r1 else r1
        md2 = l2+k//2 if l1 +k//2 < r2-l1 else r2
        if arr1[md1]<arr2[md2]:
            return self.find(arr1,md1+1,r1,arr2,l2,r2,k-k // 2-1)
        elif arr1[md1] > arr2[md2]:
            return self.find(arr1, l1, r1, arr2, md2+1, r2, k - k // 2 - 1)
        else:
            return arr1[md1]


if __name__ == '__main__':
    arr1 = [1, 3, 5]
    arr2 = [2, 3, 6]
    k = 0
    print(Solution().find_kth(arr1, arr2, k))

