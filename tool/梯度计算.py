# encoding: utf-8
"""
@author: zxf_要努力
@file: 梯度计算.py
@time: 2022/4/10 15:57
"""
import torch


def save_gradient(module,grad_input,grad_output):
    print(f"{module.__class__.__name__} input grad:\n{grad_input}\n")
    print(f"{module.__class__.__name__} output grad:\n{grad_output}\n")

def save_forward_gradient(module,rad_input,grad_output):
    print(f"{module.__class__.__name__} output grad:\n{grad_output}\n")


def main():
    x = torch.reshape(torch.as_tensor([[1., 2., 3.],
                                      [1., 1., 2.],
                                      [2., 1., 2.]],dtype=torch.float32),
                      (1,1,3,3))

    x = torch.autograd.Variable(x, requires_grad=True)

    print(f"input\n{x}\n")

    conv_weight = torch.reshape(torch.as_tensor([1, 0, 1, 2], dtype=torch.float32), (1, 1, 2, 2))

    conv = torch.nn.Conv2d(1, 1, 2, bias=False)

    conv.load_state_dict({"weight": conv_weight})

    # 注册hook，捕获反向转播过程中流经该模块的梯度信息

    #handle1 = conv.register_full_backward_hook(save_gradient)
    handle1 = conv.register_forward_hook(save_forward_gradient)
    #handle1 = conv.register_backward_hook(save_backward_gradient)

    fc_weight = torch.reshape(torch.as_tensor([[0, 1, 0, 1],
                                               [1, 0, 1, 1]], dtype=torch.float32), (2, 4))
    fc = torch.nn.Linear(4, 2, bias=False)

    fc.load_state_dict({"weight":fc_weight})

    #前向传播
    o1 = conv(x)
    print(f"features map o1\n{o1}\n")

    flatten = torch.flatten(o1, start_dim=1)
    o2 = fc(flatten)
    print(f"feature map o2:\n{o2}\n")

    #反向更新
    o2[0][0].backward()

    print(f"input grad: \n{x.grad}\n")


    # release handles
    handle1.remove()

if __name__ == '__main__':
    main()

