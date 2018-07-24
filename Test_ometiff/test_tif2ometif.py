#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:02:03 2018

@author: jpcell
"""

from .ometiff import tif2ometif


    
def test_valid_inputs():
    input_filename = "cell14/cell14_C<0-2>_T1_Z<0-19>.tif"
    output_filename = "cell14.ome.tif"
    assert tif2ometif(input_filename,output_filename) == True 
    
def test_invalid_inputs():
    input_filename = "IdontExist.tif"
    output_filename = "what.ome.tif"
    assert tif2ometif(input_filename,output_filename) == False