import os
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from pathlib import Path
import urllib.request
import requests


################################################################################
# Public Methods
################################################################################
def image2SPHARMparameterization(image_path, options):

    txtfilename = "input.txt"
    __options2txt(options, txtfilename)
    f = open(txtfilename, "a")

    #write path to image for matlab to be able to read
    text = "image_path = '" + image_path + "';\n"
    f.write(text)
    f.close()

    os.system("image2SPHARMparameterization input.txt; rm input.txt")
    #checking if file exists
    answer = os.path.isfile(options['output_filepath'])

    return answer

#########################################git s#######################################
def SPHARMparameterization2image(model_path, options):

    txtfilename = "input.txt"
    __options2txt(options, txtfilename)
    f = open(txtfilename, "a")

    #write path to model for matlab to be able to read
    text = "model_path = '" + model_path + "';\n"
    f.write(text)
    f.close()

    os.system("SPHARMparameterization2image input.txt; rm input.txt")
    #checking if file exists
    answer = os.path.isfile(options['output_filepath'])
    return answer

################################################################################
def SPHARMparameterization2mesh(model_path, options):

    txtfilename = "input.txt"
    __options2txt(options, txtfilename)
    f = open(txtfilename, "a")

    #write path to model for matlab to be able to read
    text = "model_path = '" + model_path + "';\n"
    f.write(text)
    f.close()

    os.system("SPHARMparameterization2mesh input.txt; rm input.txt")
    #checking if file exists
    answer = os.path.isfile(options['output_filepath'])
    return answer

################################################################################
def newfunc3():
    pass

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
    __options2txt(options, txtfilename)
    f = open(txtfilename, "a")

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
    # checking if the model file is generated
    answer = os.path.isfile(options['model.filename'])
    return answer

################################################################################
def slml2img(filenames, options):
    '''
    Synthesizes an image from a list of SLML models.

    Instances may be saved in the following forms:
    a) tiff stacks: a 3D tiff image stack for each pattern generated using the input models
    b) indexed images: a single 3D tiff image stack where each pattern is represented by a number 1-n
    c) object mesh: a .obj mesh file for each pattern generated using the input models (blenderfile option)
    d) SBML-Spatial file: a Systems Biology Markup Language (SBML) instance XML file utilizing the Spatial extension in level 3 version 1

    List Of Input Arguments  Descriptions
    -----------------------  ------------
    models                   A cell array of filenames
    options                  A structure holding the function options

    '''

    __options2txt(options,"input.txt")
    f = open("input.txt","a")
    f.write("filenames = {")
    text = ""
    for name in filenames:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)
    f.close()

    os.system("slml2img input.txt;rm input.txt")
    return None

################################################################################
def slml2info(filenames, options):
    '''
    Generate a report from information extracted from a genearative model file

    List Of Input Arguments  Descriptions
    -----------------------  ------------
    filename                 Model filename
    options                  Options structure
    '''

    txtfilename = 'input.txt'
    __options2txt(options,"input.txt")
    f = open("input.txt","a")
    f.write("files = {")
    text = ""
    for name in filenames:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)
    f.close()

    os.system('slml2info input.txt; rm input.txt')
    if os.path.exists('report'):
        os.system('mv ./report/* .')
        os.system('rm -rf ./report')
        return True
    else:
        return False

################################################################################
def slml2slml(files, options):
    '''
    SLML2SLML Combines multiple SLML files into a single model file.

    List Of Input Arguments     Descriptions
    -----------------------     ------------
    files                       list of paths of models need be combined
    options                     Options structure

    The input argument options holds the valid parameters for these components.
    The shape of options is described below

    List Of Parameters        Descriptions
    ------------------        ------------
    output_filename           (optional)the file name of output model,
                               default is "model.mat"
    '''

    __options2txt(options,"input.txt")
    f = open("input.txt","a")
    f.write("files = {")
    text = ""
    for name in files:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)
    f.close()

    os.system("slml2slml input.txt;rm input.txt")

    return None

################################################################################
def slml2report(model1_filename, model2_filename, options):
    '''
    Generate a report comparing two SLML generative models

    List Of Input Arguments  Descriptions
    -----------------------  ------------
    model1                   A generative model filename
    model2                   A generative model filename

    Example
    > model1_filename = '/path/to/model/model1.mat';
    > model2_filename = '/path/to/model/model2.mat';
    > options
    answer = slml2report( filename1, filename2, options );
    '''

    txtfilename = "input.txt"
    __options2txt(options,txtfilename)

    f = open(txtfilename,"a")
    f.write("model1_filename = " + "'" + model1_filename + "';\n")
    f.write("model2_filename = " + "'" + model2_filename + "';\n")
    f.close()

    os.system("slml2report input.txt;rm input.txt")

    # need to copy everything out of report folder to current working directory
    if os.path.exists('report'):
        os.system('mv ./report/* .')
        os.system('rm -rf ./report')
        return True
    else:
        return False

