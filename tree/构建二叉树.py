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


class BTree():
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def create_BTree_by_list(node_list:List):
    i = 1
    # 将原数组拆成层次遍历的数组，每一项都储存这一层所有的节点的数据
    level_order = []
    # 防止越界
    sum = 1
    #每一层节点个为 2^i 如果在列表中表示的方式  [2^i-1:2^(i+1)-1] 列表中的下标表示 也可以换为下面的表示方式
    while sum < len(node_list):
        level_order.append(node_list[i-1:2*i-1])
        i *=2
        sum +=i
    #lever_order的格式 [[第一层的节点列表],[第二层的节点列表],[第三层的节点列表]]
    level_order.append(node_list[i-1:])# 这一个步骤是在最后一层添加剩余的节点 可能不是满二叉树

    def Create_BTree_One_Step_Up(BTree_list,forword_level):
        '''
        从上往下实例化节点并创建树
        :param BTree_list: 这一层所有的节点组成的列表
        :param forword_level: 上一层节点的数据组成的列表
        :return:
        '''
        #自己的理解 每一个不是叶子节点的节点 都和其子节点构成一棵树 然后都存在这个列表中
        new_BTree_list = []
        #i 是表示上一层和下一层节点的关系
        i = 0
        #现实实例化上一层的节点 然后创建与下一层节点的联系
        for elem in forword_level:
            root = BTree(elem)
            if 2*i < len(BTree_list):
                root.left = BTree_list[2*i]
            if 2*i +1 <len(BTree_list):
                root.right = BTree_list[2*i+1]
            new_BTree_list.append(root)
            i +=1

        return new_BTree_list

    #如果只有一个节点
    if len(level_order) == 1:
        return BTree(level_order[0][0])
    else:
        #二叉树的层数大于1
        #这一步是叶子节点 只需初始化即可
        BTree_list = [BTree(elem) for elem in level_order[-1]]
        #从上往下创建二叉树
        for i in range(len(level_order)-2,-1,-1):
            BTree_list = Create_BTree_One_Step_Up(BTree_list,level_order[i])

        return BTree_list[0]


node_list = [3,9,20,6,3,15,7]
create_BTree_by_list(node_list)