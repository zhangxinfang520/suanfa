'''
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
输入：root = [3,9,20,null,null,15,7]
输出：true
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #自顶向下 遍历每一个节点都视为 根节点来遍历
        if not root:
            return True
        return abs(self.get_depth(root.left) - self.get_depth(root.right)) <= 1 and self.isBalanced(root.left) \
               and self.isBalanced(root.right)

    def get_depth(self,node):
        if not node:
            return 0
        left = self.get_depth(node.left)
        right = self.get_depth(node.right)
        return max(left,right)+1

    def isBalanced1(self, root: TreeNode) -> bool:
        #自下而上 有点后序遍历的味道
        if not  root:
            return 0
        left = self.isBalanced1(root.left)
        right = self.isBalanced1(root.right)

        if left == -1:return -1# 判断左子树是否平衡
        if right == -1:return -1# 判断右子树是否平衡
        if abs(left - right) < 2:
            return max(left,right) + 1
        else:
            return -1

