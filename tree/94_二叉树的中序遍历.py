# -*- coding:utf-8 -*-
#@Time : 2021-05-01 20:06
#@Author: zxf_要努力
#@File : 94_二叉树的中序遍历.py
'''给定一个二叉树的根节点 root ，返回它的 中序 遍历。'''
from typing import List

"""
输入：root = [1,null,2,3]
输出：[1,3,2]
输入：root = []
输出：[]
输入：root = [1]
输出：[1]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def inorderTraversal(self,root:TreeNode)->List[int]:
        result = []
        if not root:
            return result

        def mid_order(node:TreeNode):
            if node.left:
                mid_order(node.left)
            result.append(node.val)
            if node.right:
                mid_order(node.right)
        mid_order(root)
        return result
