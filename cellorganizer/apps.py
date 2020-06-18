import os
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from pathlib import Path
import urllib.request

################################################################################
# Public Methods
################################################################################
def img2slml(dim, dna, cell, protein, options):
    '''
    Trains a generative model of protein subcellular location from a
    collection of microscope images and saves the model as an SLML instance.

    An SLML model consists of four components,
    1) a (optional) documentation component
    2) a nuclear pattern model,
    3) a cell pattern model and,
    4) a protein pattern model.

    List Of Input Arguments     Descriptions
    -----------------------     ------------
    dimensionality              2D/3D
    dnaImagesDirectoryPath      DNA images collection directory
    cellImagesDirectoryPath     Cell images collection directory
    proteinImagesDirectoryPath  Protein images collection directory
    options                     Options structure
    '''

    txtfilename = "input.txt"
    __options2txt(options,txtfilename)
    f = open(txtfilename,"a")

    text = "dimensionality = '" + dim +"';\n"
    f.write(text)

    f.write("dnaImagesDirectoryPath = {")
    text = ""
    for name in dna:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)

    f.write("cellImagesDirectoryPath = {")
    text = ""
    for name in cell:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)

    text = ""
    f.write("proteinImagesDirectoryPath = {")

    for name in protein:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)
    f.close()

    os.system("img2slml input.txt;rm input.txt")
    return None
