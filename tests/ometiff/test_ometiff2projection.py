#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:03:42 2018

@author: jpcell
"""

import numpy as np
from skimage import io
#from .ometiff import ometiff2array
#from .ometiff import get
from .ometiff import ometiff2projection


def test_valid_2D_file():
    filename = 'cell1.ome.tif'
    answer = ometiff2projection(filename)
    t = type(answer)
    assert (t == np.ndarray) == True

def test_valid_2D_array():
    filename = 'cell1.ome.tif'
    ioarr = io.imread(filename)
    arr_c = ioarr.shape[0]
    arr_y = ioarr.shape[1]
    arr_x = ioarr.shape[2]
    answer = ometiff2projection(filename)
    ans_y = answer.shape[0]
    ans_xc = answer.shape[1]
    assert arr_y == ans_y
    assert (arr_c*arr_x) == ans_xc


def test_valid_3D_file():
    filename = 'cell3D00.ome.tif'
    answer = ometiff2projection(filename)
    print(answer)
    t = type(answer)
    assert (t == np.ndarray) == True
    
def test_valid_3D_array():
    filename = 'cell3D00.ome.tif'
    ioarr = io.imread(filename)
    arr_c = ioarr.shape[0]
    arr_z = ioarr.shape[1]
    arr_y = ioarr.shape[2]
    arr_x = ioarr.shape[3]
    answer = ometiff2projection(filename)
    ans_yz = answer.shape[0]
    ans_xc = answer.shape[1]
    assert (arr_y*arr_z)  == ans_yz
    assert (arr_c*arr_x) == ans_xc

def test_invalid_file():
    filename = 'thisDoesntExist'
    assert ometiff2projection(filename) == None