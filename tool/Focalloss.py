# -*- coding:utf-8 -*-
#@Time : 2021-06-16 15:22
#@Author: zxf_要努力
#@File : Focalloss.py
'''
基于二分类交叉熵实现
'''

import numpy as np


import torch
import torch.nn as nn
import torch.nn.functional as F


class FocalLoss(nn.Module):

    def __init__(self,alpha=0.25,gamma=2,logits=False,reduce=False):
        super(FocalLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.logits = logits
        self.reduce = reduce

    def forward(self,inputs,targets):
        if self.logits:
            BCE_loss = F.binary_cross_entropy_with_logits(inputs,targets,reduction='none')
        else:
            BCE_loss = F.binary_cross_entropy(inputs,targets,reduction='none')

        pt = torch.exp(-BCE_loss)
        F_loss = self.alpha * (1-pt)**self.gamma * BCE_loss

        if self.reduce:
            return torch.mean(F_loss)
        else:
            return F_loss


class FocalLoss1(nn.Module):
    # Wraps focal loss around existing loss_fcn(), i.e. criteria = FocalLoss(nn.BCEWithLogitsLoss(), gamma=1.5)
    def __init__(self, loss_fcn, gamma=2, alpha=0.2):
        super(FocalLoss1, self).__init__()
        self.loss_fcn = loss_fcn  # must be nn.BCEWithLogitsLoss()
        self.gamma = gamma
        self.alpha = alpha
        self.reduction = loss_fcn.reduction
        self.loss_fcn.reduction = 'none'  # required to apply FL to each element

    def forward(self, pred, true):
        loss = self.loss_fcn(pred, true)
        #loss = F.binary_cross_entropy(pred, true,reduction='none')
        # p_t = torch.exp(-loss)
        # loss *= self.alpha * (1.000001 - p_t) ** self.gamma  # non-zero power for gradient stability

        # TF implementation https://github.com/tensorflow/addons/blob/v0.7.1/tensorflow_addons/losses/focal_loss.py
        pred_prob = torch.sigmoid(pred)  # prob from logits
        p_t = true * pred_prob + (1 - true) * (1 - pred_prob)
        alpha_factor = true * self.alpha + (1 - true) * (1 - self.alpha)
        modulating_factor = (1.0 - p_t) ** self.gamma
        loss *= alpha_factor * modulating_factor

        if self.reduction == 'mean':
            return loss.mean()
        elif self.reduction == 'sum':
            return loss.sum()
        else:  # 'none'
            return loss



loss = FocalLoss1(nn.BCELoss())
#loss = FocalLoss(reduce=True)

inputs = [[0.9,0.968],[0.1,0.032],
          [0.1,0.9]
          ]
inputs = np.array(inputs,dtype=np.float32)
inputs = torch.from_numpy(inputs)

# input = torch.randn((3, 2), requires_grad=True)
# input = torch.sigmoid(input)
# target = torch.rand((3, 2), requires_grad=False)
target = [[1,1],[0,0],[1,0]]
target = np.array(target,dtype=np.float32)
target = torch.from_numpy(target)
# ce_loss = F.binary_cross_entropy(inputs,target,reduction='none')
# print(ce_loss)
loss = loss(inputs,target)
print(loss)