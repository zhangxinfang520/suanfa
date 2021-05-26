# -*- coding:utf-8 -*-
#@Time : 2021-05-26 20:12
#@Author: zxf_要努力
#@File : 贪心问题_435_无重叠区间.py
#贪心问题 就是每一步都选择最优的
'''
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

思路：
正确的思路其实很简单，可以分为以下三步：
从区间集合 intvs 中选择一个区间 x，这个 x 是在当前所有区间中结束最早的（end 最小）。
把所有与 x 区间相交的区间从区间集合 intvs 中删除。
重复步骤 1 和 2，直到 intvs 为空为止。之前选出的那些 x 就是最大不相交子集。
'''
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==1:
            return 0
        sort_list = sorted(intervals,key=lambda x:x[1],reverse=False)
        result = list()
        result.append(sort_list.pop(0))

        while len(sort_list):
            if result[-1][1] > sort_list[0][0]:
                sort_list.pop(0)
            else:
                result.append(sort_list.pop(0))

        return len(intervals) - len(result)



#nums = [ [1,2], [2,3], [3,4], [1,3] ]
nums = [ [1,2], [1,2],[1,2],[1,2] ]
print(Solution().eraseOverlapIntervals(nums))