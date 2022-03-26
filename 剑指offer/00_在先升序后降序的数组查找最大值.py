# encoding: utf-8
"""
@author: zxf_要努力
@file: 00_在先升序后降序的数组查找最大值.py
@time: 2022/3/25 18:36
"""


def get_max(nums):
    n = len(nums)

    def bin(left,right):
        mid = left + (right - left) // 2
        if (mid == 0 or nums[mid-1] <= nums[mid]) and (mid == n-1 or nums[mid+1] <= nums[mid]):
            return mid
        elif mid > 0 and nums[mid-1] > nums[mid]:
            return bin(left, mid-1)
        else:
            return bin(mid+1, right)
    return bin(0,n)


if __name__ == '__main__':
    nums = [4,5,8,9,2,1]
    print(nums[get_max(nums)])