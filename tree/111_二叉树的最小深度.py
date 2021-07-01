# -*- coding:utf-8 -*-
#@Time : 2021-06-29 20:36
#@Author: zxf_要努力
#@File : 111_二叉树的最小深度.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def min_depth(root:TreeNode):
            if not root:
                return 0
            if root.left is None and root.right is None:
                return 1
            if root.left and root.right is None:
                return 1 + min_depth(root.left)
            if root.left is None and root.right :
                return 1 + min_depth(root.right)
            if root.right and root.left:
                return 1 + min(min_depth(root.left),min_depth(root.right))
        return min_depth(root)

    def get_min_depth_by_DFS(self,root: TreeNode):
        if not root:
            return 0
        queque = []
        queque.append(root)
        depth = 1
        while queque:
            len_queque = len(queque)
            for i in range(len_queque):
                temp_node = queque.pop(0)
                if temp_node.left is None and temp_node.right is None:
                    return depth
                if temp_node.left:
                    queque.append(temp_node.left)
                if temp_node.right:
                    queque.append(temp_node.right)
            depth +=1
        return depth

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
print(Solution().minDepth(tree))
print(Solution().get_min_depth_by_DFS(tree))