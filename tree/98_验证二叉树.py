# -*- coding:utf-8 -*-
#@Time : 2021-05-01 20:11
#@Author: zxf_要努力
#@File : 98_验证二叉树.py
'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
# 二叉搜数树 中序排序是一个升序数组
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        result = []

        #中序排序
        def mid_order(node):
            if node.left:
                mid_order(node.left)
            result.append(node.val)
            if node.right:
                mid_order(node.right)

        mid_order(root)

        for i in range(len(result) - 1):
            if result[i] >= result[i + 1]:
                return False
        return True