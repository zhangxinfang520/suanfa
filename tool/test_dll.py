# -*- coding:utf-8 -*-
#@Time : 2021-06-16 9:32
#@Author: zxf_要努力
#@File : test_dll.py
import os
from  ctypes import *

os.chdir(r"F:\c++\cmake-build-debug")

dll_path = "libtest.dll"
dll = CDLL(dll_path)
dll.main1()