#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:59:48 2018

@author: jpcell
"""

from .ometiff import img2ometif
import numpy as np
from skimage import io


def test_valid_2D_file():
    filename = 'cell1.ome.tif'
    img = io.imread(filename)
    output_filename = 'test2D.ome.tif'
    assert img2ometif(img, output_filename) == True
    
def test_valid_3D_file():
    filename = 'cell3D00.ome.tif'
    img = io.imread(filename)
    output_filename = 'test3D.ome.tif'
    assert img2ometif(img, output_filename) == True

def test_empty_nparray():
    npArr = np.array([])
    output_filename = 'itShouldntExist.ome.tif'
    assert img2ometif(npArr, output_filename) == False