# -*- coding:utf-8 -*-
#@Time : 2021/9/2 12:37
#@Author: zxf_要努力
#@File : Dropout.py

import numpy as np


class Dropout:

    def __init__(self,p):
        #保留比例
        self.p = p

    def __call__(self,X,mode):
        '''
        @param X:
        @param mode: train or test
        @return:
        '''
        return self.forward(X,mode)

    def forward(self,X,mode):
        if mode == 'train':
            self.mask = np.random.binomial(1,self.p,X.shape) / (1-self.p)
            out = self.mask * X
        else:
            out = X
        return out

    def backward(self, d_out):
        return d_out * self.mask

if __name__ == '__main__':
    dropout = Dropout(0.5)
    X = np.random.randn(1,10)
    print(X)
    out = dropout(X,'train')
    print(out)
