# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:33:24 2018

@author: godiva
"""

import numpy as np
import numba

def conv(image, kernel):
    ret = np.zeros(3)
    ret[0] = (np.sum(image[0]*kernel)/kernel.shape[0])
    ret[1] = (np.sum(image[1]*kernel)/kernel.shape[0])
    ret[2] = (np.sum(image[2]*kernel)/kernel.shape[0])
    return ret

def padding(image):
    h, w = image.shape[:2]
    ret = np.zeros(h, w)
    ret[1:h-1, 1:w-1] = image
    return ret

def filter2d(image, kernel, fill_value=-1):
    win_h, win_w = kernel.shape   
    h, w = image.shape[:2]
    ret = np.zeros((h*w*3), np.float32)
    print(ret.shape)
    ret = ret.reshape(h,w,3)
    print(ret.shape)
    for y in range(h - win_h):
        for x in range(w - win_w):
            # 畳み込み演算
            ret[y,x] = conv(image[y:y+win_h, x:x+win_w], kernel)
    print(ret.shape)
    return ret
    
    
            