# -*- coding:utf-8 -*-
#@Time : 2021-04-26 9:55
#@Author: zxf_要努力
#@File : CONV2D.py
import numpy as np


class my_conv(object):

    def __init__(self, input, kerenl_size, stride, padding="SAME"):
        self.input = np.asarray(input,np.float32)
        self.kerenl_size = np.asarray(kerenl_size,np.float32)
        self.stride = stride
        self.padding = padding

    def my_conv(self):
        [c,h,w] = self.input.shape
        [kc,k,_] = self.kerenl_size.shape
        pad_h = 0
        pad_w = 0
        res_h = 0
        res_w = 0
        assert kc == c
        if self.padding not in ["SAME","VALID","FULL"]:
            return
        if self.padding == 'SAME':
            pad_h = (self.stride*(h-1)+k-h)//2
            pad_w = (self.stride*(w-1)+k-w)//2
            res_h = h
            res_w = w
        elif self.padding == "VALID":
            pad_h = 0
            pad_w = 0
            res_h = (h-k)//self.stride + 1
            res_w = (w-k)//self.stride + 1
        elif self.padding == "FULL":
            pad_h = k-1
            pad_w = k-1
            res_h = (h-k+2*pad_h)//self.stride + 1
            res_w = (w-k+2*pad_w)//self.stride + 1

        fm_mat = np.zeros([c,h+2*pad_h,w+2*pad_w],dtype=np.float32)
        for i in range(c):
            fm_mat[i,pad_h:pad_h+h,pad_w:pad_w+w] = self.input[i]
        kernel_mat =self.kerenl_size
        kernel_mat.shape = (kc*k*k,1) # 转化为列向量
        # 将输入和卷积核转化为矩阵相乘的规格
        result_mat = np.zeros([res_h*res_w, kc*k*k],np.float32)
        row = 0
        for i in range(res_h):
            for j in range(res_w):
                temp = fm_mat[:,i*self.stride:(i*self.stride+k),
                                j*self.stride:(j*self.stride+k)]
                result_mat[row] = temp.flatten() #变为行向量
                row +=1
        res = np.dot(result_mat,kernel_mat).reshape((res_h,res_h))

        return res

if __name__ == '__main__':
    input_data = [
        [
            [1, 0, 1, 2, 1],
            [0, 2, 1, 0, 1],
            [1, 1, 0, 2, 0],
            [2, 2, 1, 1, 0],
            [2, 0, 1, 2, 0],
        ],
        [
            [2, 0, 2, 1, 1],
            [0, 1, 0, 0, 2],
            [1, 0, 0, 2, 1],
            [1, 1, 2, 1, 0],
            [1, 0, 1, 1, 1],

        ],
    ]
    kerenl_size = [
        [
            [1, 0, 1],
            [-1, 1, 0],
            [0, -1, 0],
        ],
        [
            [-1, 0, 1],
            [0, 0, 1],
            [1, 1, 1],
        ]
    ]
    conv = my_conv(input_data, kerenl_size, 1, "SAME")
    print(conv.my_conv())