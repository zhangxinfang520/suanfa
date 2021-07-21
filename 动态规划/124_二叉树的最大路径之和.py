# -*- coding:utf-8 -*-
#@Time : 2021-07-21 20:49
#@Author: zxf_要努力
#@File : 124_二叉树的最大路径之和.py
'''
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径和 。
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

递归求解包含左孩子的以左孩子为根结点的最大路径和maxL，以及包含右孩子的以左孩子为根结点的最大路径和maxR。
如果maxL > 0，我们的当前的最大路径和就应该加上maxL。
如果maxR > 0，我们的当前的最大路径和就应该加上maxR。
最大路径和result取result和当前最大路径和的较大值。
该递归函数的返回结果应该是root的值，root的值加上maxL的值，root的值加上maxR的值，
这三者间的较大值。
时间复杂度和空间复杂度均为O(h)，其中h为树的高度。
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return
        self.result = float('-inf')
        def dfs(node):
            if not node:
                return 0
            #左子树的最大值
            left = max(0, dfs(node.left))
            #右子树最大值
            right = max(0, dfs(node.right))
            #左子树加右子树 加根节点
            lmr = node.val + max(0,left) + max(0,right)
            #根节点加 左右子树的最大值
            ret = node.val + max(0,max(left,right))
            #和全局最大值比较
            self.result = max(self.result, max(lmr,ret))
            #返回这一路的
            return ret
        dfs(root)
        return self.result

