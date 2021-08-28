# -*- coding:utf-8 -*-
#@Time : 2021/8/24 20:32
#@Author: zxf_要努力
#@File : 交叉熵实现.py
'''实现交叉熵'''

import numpy as np
import torch
import torch.nn as nn

def CE(output,target):
    '''
    input ： list N 全都是大于等于0 小于1的小数
    target ：list N 0或者1
    '''
    q = np.array(output).reshape(-1,1)
    p = np.array(target).reshape(-1,1)
    res = -np.mean(np.nan_to_num(p*np.log(q)+(1-p)*np.log(1-q)))
    return round(res,3)

if __name__ == '__main__':
    input = [0.2,0.3,0.4,0.9]
    target = [1.,0.,1.,0.]
    print(CE(input,target))
    input = torch.as_tensor(input)
    target = torch.as_tensor(target)
    # input = torch.tensor(input,dtype=torch.float32).view(-1,1)
    # target = torch.tensor(target,dtype=torch.float32).view(-1,1)
    bc = nn.BCELoss()
    print(bc(input,target).numpy())
