# -*- coding:utf-8 -*-
#@Time : 2021/10/3 16:47
#@Author: zxf_要努力
#@File : transformer.py
import torch
import torch.nn as nn


class Transformer(nn.Module):

    def __init__(self,d_model=512,nhead=8,num_encoder_layer=6,num_decoder_layer=6,
                 dim_feedfoward=2048,dropout=0.1,activation="relu",normalization_before=False,
                 return_intermediate_dec=False):
        super(Transformer, self).__init__()
        