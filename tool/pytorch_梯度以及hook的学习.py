# -*- coding:utf-8 -*-
#@Time : 2021-08-10 10:40
#@Author: zxf_要努力
#@File : pytorch_梯度以及hook的学习.py
import torch
import torch.nn as nn

'''
backward(tensors, grad_tensors=None, retain_graph=None, create_graph=False, grad_variables=None)
    grad_tensors的作用其实可以简单地理解成在求梯度时的权重，因为可能不同值的梯度对结果影响程度不同，
    所以pytorch弄了个这种接口，而没有固定为全是1 
'''

#钩子函数
def res_hook(grad):
    print("grad:",grad)
    return grad

def grad_one_dim():
    ''' 梯度学习 单个维度学习'''
    x = torch.tensor(3.,requires_grad=True,device="cuda:0")
    y = torch.tensor(4.,requires_grad=True,device="cuda:0")
    #z为中间节点 梯度无法保存
    z = x ** 2
    out = z + y
    # 对于非叶子节点的
    z.register_hook(res_hook)
    z.retain_grad()
    #单个维度求解梯度
    out.backward()
    # 求解叶子节点梯度
    print(x.grad)
    print(y.grad)
    #如果使用 hook函数 z这个中间节点还是没有梯度 #但是对z使用retain_grad z 的梯度就会保留
    print(z.grad)

def grad_mul_dim():
    # x = [[1.,2.,3.],[4., 5., 6.]] x = [[a1,a2,a3],[a4, a5, a6]]
    #mat_z = [[a1*a1,a2*a2,a3*a3],[a4*a4, a5*a5, a6*a6]]
    #out = [
    # [a1*a1+a2*a2+a3*a3,a1*a1+a2*a2+a3*a3,a1*a1+a2*a2+a3*a3],
    # [a4*a4+a5*a5+a6*a6,a4*a4+a5*a5+a6*a6,a4*a4+a5*a5+a6*a6]
    # ]
    '''
    求out 对 x 求导 就是分别对 a1到 a6求导
    out.sum().backward()  相当于以a1 就是 out_1 = a1*a1+a2*a2+a3*a3 + a1*a1+a2*a2+a3*a3+a1*a1+a2*a2+a3*a3+... =
        3（a1*a1+a2*a2+a3*a3） + 3（a4*a4+a5*a5+a6*a6）
                                dout_1/da1 = 6a_1
    out.mean().backward() 相当于以a1 就是 out_1 = a1*a1+a2*a2+a3*a3 + a1*a1+a2*a2+a3*a3+a1*a1+a2*a2+a3*a3+... =
        （3（a1*a1+a2*a2+a3*a3） + 3（a4*a4+a5*a5+a6*a6）） / 6
                                dout_1/da1 = 6a_1 / 6 = a_1
    out.backward(torch.ones_like(out)) 相当于以a1 out = out * 1 然后
    '''

    #多维度的梯度的求解
    mat_x = torch.tensor([[1.,2.,3.],[4.,5.,6.]],requires_grad=True,device="cuda:0")
    mat_y = torch.ones((3,3),requires_grad=True,device="cuda:0")

    mat_z = mat_x ** 2
    out = mat_z @ mat_y

    #多维度的梯度求解

    mat_z.register_hook(res_hook)

    #不能直接使用 out.backward() 因为维度不一致 backward（）里面默认值为1
    #方法 1 out.sum().backward()/out.mean().backward()
    #out.sum().backward()
    #out.mean().backward()
    out.backward(torch.ones_like(out))
    print( out*torch.ones_like(out))
    print(mat_x.grad)




if __name__ == '__main__':
    #grad_one_dim()
    grad_mul_dim()