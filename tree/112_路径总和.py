# -*- coding:utf-8 -*-
# @Time : 2021-05-03 17:41
# @Author: zxf_要努力
# @File : 112_路径总和.py
'''
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
叶子节点 是指没有子节点的节点
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true\
两个函数两个方法
第一个方法  前序遍历  遍历所有 根节点 到叶子节点的路径 这种方法在leetcode上通过了 但是我认为有bug 不推荐使用
第二个方法 层次遍历

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        node_list = []
        bool_list = []
        node_list.append(root.val)
        def pre_order(node, target):
            if not node.left and not node.right and target == node.val:
                print(node_list)
                bool_list.append(True)
            if not node.left and not node.right and target != node.val:
                print(node_list)
                bool_list.append(False)
            if node.left:
                node_list.append(node.left.val)
                pre_order(node.left, target - node.val)
            if node.right:
                node_list.append(node.right.val)
                pre_order(node.right, target - node.val)

        pre_order(root, targetSum)

        if True in bool_list:
            return True

        return False

    def queque_Sum(self, root: TreeNode, targetSum: int):
        if not root:
            return False
        queque_node = list()
        queque_val = list()
        queque_node.append([root])
        queque_val.append([root.val])
        while len(queque_node) > 0:
            temp_node = queque_node.pop(0)
            temp_val = queque_val.pop(0)
            temp_node_list = list()
            temp_val_list = list()

            for node, val in zip(temp_node, temp_val):
                if not node.left and not node.right:
                    if val == targetSum:
                        return True
                    continue

                if node.left:
                    temp_node_list.append(node.left)
                    temp_val_list.append(node.left.val + val)
                if node.right:
                    temp_node_list.append(node.right)
                    temp_val_list.append(node.right.val + val)
            if len(temp_node_list) > 0 and len(temp_val_list) > 0:
                queque_node.append(temp_node_list)
                queque_val.append(temp_val_list)

        return False


#
# left = TreeNode(2)
# right = TreeNode(3)
# tree = TreeNode(1)
# tree.left = left
# tree.right = right

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

print(Solution().hasPathSum(tree, 22))
# print(Solution().queque_Sum(tree, 22))



