# -*- coding:utf-8 -*-
#@Time : 2021-05-02 14:06
#@Author: zxf_要努力
#@File : 107_二叉树的遍历 倒序遍历.py
'''
使用队列进行求解
求得是正序的层次遍历 最后使用[：：-1]
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        reuslt = []
        if not root:
            return reuslt
        queque = list()
        queque.append(root)
        while len(queque) > 0:
            temp = []
            for i in range(len(queque)):
                node = queque.pop(0)
                temp.append(node.val)
                if node.left:
                    queque.append(node.left)
                if node.right:
                    queque.append(node.right)
            if len(temp) > 0:
                reuslt.append(temp)

        return reuslt[::-1]