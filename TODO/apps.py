import os
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from pathlib import Path
import urllib.request
import cellorganizer.tools

################################################################################
# Public Methods
################################################################################
def img2shapespace( nuc, cellm, options ):
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
    for name in nuc:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)

    #soham do the same thing for cell
    f.write("cellImagesDirectoryPath = {")
    text = ""
    for name in cellm:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)
    f.close()

    os.system("img2shapespace input.txt;rm input.txt")
    return None

################################################################################
#Private Methods
################################################################################
def __options2txt(options,filename):
    if os.path.exists(filename):
        os.system('rm '+filename)
    f = open(filename,"w")
    keys = list(options.keys())
    keys.sort()
    for key in keys:
        if isinstance(options[key],str):
            if 'pwd' in options[key]:
                if options[key] == 'pwd':
                    text = 'options.'+key+' = '+ options[key]+";\n"
                else:
                    text =  'options.'+key+' = '+"["+ options[key]+"];\n"
            # if value is list or matrix
            elif options[key] == 'date':
                text = 'options.'+key+' = '+ options[key]+";\n"
            elif '[' in options[key]:
                text = 'options.'+key+' = '+ options[key]+";\n"
            # if value is a function
            elif '(' in options[key]:
                text = 'options.'+key+' = '+ options[key]+";\n"
            elif '{' in options[key]:
                text = 'options.'+key+' = '+ options[key]+";\n"
            else:
                text = 'options.'+key+' = '+ "'"+options[key]+"';\n"
        elif isinstance(options[key],bool):
            if options[key]:
                text = 'options.'+key+' = '+ 'true;\n'
            else:
                text = 'options.'+key+' = '+ 'false;\n'
        # if value is list
        elif isinstance(options[key],list):
            if len(options[key])<1:
                text = 'options.'+key+' = [];\n'
            else:
                if key == "masks":
                    text = 'options.'+key+' = {'
                else:
                    text = 'options.'+key+' = ['
                for element in options[key]:
                    # if element in list is str
                    if isinstance(element,str):
                        text = text + "'" + element + "',"
                    # if element in list is float, keep three decimal places
                    elif isinstance(element,float):
                        text = text + str('%.3f' % element) + ","
                    else:
                        text = text + str(element) + ","
                text = text[:-1]
                if key == "masks":
                    text = text+"};\n"
                else:
                    text = text+"];\n"

        elif isinstance(options[key],float):
            text = 'options.'+key+ ' = ' +str('%.3f' %  options[key])+';\n'
        else:
            text = 'options.'+key+ ' = ' +str(options[key])+';\n'
        f.write(text)
    f.close()
