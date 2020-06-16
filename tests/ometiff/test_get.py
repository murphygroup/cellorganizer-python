#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:19:15 2018

@author: jpcell
"""

from .ometiff import get

# File used: ome.tif generated from demo 2d00


# Features

# None - empty string

def test_none_feature_2D():
    filename = 'cell1.ome.tif'
    feature = ''
    assert get(filename, feature) == None


# dimensionality - either '2D' or '3D' string
def test_dimensionality_feature_2D():
    filename = 'cell1.ome.tif'
    feature = 'dimensionality'
    assert get(filename, feature) == '2D'


# resolution - array [x,y] or [x, y, z] depending on dimensionality
def test_resolution_feature_2D():
    filename = 'cell1.ome.tif'
    feature = 'resolution'
    assert get(filename, feature) == [0.23, 0.23]

# size - array [x,y,z,c,t]
def test_size_feature_2D():
    filename = 'cell1.ome.tif'
    feature = 'size'
    assert get(filename, feature) == [757, 777,1,6,1]


# number of channel - number
def test_numChannels_feature_2D():
    filename = 'cell1.ome.tif'
    feature = 'number_of_channels'
    assert get(filename, feature) == 6



# number of timepoints - number
def test_numTime_feature_2D():
    filename = 'cell1.ome.tif'
    feature = 'number_of_timepoints'
    assert get(filename,feature) == 1
    

def test_none_feature_3D():
    filename = 'cell3D00.ome.tif'
    feature = ''
    assert get(filename, feature) == None


# dimensionality - either '2D' or '3D' string
def test_dimensionality_feature_3D():
    filename = 'cell3D00.ome.tif'
    feature = 'dimensionality'
    assert get(filename, feature) == '3D'


# resolution - array [x,y] or [x, y, z] depending on dimensionality
def test_resolution_feature_3D():
    filename = 'cell3D00.ome.tif'
    feature = 'resolution'
    assert get(filename, feature) == [0.049, 0.049,0.2]

# size - array [x,y,z,c,t]
def test_size_feature_3D():
    filename = 'cell3D00.ome.tif'
    feature = 'size'
    assert get(filename, feature) == [769, 459,10,3,1]


# number of channel - number
def test_numChannels_feature_3D():
    filename = 'cell3D00.ome.tif'
    feature = 'number_of_channels'
    assert get(filename, feature) == 3



# number of timepoints - number
def test_numTime_feature_3D():
    filename = 'cell3D00.ome.tif'
    feature = 'number_of_timepoints'
    assert get(filename,feature) == 1