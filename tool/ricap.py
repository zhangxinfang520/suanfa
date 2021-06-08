# -*- coding:utf-8 -*-
#@Time : 2021-06-07 14:58
#@Author: zxf_要努力
#@File : Random image cropping and patching.py''
'''
andom image cropping and patching (RICAP)[7]方法随机裁剪四个图片的中部分，然后把它们拼接为一个图片，同时混合这四个图片的标签。
'''
#这里为一个样式
import numpy as np
import torch

beat = 0.3 #hyperparameter
train_loader = None
for (images,target) in train_loader:
    I_x,I_y = images.size()[2:]

    w = int(np.round(I_x * np.random.beta(beat,beat)))
    h = int(np.round(I_y * np.random.beta(beat,beat)))

    w_ = [w, I_x - w, w, I_x - w]
    h_ = [h, w, I_y - h, I_y - h]

    cropped_images = {}
    c_ = {}
    W_ = {}

    for k in range(4):
        index = torch.randperm(images.size(0))
        x_k = np.random.randint(0, I_x - w_[k] + 1)
        y_k = np.random.randint(0, I_y - h_[k] + 1)
        cropped_images[k] = images[index][:, :, x_k:x_k + w_[k], y_k:y_k + h_[k]]
        c_[k] = target[index].cuda()
        W_[k] = w_[k] * h_[k] / (I_x * I_y)

    patched_images = torch.cat(
        (torch.cat((cropped_images[0], cropped_images[1]), 2), torch.cat((cropped_images[2], cropped_images[3]), 2)), 3)