#######################################################################
def imshow(img_path, options):
    '''
    Show your output image in the notebook

    List Of Input Arguments  Descriptions
    -----------------------  ------------
    img_path                 filename of image
    '''

    img_file = Path(img_path)
    if img_file.is_file():
        img = plt.imread(img_path)
        plt.imshow(img)
        plt.show()
    else:
        print('Invalid file path.')

################################################################################
def get_model_files():
    '''
    Helper function that downloads models from the Murphy Lab's website.
    '''

    url = 'http://www.cellorganizer.org/Downloads/latest/docker/models.tgz'
    print('Retrieving ' + url)
    if __does_file_exist(url):
        if not os.path.exists('/home/murphylab/cellorganizer/local/models/'):
            print('Creating directory /home/murphylab/cellorganizer/local/models/')
            os.mkdir('/home/murphylab/cellorganizer/local/models/')

        urllib.request.urlretrieve( url, 'models.tgz' )
        print( 'Extracting models' )
        os.system('tar -C /home/murphylab/cellorganizer/local/ --keep-old-files -xvf models.tgz')
        os.system('rm -fv models.tgz')
        print('Fetched all models...')
        return True
    else:
        print('Unable to find model files. Check later.')
        return False

################################################################################
def download_latest_notebooks():
    '''
    Helper function that downloads the latest notebooks from the Murphy Lab's GitHub repository.
    '''

    url = 'https://github.com/murphygroup/cellorganizer-jupyter-notebooks/archive/master.zip'
    print('Retrieving ' + url)
    if __does_file_exist(url):
        if not os.path.exists('/home/murphylab/cellorganizer/local/notebooks/'):
            print('Creating directory /home/murphylab/cellorganizer/local/notebooks/')
            os.mkdir('/home/murphylab/cellorganizer/local/notebooks/')

        urllib.request.urlretrieve(url, '/home/murphylab/cellorganizer/local/master.zip')
        print('Extracting notebooks...')
        os.system('unzip /home/murphylab/cellorganizer/local/master.zip -d /home/murphylab/cellorganizer/local/')
        os.remove('/home/murphylab/cellorganizer/local/master.zip')
        print('Extracting notebooks done.')
        os.system('mv /home/murphylab/cellorganizer/local/cellorganizer-jupyter-notebooks-master/demo_notebooks/ /home/murphylab/cellorganizer/local/notebooks/.')
        os.system('mv /home/murphylab/cellorganizer/local/cellorganizer-jupyter-notebooks-master/workshop_demos/ /home/murphylab/cellorganizer/local/notebooks/.')
        os.system('mv /home/murphylab/cellorganizer/local/cellorganizer-jupyter-notebooks-master/helper_notebooks/ /home/murphylab/cellorganizer/local/notebooks/.')
        os.system('rm -rf /home/murphylab/cellorganizer/local/cellorganizer-jupyter-notebooks-master')
        print('Fetched all notebooks...')
        return True
    else:
        print('Unable to download notebooks at this time. Try again later.')
        return False

################################################################################
def get_image_collection():
    '''
    Helper function that downloads Murphy Lab's image collection used
    by CellOrganizer for model creation and demonstrations.
    '''

    # url = 'http://www.cellorganizer.org/Downloads/latest/docker/images.zip'
    url = 'http://www.andrew.cmu.edu/~icaoberg/mmbios-images.zip'

    target_path = "/home/murphylab/cellorganizer/local/mmbios-images.zip"
    print('Retrieving ' + url)
    if __does_file_exist(url):
        if not os.path.exists('/home/murphylab/cellorganizer/local/images/'):
            print('Creating directory /home/murphylab/cellorganizer/local/images/')
            os.mkdir('/home/murphylab/cellorganizer/local/images/')

            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(target_path, 'wb') as f:
                    f.write(response.raw.read())

            print("Extracting image files .....")
            os.system('unzip /home/murphylab/cellorganizer/local/mmbios-images.zip -d /home/murphylab/cellorganizer/local/')
            os.remove('/home/murphylab/cellorganizer/local/mmbios-images.zip')
            print('Fetched all images...')
            return True
        else:
            print('Image collection is already present. Skipping download.')
            return False
    else:
        print('Unable to download images at this time. Try again later.')
        return False

