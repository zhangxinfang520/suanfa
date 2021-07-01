# -*- coding:utf-8 -*-
#@Time : 2021-07-01 14:38
#@Author: zxf_要努力
#@File : ration_to_xyxyxyxy.py
import os
import xml.etree.ElementTree as ET
import math


def edit_xml(xml_file):
    """
    修改xml文件
    :param xml_file:xml文件的路径
    :return:
    """
    tree = ET.parse(xml_file)
    objs = tree.findall('object')
    for ix, obj in enumerate(objs):
        x0 = ET.Element("x0")  # 创建节点
        y0 = ET.Element("y0")
        x1 = ET.Element("x1")
        y1 = ET.Element("y1")
        x2 = ET.Element("x2")
        y2 = ET.Element("y2")
        x3 = ET.Element("x3")
        y3 = ET.Element("y3")
        obj_type = obj.find('type')
        type = obj_type.text
        print(xml_file)
        if type == 'bndbox':
            obj_bnd = obj.find('bndbox')
            obj_xmin = obj_bnd.find('xmin')
            obj_ymin = obj_bnd.find('ymin')
            obj_xmax = obj_bnd.find('xmax')
            obj_ymax = obj_bnd.find('ymax')
            xmin = float(obj_xmin.text)
            ymin = float(obj_ymin.text)
            xmax = float(obj_xmax.text)
            ymax = float(obj_ymax.text)
            obj_bnd.remove(obj_xmin)  # 删除节点
            obj_bnd.remove(obj_ymin)
            obj_bnd.remove(obj_xmax)
            obj_bnd.remove(obj_ymax)
            x0.text = str(xmin)
            y0.text = str(ymin)
            x1.text = str(xmax)
            y1.text = str(ymin)
            x2.text = str(xmin)
            y2.text = str(ymax)
            x3.text = str(xmax)
            y3.text = str(ymax)
        elif type == 'robndbox':
            obj_bnd = obj.find('robndbox')
            obj_bnd.tag = 'bndbox'   # 修改节点名
            obj_cx = obj_bnd.find('cx')
            obj_cy = obj_bnd.find('cy')
            obj_w = obj_bnd.find('w')
            obj_h = obj_bnd.find('h')
            obj_angle = obj_bnd.find('angle')
            cx = float(obj_cx.text)
            cy = float(obj_cy.text)
            w = float(obj_w.text)
            h = float(obj_h.text)
            angle = float(obj_angle.text)
            obj_bnd.remove(obj_cx)  # 删除节点
            obj_bnd.remove(obj_cy)
            obj_bnd.remove(obj_w)
            obj_bnd.remove(obj_h)
            obj_bnd.remove(obj_angle)

            x0.text, y0.text = rotatePoint(cx, cy, cx - w / 2, cy - h / 2, -angle)
            x1.text, y1.text = rotatePoint(cx, cy, cx + w / 2, cy - h / 2, -angle)
            x2.text, y2.text = rotatePoint(cx, cy, cx + w / 2, cy + h / 2, -angle)
            x3.text, y3.text = rotatePoint(cx, cy, cx - w / 2, cy + h / 2, -angle)

        obj.remove(obj_type)  # 删除节点
        obj_bnd.append(x0)    # 新增节点
        obj_bnd.append(y0)
        obj_bnd.append(x1)
        obj_bnd.append(y1)
        obj_bnd.append(x2)
        obj_bnd.append(y2)
        obj_bnd.append(x3)
        obj_bnd.append(y3)

        tree.write(xml_file, method='xml', encoding='utf-8')  # 更新xml文件

# 转换成四点坐标
def rotatePoint(xc, yc, xp, yp, theta):
    xoff = xp - xc;
    yoff = yp - yc;
    cosTheta = math.cos(theta)
    sinTheta = math.sin(theta)
    pResx = cosTheta * xoff + sinTheta * yoff
    pResy = - sinTheta * xoff + cosTheta * yoff
    return str(int(xc + pResx)), str(int(yc + pResy))

if __name__ == '__main__':
    # dir="E:/Projects/xmls_origin"
    # filelist = os.listdir(dir)
    # for file in filelist:r
    #     edit_xml(os.path.join(dir,file))
    edit_xml(r"C:\Users\lenovo\Desktop\recent_Tracker_development.xml")