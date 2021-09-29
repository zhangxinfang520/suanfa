# -*- coding:utf-8 -*-
#@Time : 2021/9/19 20:53
#@Author: zxf_要努力
#@File : ASPP.py

'''
ASPP 对所给定的输入以不同采样率的空洞卷积并行采样，相当于以多个比例捕捉图像的上下文
'''

import torch
import torch.nn as nn
import torch.nn.functional as F


class ASPP(nn.Module):
    def __init__(self,in_channels=512,depth=256):
        super(ASPP, self).__init__()
        self.mean = nn.AdaptiveAvgPool2d((1,1))
        self.conv = nn.Conv2d(in_channels,depth,1,1)
        self.asrous_block1 = nn.Conv2d(in_channels, depth, 1, 1)
        self.asrous_block6 = nn.Conv2d(in_channels, depth, 3, 1, padding=6, dilation=6)
        self.asrous_block12 = nn.Conv2d(in_channels, depth, 3, 1, padding=12, dilation=12)
        self.asrous_block18 = nn.Conv2d(in_channels, depth, 3, 1, padding=18, dilation=18)
        self.conv_1x1_output = nn.Conv2d(depth*5,depth,1,1)

    def forward(self,x):
        size = x.shape[2:]

        image_features = self.mean(x)
        image_features = self.conv(image_features)
        image_features = F.interpolate(image_features,size=size,mode="bilinear",align_corners=True)

        asrous_block1 = self.asrous_block1(x)
        asrous_block6 = self.asrous_block6(x)
        asrous_block12 = self.asrous_block12(x)
        asrous_block18 = self.asrous_block18(x)
        
        net = self.conv_1x1_output(torch.cat([image_features,asrous_block1,asrous_block6,
                                              asrous_block12,asrous_block18],dim=1))

        return net

if __name__ == '__main__':
    aspp = ASPP()
    x = torch.randn((3,512,24,24))
    out = aspp(x)
    print(out.shape)





