import os
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from pathlib import Path
import urllib.request

################################################################################
# Public Methods
################################################################################
def img2shapespace( dna, cell, options ):
    '''                   
    '''

    txtfilename = "input.txt"
    __options2txt(options,txtfilename)
    f = open(txtfilename,"a")

    #soham check that if
    # dna = [] or None
    # it gets written to disk as
    # dnaImageDirectoryPath = {};
    f.write("dnaImagesDirectoryPath = {")
    text = ""
    for name in dna:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)

    #soham do the same thing for cell
    f.write("cellImagesDirectoryPath = {")
    text = ""
    for name in cell:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)
    f.close()

    os.system("img2shapespace input.txt;rm input.txt")
    return None
