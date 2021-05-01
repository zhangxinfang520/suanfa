# -*- coding:utf-8 -*-
#@Time : 2021-04-26 16:52
#@Author: zxf_要努力
#@File : 102.py
#给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 3
# / \
#     9
# 20
# / \
#     15
# 7
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
from typing import List


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self,root:TreeNode)->List[List[int]]:
        def LChild_Of_node(node: TreeNode):
            return node.left if node.left is not None else None

        def RChild_Of_node(node):
            return node.right if node.right is not None else None
        height = self.get_lenght_tree(root)
        level_order = []
        if root.val !=0:
            level_order.append([root])
        if height >=1:
            for _ in range(1,height+1):
                level = []
                for node in level_order[-1]:
                    if LChild_Of_node(node):
                        level.append(LChild_Of_node(node))
                    if RChild_Of_node(node):
                        level.append(RChild_Of_node(node))
                if level:
                    level_order.append(level)
            for i in range(0,height):
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].val
        return level_order


    def get_lenght_tree(self,tree:TreeNode):
        if tree.val == 0: return 0
        elif tree.left is None and tree.right is None:
            return 1
        elif tree.left is None and tree.right is None:
            return 1 + self.get_lenght_tree(tree.right)
        elif tree.left is not None and tree.right is None:
            return 1 + self.get_lenght_tree(tree.left)
        else:
            return 1 + max(self.get_lenght_tree(tree.left),self.get_lenght_tree(tree.right))


left_tree = TreeNode(9)
right_tree = TreeNode(20)
right_tree.left = TreeNode(15)
right_tree.right = TreeNode(7)
btree = TreeNode(3)
btree.left = left_tree
btree.right = right_tree

# right_tree = TreeNode(6)
# right_tree.left = TreeNode(2)
# right_tree.right = TreeNode(4)
#
# left_tree = TreeNode(5)
# left_tree.left = TreeNode(1)
# left_tree.right = TreeNode(3)
#
# tree = TreeNode(11)
# tree.left = left_tree
# tree.right = right_tree
#
# left_tree = TreeNode(7)
# left_tree.left = TreeNode(3)
# left_tree.right = TreeNode(4)

# right_tree = tree # 增加新的变量
# tree = TreeNode(18)
# tree.left = left_tree
# tree.right = right_tree


solution = Solution()
print(solution.levelOrder(btree))
