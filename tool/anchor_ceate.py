# encoding: utf-8
"""
@author: zxf_要努力
@file: anchor_ceate.py
@time: 2022/5/10 13:24
"""
import torch
import cv2

torch.set_printoptions(2)  # 精简输出精度

def multibox_prior(data, sizes, ratios):
    """生成以每个像素为中心具有不同形状的锚框"""
    in_height, in_width = data.shape[-2:]
    device, num_sizes, num_ratios = data.device, len(sizes), len(ratios) # 3, 3

    #boxes_per_pixel = (num_sizes + num_ratios - 1) # 每个像素的锚框数
    boxes_per_pixel = (num_sizes * num_ratios) # 每个像素的锚框数
    size_tensor = torch.tensor(sizes, device=device) # list 转为 tensor
    ratio_tensor = torch.tensor(ratios, device=device)

    # 为了将锚点移动到像素的中心，需要设置偏移量。
    # 因为一个像素的的高为1且宽为1，我们选择偏移我们的中心0.5
    offset_h, offset_w = 0.5, 0.5
    steps_h = 1.0 / in_height  # 在y轴上缩放步长
    steps_w = 1.0 / in_width  # 在x轴上缩放步长

    # 生成锚框的所有中心点
    center_h = (torch.arange(in_height, device=device) + offset_h) * steps_h
    center_w = (torch.arange(in_width, device=device) + offset_w) * steps_w
    shift_y, shift_x = torch.meshgrid(center_h, center_w)

    # center_h：tensor([0.1250, 0.3750, 0.6250, 0.8750])
    # tensor([
    #       [0.1250, 0.1250, 0.1250, 0.1250],
    #       [0.3750, 0.3750, 0.3750, 0.3750],
    #       [0.6250, 0.6250, 0.6250, 0.6250],
    #       [0.8750, 0.8750, 0.8750, 0.8750]])

    # tensor([
    #       [0.1250, 0.3750, 0.6250, 0.8750],
    #       [0.1250, 0.3750, 0.6250, 0.8750],
    #       [0.1250, 0.3750, 0.6250, 0.8750],
    #       [0.1250, 0.3750, 0.6250, 0.8750]])
    shift_y, shift_x = shift_y.reshape(-1), shift_x.reshape(-1)
    # 全部每个像素中心点坐标
    # tensor([0.1250, 0.1250, 0.1250, 0.1250, 0.3750, 0.3750, 0.3750, 0.3750, 0.6250,
    #     0.6250, 0.6250, 0.6250, 0.8750, 0.8750, 0.8750, 0.8750])
    # tensor([0.1250, 0.3750, 0.6250, 0.8750, 0.1250, 0.3750, 0.6250, 0.8750, 0.1250,
    #     0.3750, 0.6250, 0.8750, 0.1250, 0.3750, 0.6250, 0.8750])

    # 生成“boxes_per_pixel”个高和宽，
    # 之后用于创建锚框的四角坐标(xmin,xmax,ymin,ymax)

    ## 动手学深度学习V2 原始代码
    # w = torch.cat((size_tensor * torch.sqrt(ratio_tensor[0]),
    #                sizes[0] * torch.sqrt(ratio_tensor[1:])))\
    #                * in_height / in_width  # 处理矩形输入
    # h = torch.cat((size_tensor / torch.sqrt(ratio_tensor[0]),
    #                sizes[0] / torch.sqrt(ratio_tensor[1:])))
    # # 除以2来获得半高和半宽
    # anchor_manipulations = torch.stack((-w, -h, w, h)).T.repeat(
    #                                     in_height * in_width, 1) / 2

    ## 更新后的代码
    w_0 = torch.cat((sizes[0] * torch.sqrt(in_height * ratio_tensor[:] / in_width),
                     size_tensor[1:] * torch.sqrt(in_height * ratio_tensor[0] / in_width)))
    h_0 = torch.cat((sizes[0] * torch.sqrt(in_width / ratio_tensor[:] / in_height),
                     size_tensor[1:] * torch.sqrt(in_width / ratio_tensor[0] / in_height)))
    # 除以2来获得半高和半宽
    anchor_manipulations = torch.stack((-w_0, -h_0, w_0, h_0)).T.repeat(
                                        in_height * in_width, 1) / 2

    # 每个中心点都将有“boxes_per_pixel”个锚框，
    # 所以生成含所有锚框中心的网格，重复了“boxes_per_pixel”次
    out_grid = torch.stack([shift_x, shift_y, shift_x, shift_y],
                dim=1).repeat_interleave(boxes_per_pixel, dim=0)
    output = out_grid + anchor_manipulations
    return output.unsqueeze(0)


img = cv2.imread('/Users/zhangxinfang/Desktop/a.jpg')
h, w = img.shape[:2]

print(h, w)
X = torch.rand(size=(1, 3, 4, 4))
Y = multibox_prior(X, sizes=[0.75, 0.5, 0.25], ratios=[1, 2, 0.5])
print(Y, Y.shape)