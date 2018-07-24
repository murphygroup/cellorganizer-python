import os
import os.path
from pathlib import Path

def xmlvalid(filename):
    '''
    A command-line XML validation tool, useful for checking an OME-XML document for compliance with the OME-XML schema.

    :param filename: Path to an OME.TIF
    :type filename: string
    :rtype: boolean

    An example would be

    >>> filename = "img/test.ome.tif"
    >>> ans = xmlvalid(filename )
    '''

    # Check if it is a valid file, otherwise return
    path = Path(filename)

    if not path.is_file():
        print("Invalid file path.")
        return False

    # Execute the xmlvalid command and save it in a string

    xml_valid_str = os.popen('xmlvalid ' + filename).read()

    #print(xml_valid_str)

    # A correct xml interpretation will contain the strin 'No valid errors found'

    if 'No validation errors found' in xml_valid_str:
        return True

    return False

def tiffcomment(filename):
    '''
    Dumps the comment from the given TIFF file’s first IFD entry; useful for examining the OME-XML block in an OME-TIFF file.

    :param filename: Path to an OME.TIF
    :type filename: string
    :rtype: boolean

    An example of using this function would be

    >>> filename = 'img/test.ome.tif'
    >>> XML_String = tiffcomment(filename )
    '''

    # Check if it is a valid file, otherwise return

    path = Path(filename)

    if not path.is_file():
        print("Invalid file path.")
        return False

    # Execute and return the string with the comments

    comment = os.popen('tiffcomment '+filename).read()
    return comment

def xmlindent(filename):
    '''
    A simple XML prettifier similar to xmllint –format but more robust in that it attempts to produce output regardless of syntax errors in the XML.

    :param filename: Path to an OME.TIF
    :type filename: string

    An example of using this function would be

    >>> filename = 'img/test.ome.tif'
    >>> indentedXML_String = xmlindent(filename )
    '''

    # Check if it is a valid file, otherwise return
    path = Path(filename)

    if not path.is_file():
        print("Invalid file path.")
        return False

    # Execute and return a string with the comments indented properly
    comment = os.popen('tiffcomment '+filename + ' | xmlindent').read()

    return comment


def showinf(filename, **kwargs):
    '''
    Prints information about a given image file to the console, and displays the image itself in the Bio-Formats image viewer.


    :param filename: Path to an OME.TIF
    :type filename: string

    Examples for using the function

    >>> filename = 'img/test.ome.tif'
    >>> info = showinf(filename )

    or

    >>> filename = 'img/test.ome.tif'
    >>> testKwargs = {"-swap":"False", "-version":"True","-debug":"False"}
    >>> info = showinf(filename, **testKwargs )
    '''

    path = Path(filename)
    if not path.is_file():
        print("Invalid file path.")
        return False
    # temp_str = string to hold the instructions that will be called
    temp_str = "showinf "

    # traverse the dictionary to append the flags from the user to temp_str (Example, key: -debug, value: False)
    for key, value in kwargs.items():
        temp_str += key + " " + value + " "

    # finish the instructions with the filename
    temp_str += filename
    # call the instructions and save them as a string
    answer = os.popen(temp_str).read()
    return answer