################################################################################
def load( matfile ):
    '''
    Loads a Matlab file into the workspace as a dictionary.
    '''

    model=__mat2python(matfile)
    return model

################################################################################
def save( model, filename="model.mat" ):
    '''
    Saves model into a Matlab mat-file.
    '''

    answer = __shallowdict2mat(model, filename)
    return answer

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

################################################################################
# The input is shallow model dictionary
def __shallowdict2mat(model, filename="model.mat"):
    tem_dic = {}
    #put each element into the fixed dictionary
    for key,value in model.items():
        Key_list = key.split('.')
        if len(Key_list)>1:
            point = tem_dic
            for i in range(len(Key_list)-1):
                if Key_list[i] in point.keys():
                    point = point[Key_list[i]]
                else:
                    point[Key_list[i]] = {}
                    point = point[Key_list[i]]

            point[Key_list[len(Key_list)-1]] = value
        else:
            tem_dic.update({key:value})

    scipy.io.savemat(filename, mdict={'model': tem_dic})
    return True

################################################################################
def __mat2numpy(matfile,savefile,parameter=None):
	'''
	mat2numpy reads a .mat file which contains a struct representing a model and save it as a numpy file
	@param matfile: a valid string of matfile in the disk
	@param savefile: the name of the numpy file needed to be saved
	'''

	model=__mat2python(matfile)
	if (model=={}):
		print("Empty matfile")
		return False
	if type(savefile)!=str:
		print("__mat2numpy: input savefile must be a string")
		return False
	try:
		np.save(savefile,model)
		return True
	except:
		print("__mat2numpy:Can't save the numpy file")
		return False

################################################################################
def __mat2python(matfile,parameter=None):
	'''
	__mat2python reads a .mat file which contains a struct representing a model and returns a dictionary corresponding to the matlab struct
	@param matfile: a string which represend a valid matfile in the disk
	'''

	if type(matfile)!=str:
		print("__mat2python: input matfile has to be a string")
		return {}
	if not os.path.isfile(matfile):
		print("__mat2python: matfile: "+matfile+" does not exsist")
		return {}
	if not matfile.endswith('.mat'):
		print("__mat2python: matfile: "+matfile+" is not a valid .mat format")
		return {}
	try:
		model=scipy.io.loadmat(matfile,squeeze_me=True,struct_as_record=False)
	except:
		print("__mat2python: can't load "+matfile)
		return {}
	for key in model:
		if "__" not in key:
			return __convert(model[key])

################################################################################
def __convert(model):
	'''
	__convert is a helper method that recursively turns a  mat_struct to dictionary
	@param: model: a mat_struct defined by scipy.io.matlab
	'''

	if type(model)!=scipy.io.matlab.mio5_params.mat_struct:
		if type(model)==str:
			model=str(model)
		return model
	else:
		model1=model.__dict__
		del model1['_fieldnames']
		for key in model1:
			model1[key]=__convert(model1[key])
		return model1

################################################################################
def __getmodel(model):
    '''
    Sets path for loading cellorganizer
    @param: model: a mat_struct defined by scipy.io.matlab
    '''

    path=os.sep.join(cellorganizer.__file__.split(os.sep)[0:-1])+os.sep+"models"+os.sep+model
    # when you are importing cellorganizer in the distribution directory, the path will be the local path
    if path.index('cellorganizer')==0:
        print("You are importing cellorganizer in the distribution folder")
        path=path.split('cellorganizer'+os.sep)[1]
    return np.load(path).tolist()

################################################################################
def __printKeys(myDict, theDict, tempStr = ''):
    '''
    This is the recursive function to create the dictionary
    '''

    keys = myDict.keys()
    for key in keys:
        if isinstance(myDict[key],dict):
            __printKeys(myDict[key], theDict, tempStr+key+'.')
        else:
            if not tempStr:
                theDict.update({key:myDict[key]})
            else:
                theDict.update({tempStr+key:myDict[key]})

################################################################################
def __mat2simplyDict(matfile):
    '''
    This are the functions to create the shallow dictionary.
    '''

    model = __mat2python(matfile,parameter=None)
    ans= {}
    printKeys(model,ans)
    return ans

################################################################################
def __does_file_exist(url):
    '''
    Helper function that checks if file exists on disk
    '''

    try:
        response =urllib.request.urlopen(url)
    except:
        return False

    return True
