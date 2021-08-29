# -*- coding:utf-8 -*-
#@Time : 2021/8/29 15:49
#@Author: zxf_要努力
#@File : avgpool.py
import numpy as np
import torch

class AvgPool:

    def __init__(self,kernel_size=(2,2),stride=2):

        self.kernel_size = kernel_size
        self.w_height,self.w_width = kernel_size

        self.stride = stride

        self.in_height = None
        self.in_width = None

        self.out_height = None
        self.out_width = None

        self.x = None

    def __call__(self, x):
        
        self.x =  x
        self.in_height, self.in_width = x.shape
        self.out_height = int((self.in_height - self.w_height ) / self.stride) + 1
        self.out_width = int((self.in_width - self.w_width) / self.stride) + 1

        out = np.zeros((self.out_height,self.out_width))
        for i in range(self.out_height):
            for j in range(self.out_width):
                temp = x[i*self.stride:(i*self.stride+self.w_height),j*self.stride:(j*self.stride+self.w_height)]
                out[i,j] = temp.mean()
        return out

    def backward(self,d_loss):
        dx = np.zeros_like(self.x)

        for i in range(self.out_height):
            for j in range(self.out_width):
                dx[i * self.stride:(i * self.stride + self.w_height), j * self.stride:(j * self.stride + self.w_height)] = d_loss[i,j] /(self.w_height*self.w_width)
        return dx
    
if __name__ == '__main__':
    np.set_printoptions(precision=4)
    data_numpy = np.random.rand(1,1,6,8)
    data_tensor = torch.tensor(data_numpy,requires_grad=True)
    print(data_numpy.shape)
    print(data_tensor.shape)
    torch_avg = torch.nn.AvgPool2d((2,2),2)
    numpy_avg = AvgPool(kernel_size=(2,2),stride=2)

    out_tensor = torch_avg(data_tensor)
    out_numpy  = numpy_avg(data_numpy[0,0])
    print(out_tensor.shape)
    print(out_numpy.shape)

    loss_  = np.random.random(out_tensor.shape)
    loss_tensor  = torch.tensor(loss_,requires_grad=True)
    loss_numpy = loss_[0,0]

    out_tensor.backward(loss_tensor)

    print(numpy_avg.backward(loss_numpy))
    print(".............")
    print(data_tensor.grad)
