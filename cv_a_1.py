# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:29:37 2018

@author: godiva
"""

from cv_utils import *
import cv2
import numpy as np
import sys
import numba

if __name__ == '__main__':
    path = sys.argv[1]
    print("read image...")
    image = cv2.imread(path, 3)
    print("filter processing...")
    smooth = np.ones((3, 3), np.float32)/9
    edge = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    sharp = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    print("smoothing")
    cv2.imwrite("a_1_smooth.jpg", filter2d(image, smooth))
    print("edge")
    cv2.imwrite("a_1_edge.jpg", filter2d(image, edge))
    print("sharp")
    cv2.imwrite("a_1_sharp.jpg", filter2d(image, sharp))
    
    
