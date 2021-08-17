'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：
   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
最开始想到的是 先遍历但是 [10,12,6,8,3,11] [10,12,6,8] 这一种特殊情况有问题
用递归
'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure1(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return  False
        res = []
        def dfs(node):
            res.append(node)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            return res
        res_A = dfs(A)
        res = []
        res_B = dfs(B)
        if len(res_B) > len(res_A):
            return False
        for i in range(len(res_A)):
            if res_A[i] == res_B[0]:
                if len(res_A) - i < len(res_B):
                    return False
                j, x = i, 0
                while x < len(res_B) and j < len(res_A):
                    if res_A[x] != res_B[j]:
                        break
                    else:
                        x += 1
                        j += 1
                return True

        return False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B: return False
        return self.isSameStructure(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)

    def isSameStructure(self,root,subroot):
        # root比subroot还早结束肯定不是
        if not root and  subroot:
            return False
        # root 还有
        if root and not subroot:
            return True
        #两者同时没有
        if not  root and not subroot:
            return True
        return root.val == subroot.val and self.isSameStructure(root.left, subroot.left) \
               and self.isSameStructure(root.right, subroot.right)

if __name__ == '__main__':
    res_A = [1, 0, -4, 3, 1]
    res_B = [1, -4]
    flag = False
    for i in range(len(res_A)):
        if res_A[i] == res_B[0]:
            if len(res_A) - i < len(res_B):
                flag = False
            j, x = i, 0
            while x < len(res_B) and j < len(res_A):
                if res_A[x] != res_B[j]:
                    break
                else:
                    x += 1
                    j += 1

    print(flag)



