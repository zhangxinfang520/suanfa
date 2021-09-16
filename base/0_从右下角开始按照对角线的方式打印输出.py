# -*- coding:utf-8 -*-
#@Time : 2021/9/14 15:29
#@Author: zxf_要努力
#@File : 0_从右下角开始按照对角线的方式打印输出.py

class Solution:
    def printpath(self,nums):
        m,n = len(nums),len(nums[0])
        res = []
        for row in list(range(m+n-1)):
            #反转元素的开始位置
            ret_count = len(res)
            i = row if row+1 <=m else m-1
            j = n - 1 if row + 1 <= m else (m + n - 1) - row - 1
            # 获取每条对角线上的元素

            while i >= 0 and j >= 0:
                res.append(nums[i][j])
                i -= 1
                j -= 1
          # 奇数行顺序反转
            if row % 2 == 0:
                res = res[:ret_count] + res[ret_count:][::-1]
        return res

if __name__ == '__main__':
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().printpath(nums))