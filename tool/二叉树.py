# -*- coding:utf-8 -*-
#@Time : 2021-04-26 16:05
#@Author: zxf_要努力
#@File : 二叉树.py
'''
Python实现了二叉树
'''
class BTree(object):

    def __init__(self,data=None,left=None,right=None):
        """

        :param data: 节点的值
        :param left: 左子树
        :param right: 右子树
        """
        self.data = data
        self.left = left
        self.right = right

    def preorder(self):
        '''前序遍历'''
        if self.data is not None:
            print(self.data,end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def midorder(self):
        '''中序遍历'''
        if self.left is not None:
            self.left.midorder()
        if self.data is not None:
            print(self.data,end=" ")
        if self.right is not  None:
            self.right.midorder()

    def postorder(self):
        '''后续遍历'''
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=" ")

    def levelorder(self):
        '''层次遍历'''
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None
        #层次遍历列表
        level_order = []
        if self.data is not None:
            level_order.append([self])

        height = self.height()
        if height >= 1:
            #对第二层及其以后的层数进行操作，在level_order中添加的节点而不是数据
            for _ in range(2,height+1):
                level = []
                for node in level_order[-1]:
                    #如果左孩子为非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    #如果右孩子为非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                #如果该层非空 就添加该层
                if level:
                    level_order.append(level)
            for i in range(0,height):
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].data

        return level_order

    def height(self):
        '''
        空树的高度为0，只有root节点的树高度为1
        :return:
        '''
        if self.data is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1+self.right.height()
        elif self.left is not None and self.right is None:
            return 1+self.left.height()
        else:
            return 1+max(self.left.height(),self.right.height())

    def leaves(self):
        if self.data is None:
            return None
        elif self.left is None and self.right is None:
            print(self.data,end='')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.left is not None and self.right is None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()




# 构造二叉树, BOTTOM-UP METHOD
right_tree = BTree(6)
right_tree.left = BTree(2)
right_tree.right = BTree(4)

left_tree = BTree(5)
left_tree.left = BTree(1)
left_tree.right = BTree(3)

tree = BTree(11)
tree.left = left_tree
tree.right = right_tree

left_tree = BTree(7)
left_tree.left = BTree(3)
left_tree.right = BTree(4)

right_tree = tree # 增加新的变量
tree = BTree(18)
tree.left = left_tree
tree.right = right_tree

print('先序遍历为:')
tree.preorder()
print()

print('中序遍历为:')
tree.midorder()
print()

print('后序遍历为:')
tree.postorder()
print()

print('层序遍历为:')
level_order = tree.levelorder()
print(level_order)
print()

height = tree.height()
print('树的高度为%s.' % height)

print('叶子节点为：')
tree.leaves()
print()
