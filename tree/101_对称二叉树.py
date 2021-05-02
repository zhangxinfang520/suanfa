# -*- coding:utf-8 -*-
#@Time : 2021-05-02 13:37
#@Author: zxf_要努力
#@File : 101_对称二叉树.py
'''
给定一个二叉树，检查它是否是镜像对称的。
二叉树 [1,2,2,3,4,4,3] 是对称的。
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    本题思路 就是
    怎么判断一棵树是不是对称二叉树？
    答案：如果所给根节点，为空，那么是对称。如果不为空的话，当他的左子树与右子树对称时，他对称
    那么怎么知道左子树与右子树对不对称呢？
    答案：如果左树的左孩子与右树的右孩子对称，左树的右孩子与右树的左孩子对称，那么这个左树和右树就对称。
    '''
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def mid_order(left,right):
           if left is None and right is None:
               return True
           if left is None or right is None:
                return False
           return left.val == right.val and mid_order(left.left,right.right) and mid_order(left.right,right.left)

        return mid_order(root.left,root.right)


right_tree = TreeNode(2)
right_tree.right = TreeNode(3)
left_tree = TreeNode(2)
left_tree.right = TreeNode(3)

tree = TreeNode(1)
tree.left = left_tree
tree.right = right_tree

print(Solution().isSymmetric(tree))
#
# left_tree = TreeNode(7)
# left_tree.left = TreeNode(3)
# left_tree.right = BTree(4)
#
# right_tree = tree # 增加新的变量
# tree = BTree(18)
# tree.left = left_tree
# tree.right = right_tree