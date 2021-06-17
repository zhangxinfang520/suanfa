import torch

from deform_dcn_CONV_V2 import DeformConv2d

input = torch.randn(2,64,128,128).cuda()
dcn = DeformConv2d(64,64,kernel_size=3,stride=1,padding=1).cuda()
out = dcn(input)

print(out.shape)