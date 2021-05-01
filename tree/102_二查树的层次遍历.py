# -*- coding:utf-8 -*-
#@Time : 2021-05-01 15:41
#@Author: zxf_要努力
#@File : 102.py

"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

 返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
#层次遍历
from typing import List

#提交格式为list[lsit]


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    使用队列 遍历层次结构
    '''
    def levelOrder(self,root:TreeNode)->List[List[int]]:
        result = []
        if not root:
            return result
        queque = []
        queque.append(root)
        while len(queque) >0:
            temp = []
            for i in range(len(queque)):
                node = queque[0]
                temp.append(node.val)
                queque.pop(0)
                if node.left:
                    queque.append(node.left)
                if node.right:
                    queque.append(node.right)
            result.append(temp)
        return result

