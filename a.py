# -*- coding:utf-8 -*-
# @Time : 2021-07-01 16:54
# @Author: zxf_要努力
# @File : a.py

def quick_sort(nums):
    def sort(l, r):
        if l >= r: return
        i, j = l, r
        temp = nums[i]
        while i < j:
            while i < j and nums[j] > temp:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] < temp:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = temp
        sort(l, i - 1)
        sort(i + 1, r)

    sort(0, len(nums) - 1)
    return nums


if __name__ == '__main__':
    a = "abec"
    b = "abcdd"
    print(a  in b)

	# nums = [7,1,3,6,8,4]
	# print(quick_sort(num
