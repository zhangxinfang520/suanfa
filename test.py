import torch
import math
# from deform_dcn_CONV_V2 import DeformConv2d
#
# input = torch.randn(2,64,128,128).cuda()
# dcn = DeformConv2d(64,64,kernel_size=3,stride=1,padding=1).cuda()
# out = dcn(input)
#
# print(out.shape)

# p = torch.tensor([[-1.5650,  2.0415, -0.1024, -0.5790]]
#        )
# print(p.shape)
# print(p[:,::])
# mean = torch.var_mean(p,dim=[0])[1]
# print(mean)

# input = torch.randn(2,3,512,512)
# #dal = torch.nn.Conv2d(3,64,3,1,0)
# dal = torch.nn.Conv2d(3,64,3,1,0,2)
#
# out = dal(input)
# print(out.shape)
# 
# a = 10
# b = 15
# out = math.gcd(a,b)
# print(out)

queque = [1,2,3,4,5,6]
for i in range(len(queque)):
    temp = queque[0]
    print(queque.pop(0))






