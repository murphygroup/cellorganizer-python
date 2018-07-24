import os
from pathlib import Path
import subprocess
import numpy as np
from skimage import io

###################################################################################
def get(filename, feature):
    '''
    Return some specific infomation of an OME.TIFF.

    :param filename: name(path) of an valid OME.TIFF
    :type filename: string
    :param feature: string of the kind of info user want to get, containing "dimensionality", "resolution", "size", "number_of_channels", "number_of_timepoints"
    :type feature: string
    :rtype: string of information

    For example

    >>> info = cellorganizer.ometiff.get("cell1.ome.tif", "size")
    '''

    path = Path(filename)
    if not path.is_file():
        print("Invalid file path.")
        return ""
    commit = os.popen('tiffcomment ' + filename + '|xmlindent').read()

    # dimensionality feature
    if feature == "dimensionality":
        output = os.popen('showinf -novalid -nopix ' + filename +
                          ' | grep SizeZ | cut -d"=" -f2 ').read()
        output = int(output.replace("\n", "").replace(" ", ""))
        if output > 1:
            return "3D"
        elif output == 1:
            return "2D"
        print("The image doesn't have dimensionality information")
        return ""
    # resolution feature
    if feature == "resolution":
        res_x = commit[commit.find('"', commit.find('PhysicalSizeX=')):commit.find(' ', \
            commit.find('PhysicalSizeX='))]
        res_y = commit[commit.find('"', commit.find('PhysicalSizeY=')):commit.find(' ', \
            commit.find('PhysicalSizeY='))]
        res_x = float(res_x.replace('"', '').replace(" ", ""))
        res_y = float(res_y.replace('"', '').replace(" ", ""))

        res_z = ""
        if get(filename, "dimensionality") == "3D":
            res_z = commit[commit.find('"', commit.find('PhysicalSizeZ=')):commit.find(' ', \
                commit.find('PhysicalSizeZ='))]
            res_z = float(res_z.replace('"', '').replace(" ", ""))

        if res_z == '':
            return [res_x, res_y]
        return [res_x, res_y, res_z]

    # size feature
    if feature == "size":
        size_x = os.popen('showinf -novalid -nopix ' + filename + \
            ' | grep Width | cut -d"=" -f2').read()
        size_x = int(size_x.replace("\n", "").replace(" ", ""))
        size_y = os.popen('showinf -novalid -nopix ' + filename + \
            ' | grep Height | cut -d"=" -f2').read()
        size_y = int(size_y.replace("\n", "").replace(" ", ""))
        size_z = os.popen('showinf -novalid -nopix ' + filename + \
            ' | grep SizeZ | cut -d"=" -f2').read()
        size_z = int(size_z.replace("\n", "").replace(" ", ""))
        size_c = os.popen('showinf -novalid -nopix '+filename+' | grep SizeC | cut -d"=" -f2').read()
        size_c = int(size_c.replace("\n", "").replace(" ", ""))
        size_t = os.popen('showinf -novalid -nopix '+filename+' | grep SizeT | cut -d"=" -f2').read()
        size_t = int(size_t.replace("\n", "").replace(" ", ""))

        return [size_x, size_y, size_z, size_c, size_t]

	# number of channels feature
    if feature == "number_of_channels":
        size_c = os.popen('showinf -novalid -nopix ' + filename + ' | grep SizeC | cut -d"=" -f2').read()
        return int(size_c.replace("\n", "").replace(" ", ""))

    # number of timepoints feature
    if feature == "number_of_timepoints":
        size_t = os.popen('showinf -novalid -nopix ' + filename + ' | grep SizeT | cut -d"=" -f2').read()
        return int(size_t.replace("\n", "").replace(" ", ""))

################################################################################
def ometiff2array(filename):
    '''
    Returns an numpy array converted from an OME.TIFF

    :param filename: name(path) of an valid OME.TIFF
    :type filename: string
    :rtype: an n-dimensional numpy array corresponding to an image

    For example

    >>> img = cellorganizer.ometiff.ometiff2array("cell1.ome.tiff")
    '''
    try:
        img = io.imread(filename)
        return img
    except:
        print("Failed to get array from onetiff")
        return []


################################################################################
def ometiff2projection(filename, options={}):
    '''
    Returns a 2D numpy array corresponding to a projection translated from a 2D or 3D OME.TIFF

    :param filename: name(path) of an valid OME.TIFF
    :type filename: string
    :param options: options dictionary
    :type options: dictionary
    :rtype: an 2D numpy array corresponding to an projection

    For example

    >>> options = {key1:value, key2:value2}
    >>> proj = cellorganizer.ometiff.ometiff2projection("cell1.ome.tif", options)
    '''
    img = ometiff2array(filename)
    dim = get(filename, "dimensionality")
    output_img = []

    if dim in ('3D', '2D'):
        size_c = img.shape[0]
        for i in range(size_c):
            if dim == '2D':
                size_x = img.shape[2]
                size_y = img.shape[1]
                temp = img[i, :, :]

            else:
                size_x = img.shape[3]
                size_y = img.shape[2]
                size_z = img.shape[1]
                temp = img[i, :, :, :].reshape(size_y*size_z, size_x)

            if i == 0:
                output_img = temp
                continue

            output_img = np.concatenate((output_img, temp), axis=1)

        output_img = output_img.astype(np.uint8)
        return output_img

    else:
        print("There is an error in the OME.TIFF about dimensionality info.")
        return None

