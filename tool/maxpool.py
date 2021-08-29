# -*- coding:utf-8 -*-
#@Time : 2021/8/29 11:40
#@Author: zxf_要努力
#@File : maxpool.py

import numpy as np

import torch


class MaxPool2d:
    
    def __init__(self,kernel_size=(2,2),stride=2):
        self.kernel_size = kernel_size
        self.w_height, self.w_width = kernel_size

        self.stride = stride
        self.x = None

        self.in_height = None
        self.in_width = None

        self.out_height = None
        self.out_width = None

        self.arg_max = None

    def __call__(self,x):
        self.x = x
        self.in_height,self.in_width = x.shape

        self.out_height = int((self.in_height - self.w_height) / self.stride) + 1
        self.out_width = int((self.in_width - self.w_width) / self.stride) + 1

        out = np.zeros((self.out_height,self.out_width))
        self.arg_max = np.zeros_like(out,dtype=np.int32)

        for i in range(self.out_height):
            for j in range(self.out_width):
                temp = x[i * self.stride :(i*self.stride + self.w_height), j*self.stride:(j*self.stride + self.w_width)]
                out[i,j] = np.max(temp)
                self.arg_max[i,j] = np.argmax(temp)
        self.arg_max = self.arg_max
        return out

    def backward(self,d_loss):
        dx = np.zeros_like(self.x)
        for i in range(self.out_height):
            for j in range(self.out_width):
                index = np.unravel_index(self.arg_max[i,j],self.kernel_size)
                dx[i * self.stride :(i*self.stride + self.w_height), j*self.stride:(j*self.stride + self.w_width)][index] = d_loss[i, j]  #

        return dx


if __name__ == '__main__':
    #控制小数点输出的个数
    np.set_printoptions(precision=4)
    np.random.seed(123)
    x_numpy = np.random.random((1,1,6,8))
    x_tensor = torch.tensor(x_numpy,requires_grad=True)
    max_pool_tensor = torch.nn.MaxPool2d((2,2),2)
    max_pool_numpy = MaxPool2d((2,2),2)


    out_tensor = max_pool_tensor(x_tensor)
    out_numpy = max_pool_numpy(x_numpy[0,0])
    print(out_tensor.shape)
    print(out_numpy.shape)

    #模拟损失
    d_loss_numpy = np.random.random(out_tensor.shape)
    d_loss_tensor = torch.tensor(d_loss_numpy,requires_grad=True)

    out_tensor.backward(d_loss_tensor)
    print(x_tensor.grad)

    dx_numpy = max_pool_numpy.backward(d_loss_numpy[0,0])
    print(dx_numpy)

    #print(x_tensor)
    #print(x_numpy[0,0].shape)



