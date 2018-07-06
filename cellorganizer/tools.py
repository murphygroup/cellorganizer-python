import os
import numpy as np
import scipy.io

# Public Method
########################################################################
########################################################################
def img2slml(dim, dna, cell, protein, options):
    txtfilename = "input.txt"
    __options2txt(options,txtfilename)
    f = open(txtfilename,"a")
    
    text = "dimensionality = '" + dim +"';\n"
    f.write(text)

    f.write("dnaImagesDirectoryPath = {")

    for name in dna:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)


    f.write("cellImagesDirectoryPath = {")

    for name in cell:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)


    f.write("proteinImagesDirectoryPath = {")

    for name in protein:
        text = text + "'" + name + "',"

    text = text[:-1]
    text = text+"};\n"
    f.write(text)
    f.close()

    os.system("img2slml input.txt;rm input.txt")   
    return None


########################################################################
def slml2img(filenames, options):
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

#######################################################################
def slml2info(filename):
    os.system('slml2info {}'.format(filename))
    return None

#######################################################################
def slml2slml(files, options):
    filenames = '{'
    for filename in files:
        filenames = filenames + '\'' + filename + '\'' + ',' 
    filenames = filenames[:-1] +  '}'
    
    f = open('input.txt','w')
    f.write('files = {}'.format(filenames))
    f.write('\n')
    for key in options:
        f.write('{} = {}'.format(option, options[key]))
        f.write('\n')
    f.close()

    os.system('slml2slml input.txt; rm input.txt')
    return None
#######################################################################
def slml2report(model1_filename, model2_filename):
    os.system('slml2report {} {}'.format(model1_filename, model2_filename))
    return None


#Private Method
#######################################################################
#######################################################################
def __options2txt(options,filename):
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
                text = text+"];\n"
        elif isinstance(options[key],float):
            text = 'options.'+key+ ' = ' +str('%.3f' %  options[key])+';\n'
        else:
            text = 'options.'+key+ ' = ' +str(options[key])+';\n'
        f.write(text)                                    
    f.close()



# The input is shallow model dictionary
def __shallowdict2mat(model):
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

    scipy.io.savemat('test.mat', mdict={'model': tem_dic})
    return tem_dic
    

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

def __getmodel(model):
    path=os.sep.join(cellorganizer.__file__.split(os.sep)[0:-1])+os.sep+"models"+os.sep+model
    #when you are importing cellorganizer in the distribution directory, the path will be the local path
    if path.index('cellorganizer')==0:
        print("You are importing cellorganizer in the distribution folder")
        path=path.split('cellorganizer'+os.sep)[1]
    return np.load(path).tolist()

# This is the recursive function to create the dictionary
def __printKeys(myDict, theDict, tempStr = ''):
    keys = myDict.keys()
    for key in keys:
        if isinstance(myDict[key],dict):
            __printKeys(myDict[key], theDict, tempStr+key+'.')
        else:
            if not tempStr:
                theDict.update({key:myDict[key]})
            else:
                theDict.update({tempStr+key:myDict[key]})
                
#  This are the functions to create the shallow dictionary.      
def __mat2simplyDict(matfile):
    model = __mat2python(matfile,parameter=None)
    ans= {}
    printKeys(model,ans)
    return ans

