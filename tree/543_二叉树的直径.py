'''
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
这条路径可能穿过也可能不穿过根结点。
          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

'''
from tree.create_tree_by_list import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans,left+right+1)
            return  max(left,right) + 1
        hight = dfs(root)
        return self.ans -1


if __name__ == '__main__':
    node_list = [1,2,3,4,5,6,7,None,None,10,3,6]
    root = create_TreeNode_by_list(node_list)
    print(Solution().diameterOfBinaryTree(root))
    print(pre_order_recursion(root))
    print(mid_order_recursion(root))
    print(post_order_recursion(root))



