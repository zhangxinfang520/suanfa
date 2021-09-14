# -*- coding:utf-8 -*-
#@Time : 2021/9/14 13:12
#@Author: zxf_要努力
#@File : 0_构建二叉树.py

#将有序数组转换为二叉搜索树
from tree.create_tree_by_list import *
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def helper(self,nums):
        def bulid_tree(left,right):
            if left <= right:
                mid = (left + right) // 2
                root = TreeNode(nums[mid])
                root.left = bulid_tree(left,mid-1)
                root.right = bulid_tree(mid+1,right)
                return root
            else:
                return None
        tree = bulid_tree(0, len(nums)-1)
        return tree

if __name__ == '__main__':
    nums = [1,2,5,6,7,8,9]
    root = Solution().helper(nums)
    print(pre_order_norecursion(root))
    print(mid_order_norecursion(root))

