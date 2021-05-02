# -*- coding:utf-8 -*-
#@Time : 2021-05-02 14:16
#@Author: zxf_要努力
#@File : 105_前序和中序构建二叉树.py
'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


思路:
    只要我们在中序遍历中定位到根节点，那么我们就可以分别知道左子树和右子树中的节点数目。
    由于同一颗子树的前序遍历和中序遍历的长度显然是相同的，因此我们就可以对应到前序遍历的结果中，
    对上述形式中的所有左右括号进行定位。这样以来，我们就知道了左子树的前序遍历和中序遍历结果，
    以及右子树的前序遍历和中序遍历结果，我们就可以递归地对构造出左子树和右子树，再将这两颗子树接到根节点的左右位置。



'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pre_len = len(preorder)
        in_len = len(inorder)
        if pre_len != in_len:
            return None
        loc_map = dict()
        for i,val in enumerate(inorder):
            loc_map[val] = i
        root = self.__bulid_tree(preorder,0,pre_len-1,
                          inorder,0,in_len-1,loc_map)
        return root

    def __bulid_tree(self, preorder,prel, prer, inorder, inl, inr, loc_map):
        if prel > prer or inl > inr:
            return None
        pivot = preorder[prel]
        pivot_index = loc_map[pivot]
        root = TreeNode(pivot)

        root.left = self.__bulid_tree(preorder,prel+1,pivot_index+prel-inl,
                                      inorder,inl,pivot_index-1,loc_map)
        root.right = self.__bulid_tree(preorder,pivot_index+prel-inl+1,prer,
                                       inorder,pivot_index+1,inr,loc_map)
        return root


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Solution().buildTree(preorder,inorder)

