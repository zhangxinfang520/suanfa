# -*- coding:utf-8 -*-
# @Time : 2021-05-16 14:56
# @Author: zxf_要努力
# @File : Label-smoothing.py
import torch
import torch.nn as nn

class LSR(nn.Module):

    def __init__(self,e=0.1,reduction='mean'):
        super(LSR, self).__init__()

        self.log_softmax = nn.LogSoftmax(dim=1)
        self.e = e
        self.reduction = reduction

    def _one_hot(self,labels:torch.tensor,classes,value=1):
        '''
        Convert labels to one hot vectors
        :param label: torch tensor in format [label1, label2, label3, ...]
        :param classes:int, number of classes
        :param value: label value in one hot vector, default to 1
        :return:
        return one hot format labels in shape [batchsize, classes]
        '''
        one_hot = torch.zeros(labels.size(),classes)
        ##labels and value_added  size must match
        labels = labels.view(labels.size(),-1)
        value_added = torch.Tensor(labels.size(0),1).fill_(value)

        value_added = value_added.to(labels.device)
        one_hot = one_hot.to(labels.device)
        one_hot.scatter_add_(1, labels, value_added)

        return one_hot

    def _smooth_label(self,target,lenght,smooth_factor):
        '''
        convert targets to one-hot format, and smooth
        :param target:target in form with [label1, label2, label_batchsize]
        :param lenght:length of one-hot format(number of classes)
        :param smooth_factor:smooth factor for label smooth
        :return:
        smoothed labels in one hot format
        '''
        one_hot = self._one_hot(target,lenght,value=1 - smooth_factor)
        one_hot +=smooth_factor / lenght
        return one_hot.to(target.device)
