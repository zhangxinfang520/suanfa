# -*- coding:utf-8 -*-
#@Time : 2021-07-29 20:25
#@Author: zxf_要努力
#@File : 169_多数元素.py
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = dict()
        for x in nums:
            if x not in result.keys():
                result[x] = 1
            else:
                temp = result[x]
                temp +=1
                result[x] = temp
        list_ = sorted(result.items(),key=lambda x:-x[1])
        return list_[0][0]

nums = [6,5,5]
print(Solution().majorityElement(nums))