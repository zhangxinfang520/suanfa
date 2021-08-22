# -*- coding:utf-8 -*-
#@Time : 2021/8/22 22:43
#@Author: zxf_要努力
#@File : GCT.py

import torch
import torch.nn as nn


class GCT(nn.Module):

    def __init__(self, learnable=False):
        super(GCT, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.learnable = learnable
        if self.learnable:
            self.c = nn.Parameter(torch.ones(1) * 0)
        else:
            self.c = 2

    def forward(self, x):
        residual = x
        b, c, h, w = x.shape
        attn = self.avg_pool(x).view(b, c)
        # norm
        attn = self.norm(attn)
        # gaussian function
        if self.learnable:
            attn = self.gaussian(attn, 3 * torch.sigmoid(self.c) + 1)
        else:
            attn = self.gaussian(attn, self.c)
        attn = attn.unsqueeze(-1).unsqueeze(-1)
        out = residual * attn
        return out

    @staticmethod
    def norm(x):
        mean = x.mean(dim=-1, keepdim=True).expand_as(x)
        std = x.std(dim=-1, keepdim=True).expand_as(x)
        rst = (x - mean) / std
        return rst

    @staticmethod
    def gaussian(x, c):
        return torch.exp(-(x ** 2) / (2 * c))
