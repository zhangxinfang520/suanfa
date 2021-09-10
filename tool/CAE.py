# -*- coding:utf-8 -*-
# @Time : 2021/9/10 10:40
# @Author: zxf_要努力
# @File : SAE.py
import torch
import torch.nn as nn


class SAE(nn.Module):
    def __init__(self, num_channels, reduction_ratio=2):
        super().__init__()
        num_channels_reduced = num_channels // reduction_ratio
        self.fc1 = nn.Linear(num_channels, num_channels_reduced, bias=True)
        self.fc2 = nn.Linear(num_channels_reduced, num_channels, bias=True)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        B, C, H, W = x.size()
        quezee_tensor = x.view(B, C, -1).mean(dim=2)
        fc1_out = self.relu(self.fc1(quezee_tensor))
        fc2_out = self.sigmoid(self.fc2(fc1_out))

        out = torch.mul(x, fc2_out.view(B, C, 1, 1))
        return out

if __name__ == '__main__':
    inputs = torch.rand(1,2,2,2)
    sae = SAE(2)
    out = sae(inputs)
    print(inputs==out)
    print(out.shape)
