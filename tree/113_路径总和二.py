# -*- coding:utf-8 -*-
#@Time : 2021-05-03 19:25
#@Author: zxf_要努力
#@File : 113_路径总和二.py
'''
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]


输入：root = [1,2,3], targetSum = 5
输出：[]

深度优先遍历
dfs 最关键的就是记得删除节点
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        ret = list()
        path = list()

        def dfs(node: TreeNode,total:int):
            path.append(node.val)
            total -= node.val
            if not node.left and not node.right and total == 0:
                ret.append(path[:])
            if node.left:
                dfs(node.left,total)
            if node.right:
                dfs(node.right,total)
            path.pop()
        dfs(root,total)
        return ret


    def allpath(self,root:TreeNode):
        ret =list()
        path =list()
        def fds(node:TreeNode):
            path.append(node.val)
            if not node.left and not node.right:
                ret.append(path[:])
            if node.left:
                fds(node.left)
            if node.right:
                fds(node.right)
            path.pop()
        fds(root)

        return ret


left_tree = TreeNode(7)
right_tree = TreeNode(2)

tree = TreeNode(11)
tree.left = left_tree
tree.right = right_tree

tree_4 = TreeNode(4)
tree_4.left = tree

left_tree = tree_4

rirht_tree_r = TreeNode(1)
node_4 = TreeNode(4)
node_4.right = rirht_tree_r

node_13 = TreeNode(13)
node_8 = TreeNode(8)
node_8.left = node_13
node_8.right = node_4

tree = TreeNode(5)
tree.left = left_tree
tree.right = node_8

#print(Solution().pathSum(tree, 22))
print(Solution().allpath(tree))