################################################################################
def add_map_annotation(filename, map={}, options={}):
    '''
    Adds an map annotation in OME.TIFF

    :param filename: name(path) of a valid OME.TIFF
    :type filename: string
    :param map: key/value map for map annotation
    :type map: dictionary
    :param options: options dictionary
    :type options: dictionary
    :rtype: true if the map annotation added in OME.TIFF successfully else false
    
    For example

    >>> map = {key1:value1,key2:value2}
    >>> output = celloragnizer.ometiff.add_map_annotation("cell1.ome.tif",map,{})
    '''

    # The funtion is uncompleted, the options dictionary will be cared about in the future
    # add a map annotation in metadata of the OME.TIFF

    if not map:
        print("Emepty map.")
        return False

    path = Path(filename)
    if not path.is_file():
        print("Invalid file path.")
        return False

    text_file = open("temp_key_value.txt", "w")
    keys = list(map.keys())
    text = ""
    for key in keys:
        text = text + key + " " + str(map[key]) + "\n"
    text_file.write(text)
    text_file.close()

    bash_command = 'bash run_MapAnnotation.sh ' + filename + ' temp.ome.tif'
    subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True).wait()
    path = Path('temp_key_value.txt')
    if path.is_file():
        os.system('rm temp_key_value.txt')
    path = Path('temp.ome.tif')
    if path.is_file():
        os.system('rm ' + filename)
        os.system('mv temp.ome.tif ' + filename)
    commit = os.popen('tiffcomment ' + filename + ';xmlvalid ' + filename).read()
    if "No validation errors found." in commit:
        return True
    return False

################################################################################
def tiff2ometiff(input_filename, output_filename, options={}):
    '''
    Converts a list of TIFF files or single TIFF into an OME.TIFF file. 

    If there is just one input file the input_filename can just be the name
    of input file. input file. 

    If there are a list of input files, this function requires input
    file have similar name. 
    
    The input_filename should be like 'LAM_cell2_<0-2>_t1.tif'. What should be in <> is continuous number.

    :param filename: regular expression
    :type filename:
    :param output_filename: name(path) of the output OME.TIFF file
    :type output_filename: string
    :param options: options dictionary
    :type options: string
    :rtpye: true if image constructed correctly, false otherwise

    For example

    >>> output = cellorganizer.ometiff.tiff2ometiff('LAM_cell2_<0-2>_t1.tif','test.ome.tif',{})
    '''

    # This function is not completed, the options dictionary(metadata) should be cared
    # about later

    # keys = options.keys()
    # if 'PhysicalSizeX' not in keys:
    #     print('PhysicalSizeX not set. Exiting method')
    #     return False

    # if 'PhysicalSizeY' not in keys:
    #     print('PhysicalSizeX not set. Exiting method')
    #     return False

    # if 'PhysicalSizeZ' not in keys:
    #     print('PhysicalSizeZ not set. Assuming you are attempting to create a 2D image')

    if "<" in input_filename:
        list_file_str = input_filename.split('/')
        list_file_str[-1] = "'" + list_file_str[-1] + "'"
        input_filename = '/'.join(list_file_str)

        command = "bfconvert -stitch " + input_filename + " " + output_filename
    else:
        path = Path(input_filename)
        if not path.is_file():
            return False
        command = 'bfconvert ' + input_filename + " " + output_filename

    subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).wait()

    path = Path(output_filename)
    if path.is_file():
        return True
    print("Invalid file path.")
    return False

################################################################################
def img2ometiff(arr_img, filename, options={}):
    '''
    Converts numpy n-dimensionary array into an OME.TIFF.

    :param arr_img: an array should be converted into OME.TIFF
    :type arr_img: numpy array
    :param filename: the output file name (path)
    :type filename: string
    :param options: Information should be added into the generated OME.TIFF
    :type options: dictionary
    :rtype: true if image constructed correctly, false otherwise

    For example

    >>> arr_img = numpy.random.random((8, 460, 460))
    >>> filename = "output.ome.tif"
    >>> options = {key1:value1, key2:value2}
    >>> output = cellorganizer.ometiff.img2ometiff(arr_img, filename, options)
    '''

    # This function is not completed, the options dictionary(metadata) should be cared
    # about later
    if arr_img.size == 0:
        return False
    io.imsave('test.tif', arr_img)
    os.system('bfconvert test.tif ' + filename)
    path = Path('test.tif')
    if path.is_file():
        os.system('rm test.tif')
    path = Path(filename)
    if path.is_file():
        return True
    print("The output file did not exsit.")
    return False
