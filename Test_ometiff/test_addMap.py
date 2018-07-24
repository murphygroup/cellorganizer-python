#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:03:54 2018

@author: jpcell
"""

from .ometiff import add_map_annotation

# File used: ome.tif generated from demo 2d00


# Map values


# None - empty string

def test_empty_map():
    filename = 'cell.ome.tif'
    test_map = {}
    assert add_map_annotation(filename, test_map) == False


# One value inside the dictionary
def test_dict_single():
    filename = 'cell1.ome.tif'
    test_map = {'sizeX':0.048}
    assert add_map_annotation(filename, test_map) == True

# N-value inside the dictionary
def test_dict_multi():
    filename = 'cell2.ome.tif'
    test_map = {'sizeX':0.048,'sizeY':0.50}
    assert add_map_annotation(filename, test_map) == True