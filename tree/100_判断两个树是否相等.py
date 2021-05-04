# -*- coding:utf-8 -*-
#@Time : 2021-05-04 10:16
#@Author: zxf_要努力
#@File : 100_判断两个树是否相等.py
"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

输入：p = [1,2,3], q = [1,2,3]
输出：true

输入：p = [1,2], q = [1,null,2]
输出：false

输入：p = [1,2,1], q = [1,1,2]
输出：false
我自己想出的办法  层次遍历 每一个节点都进行判断  完整的考虑所有的条件
标准答案 深度优先遍历

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        queque_p = list()
        queque_p.append([p])
        queque_q = list()
        queque_q.append([q])
        while queque_p and queque_q:
            temp_p = list()
            temp_q = list()
            node_ps = queque_p.pop()
            node_qs = queque_q.pop()
            if len(node_ps) != len(node_qs):
                return False
            for node_p,node_q in zip(node_ps,node_qs):
                if node_p.val != node_q.val:
                    return False
                if node_p.left and not node_q.left:
                    return False
                if not node_p.left and node_q.left:
                    return False

                if node_p.left and node_q.left:
                    temp_p.append(node_p.left)
                    temp_q.append(node_q.left)
                if node_p.right and not node_q.right:
                    return False
                if not node_p.right and node_q.right:
                    return False
                if node_p.right and node_q.right:
                    temp_p.append(node_p.right)
                    temp_q.append(node_q.right)
            if len(temp_p) == len(temp_q) and len(temp_p) > 0:
                queque_p.append(temp_p)
                queque_q.append(temp_q)
        return True

    def dfsSameTree(self,p:TreeNode,q:TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.dfsSameTree(p.left,q.left) and self.dfsSameTree(p.right,q_right)



p = TreeNode(1)
p_left = TreeNode(2)
p_right = TreeNode(3)
p.left = p_left
p.right = p_right

q = TreeNode(1)
q_left = TreeNode(1)
q_right = TreeNode(2)
q.left = q_left
q.right = q_right

print(Solution().isSameTree(p, p))