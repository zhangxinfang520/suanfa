# -*- coding:utf-8 -*-
#@Time : 2021/8/30 10:51
#@Author: zxf_要努力
#@File : 337打家劫舍.py
'''
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

'''
from tree.create_tree_by_list import create_TreeNode_by_list

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not  root:
            return 0
        memo = dict()
        if root in memo.keys():
            return memo[root]
        #抢
        do_it = root.val + \
                (0 if root.left == None else self.rob(root.left.left)+self.rob(root.left.right)) + \
                (0 if root.right == None else self.rob(root.right.left)+self.rob(root.right.right))

        no_it = self.rob(root.left) + self.rob(root.right)

        res = max(do_it,no_it)
        memo[root] = res
        return res

    def rob1(self,root: TreeNode):

        '''
        arr[0] 表示不抢 root 的话，得到的最大钱数
        arr[1] 表示抢 root 的话，得到的最大钱数 */
        '''
        def dp(root):
            if not root:
                return [0,0]
            left = dp(root.left)
            right = dp(root.right)

            #抢
            rob = root.val + left[0] + right[0]
            #不抢
            no_rob = max(left[0],left[1]) + max(right[0],right[1])
            return [no_rob,rob]
        return max(dp(root))


if __name__ == '__main__':
    nums =  [3,4,5,1,3,None,1]
    root = create_TreeNode_by_list(nums)

    print(Solution().rob1(root))
