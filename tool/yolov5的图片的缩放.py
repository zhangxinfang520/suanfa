# -*- coding:utf-8 -*-
#@Time : 2021-05-24 14:29
#@Author: zxf_要努力
#@File : yolov5的图片的缩放.py

import numpy as np
import cv2


def letterbox(img, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleFill=False, scaleup=True, stride=32):
    # Resize and pad image while meeting stride-multiple constraints
    shape = img.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)

    # Scale ratio (new / old)
    #计算缩放因子
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    """
    缩放(resize)到输入大小img_size的时候，如果没有设置上采样的话，则只进行下采样
    因为上采样图片会让图片模糊，对训练不友好影响性能。
    """
    if not scaleup:  # only scale down, do not scale up (for better test mAP)
        r = min(r, 1.0)

    # Compute padding
    ratio = r, r  # width, height ratios
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
    if auto:  # minimum rectangle
        # 获取最小的矩形填充
        dw, dh = np.mod(dw, stride), np.mod(dh, stride)  # wh padding
    #  如果scaleFill=True,则不进行填充，直接resize成img_size,任由图片进行拉伸和压缩
    elif scaleFill:  # stretch
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape[1], new_shape[0])
        ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios
    #计算填充大小
    dw /= 2  # divide padding into 2 sides
    dh /= 2

    if shape[::-1] != new_unpad:  # resize
        img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    #进行填充
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
    return img, ratio, (dw, dh)

img = np.ones((800,600,3))
img, ratio, (dw, dh) = letterbox(img)
print(img.shape)
print(ratio)
print((dw,dh))