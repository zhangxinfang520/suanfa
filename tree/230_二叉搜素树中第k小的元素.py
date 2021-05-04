# -*- coding:utf-8 -*-
#@Time : 2021-05-04 10:57
#@Author: zxf_要努力
#@File : 230_二叉搜素树中第k小的元素.py
'''
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数

二叉搜索树 中序遍历为一个升序数组

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = []
        if not root:
            return []

        def mid_order(node: TreeNode):
            if node.left:
                mid_order(node.left)
            result.append(node.val)
            if node.right:
                mid_order(node.right)

        mid_order(root)
        return result[k - 1]
