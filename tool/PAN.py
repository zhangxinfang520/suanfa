# -*- coding:utf-8 -*-
#@Time : 2021-05-14 9:43
#@Author: zxf_要努力
#@File : PAN.py
import torch.nn as nn
'''模型的例子
if self.panet_buttomup:
    self.panet_buttomup_conv1_modules = nn.ModuleList()
    self.panet_buttomup_conv2_modules = nn.ModuleList()
    for i in range(self.num_backbone_stages - 1):
        if cfg.FPN.USE_GN:
            self.panet_buttomup_conv1_modules.append(nn.Sequential(
                nn.Conv2d(fpn_dim, fpn_dim, 3, 2, 1, bias=True),
                nn.GroupNorm(net_utils.get_group_gn(fpn_dim), fpn_dim,
                            eps=cfg.GROUP_NORM.EPSILON),
                nn.ReLU(inplace=True)
            ))
            self.panet_buttomup_conv2_modules.append(nn.Sequential(
                nn.Conv2d(fpn_dim, fpn_dim, 3, 1, 1, bias=True),
                nn.GroupNorm(net_utils.get_group_gn(fpn_dim), fpn_dim,
                            eps=cfg.GROUP_NORM.EPSILON),
                nn.ReLU(inplace=True)
            ))
        else:
            self.panet_buttomup_conv1_modules.append(
                nn.Conv2d(fpn_dim, fpn_dim, 3, 2, 1)
            )
            self.panet_buttomup_conv2_modules.append(
                nn.Conv2d(fpn_dim, fpn_dim, 3, 1, 1)
            )
'''
'''
torch的例子
'''
class PAN(nn.Module):
    def __init__(self, planes):
        super(PAN, self).__init__()
        self.P3_down = nn.Conv2d(planes,
                                 planes,
                                 kernel_size=3,
                                 stride=2,
                                 padding=1)
        self.P4_down = nn.Conv2d(planes,
                                 planes,
                                 kernel_size=3,
                                 stride=2,
                                 padding=1)
        self.P5_down = nn.Conv2d(planes,
                                 planes,
                                 kernel_size=3,
                                 stride=2,
                                 padding=1)
        self.P6_down = nn.Conv2d(planes,
                                 planes,
                                 kernel_size=3,
                                 stride=2,
                                 padding=1)

    def forward(self, inputs):
        [P3, P4, P5, P6, P7] = inputs

        P3_downsample = self.P3_down(P3)
        P4 = P3_downsample + P4

        P4_downsample = self.P4_down(P4)
        P5 = P4_downsample + P5

        P5_downsample = self.P5_down(P5)
        P6 = P5_downsample + P6

        P6_downsample = self.P6_down(P6)
        P7 = P6_downsample + P7

        del P3_downsample, P4_downsample, P5_downsample, P6_downsample

        return [P3, P4, P5, P6, P7]