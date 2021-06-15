# -*- coding:utf-8 -*-
#@Time : 2021-06-15 22:03
#@Author: zxf_要努力
#@File : 852_山脉数组的封顶索引.py

#属于简单题  原始条件给的比较多
'''符合下列属性的数组 arr 称为 山脉数组 ：
arr.length >= 3
存在 i（0 < i < arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给你由整数组成的山脉数组 arr ，
返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ...
> arr[arr.length - 1] 的下标 i 。'''
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))