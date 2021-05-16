# -*- coding:utf-8 -*-
#@Time : 2021-05-14 9:51
#@Author: zxf_要努力
#@File : mosaic.py
import os
import cv2
import torch
import numpy as np
import random
import math
from torch.utils.data import Dataset
from pycocotools.coco import COCO
import torch.nn.functional as F


class CocoDetection(Dataset):
    def __init__(self,
                 image_root_dir,
                 annotation_root_dir,
                 set='train2017',
                 use_mosaic=False,
                 transform=None):
        self.image_root_dir = image_root_dir
        self.annotation_root_dir = annotation_root_dir
        self.set_name = set
        self.use_mosaic = use_mosaic
        self.transform = transform

        self.coco = COCO(
            os.path.join(self.annotation_root_dir,
                         'instances_' + self.set_name + '.json'))

        self.load_classes()

    def load_classes(self):
        self.image_ids = self.coco.getImgIds()
        self.cat_ids = self.coco.getCatIds()
        self.categories = self.coco.loadCats(self.cat_ids)
        self.categories.sort(key=lambda x: x['id'])

        # category_id is an original id,coco_id is set from 0 to 79
        self.category_id_to_coco_label = {
            category['id']: i
            for i, category in enumerate(self.categories)
        }
        self.coco_label_to_category_id = {
            v: k
            for k, v in self.category_id_to_coco_label.items()
        }

    def __len__(self):
        return len(self.image_ids)

    def __getitem__(self, idx):
        if self.use_mosaic:
            if np.random.uniform(0, 1.)<0.5:
                imgs, annots = [], []
                img = self.load_image(idx)
                imgs.append(img)
                annot = self.load_annotations(idx)
                annots.append(annot)

                index_list, index = [idx], idx
                for _ in range(3):
                    while index in index_list:
                        index = np.random.randint(0, len(self.image_ids))
                    index_list.append(index)
                    img = self.load_image(index)
                    imgs.append(img)
                    annot = self.load_annotations(index)
                    annots.append(annot)

                # 第1，2，3，4张图片按顺时针方向排列，1为左上角图片，先计算出第2张图片的scale，然后推算出其他图片的最大resize尺寸，为了不让四张图片中某几张图片太小造成模型学习困难，scale限制为在0.25到0.75之间生成的随机浮点数。
                scale1 = np.random.uniform(0.2, 0.8)
                height1, width1, _ = imgs[0].shape

                imgs[0] = cv2.resize(imgs[0],
                                    (int(width1 * scale1), int(height1 * scale1)))

                max_height2, max_width2 = int(
                    height1 * scale1), width1 - int(width1 * scale1)
                height2, width2, _ = imgs[1].shape
                #判断缩放比
                #选取最大的缩放边
                scale2 = max_height2 / height2
                if int(scale2 * width2) > max_width2:
                    scale2 = max_width2 / width2
                imgs[1] = cv2.resize(imgs[1],
                                    (int(width2 * scale2), int(height2 * scale2)))

                max_height3, max_width3 = height1 - int(
                    height1 * scale1), width1 - int(width1 * scale1)
                height3, width3, _ = imgs[2].shape
                scale3 = max_height3 / height3
                if int(scale3 * width3) > max_width3:
                    scale3 = max_width3 / width3
                imgs[2] = cv2.resize(imgs[2],
                                    (int(width3 * scale3), int(height3 * scale3)))

                max_height4, max_width4 = height1 - int(height1 * scale1), int(
                    width1 * scale1)
                height4, width4, _ = imgs[3].shape
                scale4 = max_height4 / height4
                if int(scale4 * width4) > max_width4:
                    scale4 = max_width4 / width4
                imgs[3] = cv2.resize(imgs[3],
                                    (int(width4 * scale4), int(height4 * scale4)))

                # 最后图片大小和原图一样
                final_image = np.zeros((height1, width1, 3))
                final_image[0:int(height1 * scale1),
                            0:int(width1 * scale1)] = imgs[0]
                final_image[0:int(height2 * scale2),
                            int(width1 * scale1):(int(width1 * scale1) +
                                                int(width2 * scale2))] = imgs[1]
                final_image[int(height1 * scale1):(int(height1 * scale1) +
                                                int(height3 * scale3)),
                            int(width1 * scale1):(int(width1 * scale1) +
                                                int(width3 * scale3))] = imgs[2]
                final_image[int(height1 * scale1):(int(height1 * scale1) +
                                                int(height4 * scale4)),
                            0:int(width4 * scale4)] = imgs[3]

                annots[0][:, :4] *= scale1
                annots[1][:, :4] *= scale2
                annots[2][:, :4] *= scale3
                annots[3][:, :4] *= scale4

                annots[1][:, 0] += int(width1 * scale1)
                annots[1][:, 2] += int(width1 * scale1)

                annots[2][:, 0] += int(width1 * scale1)
                annots[2][:, 2] += int(width1 * scale1)
                annots[2][:, 1] += int(height1 * scale1)
                annots[2][:, 3] += int(height1 * scale1)

                annots[3][:, 1] += int(height1 * scale1)
                annots[3][:, 3] += int(height1 * scale1)

                final_annot = np.concatenate(
                    (annots[0], annots[1], annots[2], annots[3]), axis=0)

                sample = {'img': final_image, 'annot': final_annot, 'scale': 1.}
            else:
                img = self.load_image(idx)
                annot = self.load_annotations(idx)

                sample = {'img': img, 'annot': annot, 'scale': 1.}

        else:
            img = self.load_image(idx)
            annot = self.load_annotations(idx)

            sample = {'img': img, 'annot': annot, 'scale': 1.}

        if self.transform:
            sample = self.transform(sample)

        return sample

    def load_image(self, image_index):
        image_info = self.coco.loadImgs(self.image_ids[image_index])[0]
        path = os.path.join(self.image_root_dir, image_info['file_name'])
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        return img.astype(np.float32) / 255.

    def load_annotations(self, image_index):
        # get ground truth annotations
        annotations_ids = self.coco.getAnnIds(
            imgIds=self.image_ids[image_index], iscrowd=False)
        annotations = np.zeros((0, 5))

        # some images appear to miss annotations
        if len(annotations_ids) == 0:
            return annotations

        # parse annotations
        coco_annotations = self.coco.loadAnns(annotations_ids)
        for _, a in enumerate(coco_annotations):
            # some annotations have basically no width / height, skip them
            if a['bbox'][2] < 1 or a['bbox'][3] < 1:
                continue

            annotation = np.zeros((1, 5))
            annotation[0, :4] = a['bbox']
            annotation[0, 4] = self.find_coco_label_from_category_id(
                a['category_id'])

            annotations = np.append(annotations, annotation, axis=0)

        # transform from [x_min, y_min, w, h] to [x_min, y_min, x_max, y_max]
        annotations[:, 2] = annotations[:, 0] + annotations[:, 2]
        annotations[:, 3] = annotations[:, 1] + annotations[:, 3]

        return annotations

    def find_coco_label_from_category_id(self, category_id):
        return self.category_id_to_coco_label[category_id]

    def find_category_id_from_coco_label(self, coco_label):
        return self.coco_label_to_category_id[coco_label]

    def num_classes(self):
        return 80

    def image_aspect_ratio(self, image_index):
        image = self.coco.loadImgs(self.image_ids[image_index])[0]
        return float(image['width']) / float(image['height'])
