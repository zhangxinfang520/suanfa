# -*- coding:utf-8 -*-
#@Time : 2021-05-17 20:38
#@Author: zxf_要努力
#@File : 993_二叉树的堂兄节点.py
'''
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。
输入：root = [1,2,3,4], x = 4, y = 3
输出：false
输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true
输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth, x_parent, y_depth, y_parent = None, None, None, None

        #nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
        def dfs(root, parent, x, y, depth):
            nonlocal x_depth, x_parent, y_depth, y_parent
            if root is None:
                return

                # 判断 x, y 是否等于当前节点的值, 是的话更新 x 或者 y 的深度和parent
            if root.val == x:
                x_depth = depth
                x_parent = parent
            if root.val == y:
                y_depth = depth
                y_parent = parent

            dfs(root.left, root, x, y, depth + 1)
            dfs(root.right, root, x, y, depth + 1)

        dfs(root, None, x, y, 0)
        # 最后保证 x, y的深度一样, 但是parent节点不一样, 这样才是堂兄弟
        return x_depth == y_depth and x_parent != y_parent


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

print(Solution().isCousins(tree, 5,2))




