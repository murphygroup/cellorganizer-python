#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:22:57 2018

@author: jpcell
"""

from .ometiff import ometiff2array
import numpy as np
from skimage import io

# File used: ome.tif generated from demo 2d00


# Map values


# Correct file - should return an array

def test_valid_file():
    filename = 'cell1.ome.tif'
    img = io.imread(filename)
    assert np.array_equal(ometiff2array(filename),img) == True

def test_npArray_notEmpty():
    filename = 'cell1.ome.tif'
    npArray = ometiff2array(filename)
    assert (npArray.size != 0) == True


def test_invalid_file():
    filename = 'lolIdontExist.ome.tif'
    assert ometiff2array(filename) == []
