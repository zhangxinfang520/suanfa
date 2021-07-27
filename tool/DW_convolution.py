# -*- coding:utf-8 -*-
#@Time : 2021-07-27 14:18
#@Author: zxf_要努力
#@File : DW_convolution.py
import torch
import torch.nn as nn
import torch.nn.functional as F


def _make_divisible(ch,divisor=8,min_ch=None):
    '''
    It ensures that all layers have a channel number that is divisible by 8
    :param ch:
    :param divisor:
    :param min_ch:
    :return:
    '''
    if min_ch is None:
        min_ch = divisor
    new_ch = max(min_ch,int(ch + divisor / 2)) // divisor * divisor
    if new_ch < 0.9 * ch:
        new_ch += divisor
    return new_ch

#SE 模块
class SqueezeExcitation(nn.Module):
    def __init__(self,input_c: int, squeeze_factor: int = 4):
        super(SqueezeExcitation, self).__init__()
        squeeze_c = _make_divisible(input_c // squeeze_factor, 8)
        self.fc1 = nn.Conv2d(input_c,squeeze_c,1)
        self.fc2 = nn.Conv2d(squeeze_c,input_c,1)

    def forward(self,x):
        scale = F.adaptive_avg_pool2d(x,output_size=(1,1))
        scale = self.fc1(scale)
        scale = F.relu(scale)
        scale = self.fc2(scale)
        scale = F.hardsigmoid(scale,inplace=True)
        return scale * x





class DW_convolution(nn.Module):
    def __init__(self, C_in, C_out, kernel_out, stride, padding, affine=True):
        super(DW_convolution, self).__init__()
        self.op = nn.Sequential(
            nn.Conv2d(C_in, C_in,kernel_size=kernel_out,stride=stride,padding=padding,bias=False),
            nn.Conv2d(C_in, C_out,kernel_size=1,padding=0,bias=False),
            nn.BatchNorm2d(C_out,eps=1e-5,affine=True)
        )
    
    def forward(self,x):
        return self.op(x)


class Conv2d(nn.Module):
    def __init__(self, C_in, C_out, kernel_out, stride, padding, affine=True):

        super(Conv2d, self).__init__()
        self.op = nn.Sequential(
            nn.Conv2d(C_in, C_out, kernel_size=kernel_out, stride=stride, padding=padding, bias=False),
            nn.BatchNorm2d(C_out, eps=1e-5, affine=True)
        )

    def forward(self, x):
        return self.op(x)
  
x = torch.randn(3,512,16,16)
dw = DW_convolution(512,1024,3,1,1)
cw = Conv2d(512,1024,3,1,1)

for idx, m in enumerate(dw.named_modules()):
    print(idx,m)

a = sum([x.numel() for x in dw.parameters()])
print(a)
b = sum([x.numel() for x in cw.parameters()])
print(b)

out_w = dw(x)
print(out_w.shape)
out_c = cw(x)
print(out_c.shape)


