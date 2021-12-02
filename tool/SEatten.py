# -*- coding:utf-8 -*-
#@Time : 2021/12/2 15:52
#@Author: zxf_要努力
#@File : SEatten.py`
import torch
import torch.nn as nn


class SeAttention(nn.Module):
    def __init__(self, channel_num, r=4):
        """ Constructor
        """
        super(SeAttention, self).__init__()
        self.channel_num = channel_num
        self.r = r
        self.inter_channel = int(float(self.channel_num) / self.r)
        self.fc_e1 = torch.nn.Linear(channel_num, self.inter_channel)
        self.relu_e1 = nn.ReLU(inplace=True)
        self.fc_e2 = torch.nn.Linear(self.inter_channel, channel_num)

    def forward(self, x):
        y = torch.nn.functional.adaptive_avg_pool2d(x, (1, 1)).squeeze()
        y = self.fc_e1(y)
        y = self.relu_e1(y)
        y = self.fc_e2(y)
        y = torch.sigmoid(y).unsqueeze(-1).unsqueeze(-1)
        return x * y