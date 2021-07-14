import torch
# from deform_dcn_CONV_V2 import DeformConv2d
#
# input = torch.randn(2,64,128,128).cuda()
# dcn = DeformConv2d(64,64,kernel_size=3,stride=1,padding=1).cuda()
# out = dcn(input)
#
# print(out.shape)

p = torch.tensor([[-1.5650,  2.0415, -0.1024, -0.5790]]
       )
print(p.shape)
print(p[:,::])
mean = torch.var_mean(p,dim=[0])[1]
print(mean)

class Solution:
    def isValidSudoku(self, board) :
        """

        :param board:
        :return:
        """
        row = len(board)
        col = len(board[0])

        for i in range(row):
               for j in range(col):
                      temp =board[i][j]
                      if temp ==".":
                             continue
                      if not self.is_valid(board,i,j,temp):
                             return False
        return True
    def is_valid(self,board,i,j,num,n=9):
           pass




