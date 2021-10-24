# -*- coding:utf-8 -*-
#@Time : 2021/10/12 11:09
#@Author: zxf_要努力
#@File : 226反转二叉树.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverse(self,root):
        if not root:
            return 0
        root.left,root.right = self.reverse(root.right),self.reverse(root.left)
        return root