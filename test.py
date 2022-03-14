# -*- coding:utf-8 -*-
#@Time : 2021/8/26 19:13
#@Author: zxf_要努力
#@File : test.py

import numpy as np
import cv2

path = r"C:\Users\Lenovo\Desktop\23f3c52174a870202e67010b2408276.jpg"

img = cv2.imread(path,0)
edge = np.zeros((img.shape[0], img.shape[1]))
for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        # if (img[i,j]==255&img[i+1,j]==0)|(img[i,j]==255&img[i-1,j]==0):
        if (img[i, j] == 255 and img[i + 1, j] == 0) or (img[i, j] == 255 and img[i - 1, j] == 0):
            edge[i, j] = 255
        if (img[i, j] == 255 and img[i, j + 1] == 0) or (img[i, j] == 255 and img[i, j - 1] == 0):
            edge[i, j] = 255
cv2.imwrite("a.jpg", edge)
