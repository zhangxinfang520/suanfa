# -*- coding:utf-8 -*-
#@Time : 2021-05-02 15:30
#@Author: zxf_要努力
#@File : 106_从中序和后序构建二插树.py
'''
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
思路和前序和中序构建二叉树一样的
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        in_len = len(inorder)
        post_len = len(postorder)
        if in_len != post_len:
            return None
        loc_map = dict()
        for i,val in enumerate(inorder):
            loc_map[val] = i
        root = self.__bulid_Tree(postorder,0,post_len-1,
                                 inorder,0,in_len-1,loc_map)
        return root


    def __bulid_Tree(self, postorder, postl, postr, inorder, inl,inr, loc_map):

        if postl > postr or inl > inr:
            return None
        pivot = postorder[postr]
        pivot_index = loc_map[pivot]
        root = TreeNode(pivot)
        root.left = self.__bulid_Tree(postorder,postl,pivot_index+postl-inl-1,
                                      inorder,inl,pivot_index-1,loc_map)
        root.right = self.__bulid_Tree(postorder,pivot_index+postl-inl,postr-1,
                                       inorder,pivot_index+1,inr,loc_map)
        return root


def mid_order(root:TreeNode):
    if root.left:
        mid_order(root.left)

    if root.right:
        mid_order(root.right)
    print(root.val, end="")

inorder = [9,3,15,20,7]
postorder =  [9,15,7,20,3]
mid_order(Solution().buildTree(inorder,postorder))