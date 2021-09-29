# -*- coding:utf-8 -*-
#@Time : 2021/9/20 20:14
#@Author: zxf_要努力
#@File : 模型参数量.py
import thop

import torch
import torch.nn as nn


class testModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Conv2d(256,512,kernel_size=3,groups=1)

    def forward(self,x):
        return self.layers(x)


class testModel2(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Conv2d(256, 512, kernel_size=3, groups=2)

    def forward(self, x):
        return self.layers(x)


class testModel3(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Conv2d(256,512,kernel_size=3,groups=4)

    def forward(self, x):
        return self.layers(x)

if __name__ == '__main__':
    x = torch.randn(3,256,25,25)
    net_1 = testModel()
    net_2 = testModel2()
    net_3 = testModel3()

    print(thop.clever_format(thop.profile(net_1,(x,))))
    print(thop.clever_format(thop.profile(net_2,(x,))))
    print(thop.clever_format(thop.profile(net_3,(x,))))