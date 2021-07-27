# -*- coding:utf-8 -*-
#@Time : 2021-07-27 15:52
#@Author: zxf_要努力
#@File : NonLocalBlock.py
import torch
import torch.nn as nn

class  NonLocalBlock(nn.Module):
    def __init__(self,channel):
        super(NonLocalBlock, self).__init__()
        self.inter_channels = channel // 2
        self.conv_phi = nn.Conv2d(in_channels=channel,out_channels=self.inter_channels,
                                  kernel_size=1, stride=1,padding=0)
        self.conv_theta = nn.Conv2d(in_channels=channel,out_channels=self.inter_channels,
                                    kernel_size=1, stride=1, padding=0, bias=False)
        self.conv_g = nn.Conv2d(in_channels=channel,out_channels=self.inter_channels,
                                kernel_size=1, stride=1, padding=0, bias=False)
        self.softmax = nn.Softmax(dim=1)

        self.conv_mask = nn.Conv2d(in_channels=self.inter_channels, out_channels=channel,
                                   kernel_size=1, stride=1, padding=0, bias=False)

    def forward(self,x):
        # [N, C, H , W]
        b, c, h, w = x.size()
        # [N, C/2, H * W]
        x_phi = self.conv_phi(x).view(b, c, -1)
        # [N, H * W, C/2]
        x_theta = self.conv_theta(x).view(b, c, -1).permute(0,2,1).contiguous()
        x_g = self.conv_g(x).view(b, c, -1).permute(0, 2, 1).contiguous()
        # [N, H * W, H * W]
        mul_theta_phi = torch.matmul(x_theta, x_phi)
        mul_theta_phi = self.softmax(mul_theta_phi)
        # [N, H * W, C/2]
        mul_theta_phi_g = torch.matmul(mul_theta_phi, x_g)
        # [N, C/2, H, W]
        mul_theta_phi_g = mul_theta_phi_g.permute(0, 2, 1).contiguous().view(b, self.inter_channels, h, w)
        # [N, C, H , W]
        mask = self.conv_mask(mul_theta_phi_g)
        out = mask + x
        return out

x = torch.randn(3,256,32,32)
NLB = NonLocalBlock(256)
parm = sum([ x.numel() for x in NLB.parameters()])
print(parm)
out = NLB(x)
print(out.shape)
