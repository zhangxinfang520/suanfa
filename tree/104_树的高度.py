# -*- coding:utf-8 -*-
#@Time : 2021-05-02 13:53
#@Author: zxf_要努力
#@File : 104_树的高度.py
'''
求二叉树的高度 递归即可
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def getDepth(node):
            if not node:
                return 0
            elif node.left is None and node.right is None:
                return 1
            elif node.left is not None and node.right is None:
                return 1 + getDepth(node.left)
            elif node.left is None and node.right is not None:
                return 1 + getDepth(node.right)
            else:
                return 1 + max(getDepth(node.left), getDepth(node.right))

        return getDepth(root)
