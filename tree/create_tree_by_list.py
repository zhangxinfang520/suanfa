# -*- coding:utf-8 -*-
#@Time : 2021-05-01 14:48
#@Author: zxf_要努力
#@File : 构建二叉树.py

"""
根据给定的数组构建二叉树
二叉树：[3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
"""
from typing import List


class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def create_TreeNode_by_list(node_list:List):
    i = 1
    # 将原数组拆成层次遍历的数组，每一项都储存这一层所有的节点的数据
    level_order = []
    # 防止越界
    sum = 1
    #每一层节点个为 2^i 如果在列表中表示的方式  [2^i-1:2^(i+1)-1] 列表中的下标表示 也可以换为下面的表示方式
    while sum < len(node_list):
        level_order.append(node_list[i-1:2*i-1])
        i *= 2
        sum += i
    #lever_order的格式 [[第一层的节点列表],[第二层的节点列表],[第三层的节点列表]]
    level_order.append(node_list[i-1:])# 这一个步骤是在最后一层添加剩余的节点 可能不是满二叉树

    def Create_TreeNode_One_Step_Up(TreeNode_list,forword_level):
        '''
        从上往下实例化节点并创建树
        :param TreeNode_list: 这一层所有的节点组成的列表
        :param forword_level: 上一层节点的数据组成的列表
        :return:
        '''
        #自己的理解 每一个不是叶子节点的节点 都和其子节点构成一棵树 然后都存在这个列表中
        new_TreeNode_list = []
        #i 是表示上一层和下一层节点的关系
        i = 0
        #现实实例化上一层的节点 然后创建与下一层节点的联系
        for elem in forword_level:
            if elem is not None:
                root = TreeNode(elem)
                if 2*i < len(TreeNode_list):
                    root.left = TreeNode_list[2*i]
                if (2*i +1) <len(TreeNode_list):
                    root.right = TreeNode_list[2*i+1]
                new_TreeNode_list.append(root)
                i +=1
            else:
                new_TreeNode_list.append(None)
                i += 1
        return new_TreeNode_list

    #如果只有一个节点
    if len(level_order) == 1:
        return TreeNode(level_order[0][0])
    else:
        #二叉树的层数大于1
        #这一步是叶子节点 只需初始化即可
        TreeNode_list = []
        for elem in level_order[-1]:
            if elem is None:
                TreeNode_list.append(None)
            else:
                TreeNode_list.append(TreeNode(elem))
        #从上往下创建二叉树
        for i in range(len(level_order)-2,-1,-1):
            TreeNode_list = Create_TreeNode_One_Step_Up(TreeNode_list,level_order[i])

        return TreeNode_list[0]

#树的遍历
#前序 递归遍历
def pre_order_recursion(root):
    res = []
    def pre(node:TreeNode):
        res.append(node.val)
        if node.left:
            pre(node.left)
        if node.right:
            pre(node.right)
    pre(root)
    return res

#前序非递归
def pre_order_norecursion(root):
    res = []
    if not root:
        return res
    stack_list = []
    stack_list.append(root)
    while stack_list:
        temp_node = stack_list.pop()
        res.append(temp_node.val)
        if temp_node.right:
            stack_list.append(temp_node.right)
        if temp_node.left:
            stack_list.append(temp_node.left)
    return res

#前序 递归遍历
def mid_order_recursion(root):
    res = []
    def mid(node:TreeNode):
        if node.left:
            mid(node.left)
        res.append(node.val)
        if node.right:
            mid(node.right)
    mid(root)
    return res

#中序非递归遍历
def mid_order_norecursion(root):
    res = []
    if not root:
        return res
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            temp_node = stack.pop()
            res.append(temp_node.val)
            root = temp_node.right
    return  res


#后序遍历
def post_order_recursion(root):
    res = []
    def post(node:TreeNode):
        if node.left:
            post(node.left)
        if node.right:
            post(node.right)
        res.append(node.val)
    post(root)
    return res

def post_order_norecursion(root):
    res = []
    if not root:
        return res
    stack = []
    while root or  stack:
        while root:
            stack.append(root)
            root = root.left if root.left else root.right
        temp_node = stack.pop()
        res.append(temp_node.val)
        if stack and stack[-1].left == temp_node:
            root = stack[-1].right
        else:
            root = None
    return res

def order_by_level(root):
    #对于层次遍历
    res = []
    if not root:
        return res
    queque_ = []
    queque_.append([root])
    while queque_:
        level_list = queque_.pop(0)
        temp_list = []
        for temp_node in level_list:
            if temp_node :
                res.append(temp_node.val)
                if temp_node.left:
                    temp_list.append(temp_node.left)
                if temp_node.right:
                    temp_list.append(temp_node.right)
        if len(temp_list) > 0:
            queque_.append(temp_list)
    return res



if __name__ == '__main__':
    # node_list = [3,9,20,6,3,15,7]
    node_list = [1, 2, 3, 8, 4, 5, None, None, 6, 7]
    root = create_TreeNode_by_list(node_list)
    print("前序递归遍历", pre_order_recursion(root))
    print("前序非递归遍历", pre_order_norecursion(root))
    print("中序递归遍历", mid_order_recursion(root))
    print("中序非递归遍历", mid_order_norecursion(root))
    print("后序递归遍历", post_order_recursion(root))
    print("后序非递归遍历", post_order_norecursion(root))
    print("层次遍历", order_by_level(root))