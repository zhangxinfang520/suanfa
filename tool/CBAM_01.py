# -*- coding:utf-8 -*-
#@Author: zxf_要努力
#@File : CBAM.py
import torch
import torch.nn as nn
import torch.nn.functional as F


class SpatialAttention(nn.Module):
    def __init__(self,kernel_size=7):
        super(SpatialAttention, self).__init__()
        assert kernel_size in (3,7), "kernel_size 不合理"
        padding = 3 if kernel_size == 7 else 1
        self.conv1 = nn.Conv2d(2,1,kernel_size,padding=padding,bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self,x):
        avg_out = torch.mean(x,dim=1,keepdim=True)
        max_out,_ = torch.max(x,dim=1,keepdim=True)
        x = torch.cat([avg_out,max_out],dim=1)
        x = self.conv1(x)
        return self.sigmoid(x)




if __name__ == '__main__':
    x = torch.randn(3,512,16,16)
    sae = SpatialAttention()
    parm = sum([x.numel() for x in sae.parameters()])
    print(parm)
    out = sae(x)
    x = out * x
    print(x.shape)
    print(out.shape)
