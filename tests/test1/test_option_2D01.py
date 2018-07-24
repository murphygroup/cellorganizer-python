import glob
import tarfile 
import os
from Options2txt import __options2txt
import filecmp
if not os.path.exists('../../images/HeLa/2D/LAM/'):
    os.makedirs('../../images/HeLa/2D/LAM/')
    os.system('wget -nc --quiet http://www.cellorganizer.org/Downloads/v2.7/docker/v2.7.1/images/demo2D01.tgz;mkdir -p ../../images/HeLa/2D/LAM;tar -xvf demo2D01.tgz -C ../../images/HeLa/2D/LAM/;rm -f demo2D01.tgz')
		
options = {}
options['verbose'] = True
options['debug'] = False
options['display'] = False
options['model.name'] = 'demo2D01'
options['train.flag'] = 'all'
options['nucleus.class'] = 'nuclear_membrane'
options['nucleus.type'] = 'medial_axis'
options['cell.class'] = 'cell_membrane'
options['cell.type'] = 'ratio'
options['protein.class'] = 'vesicle'
options['protein.type'] = 'gmm'
directory = '/home/ruijiac/docker-python/images/HeLa/2D/LAM/'
options['masks'] = glob.glob(directory + 'crop/*.tif')
options['model.resolution'] = [ 0.49, 0.49 ]
options['model.filename'] = 'lamp2.xml'
options['model.id'] = 'lamp2'
options['documentation.description'] = 'This model has been trained using demo2D01 from CellOrganizer'

__options2txt(options,"input.txt")

print filecmp.cmp('input.txt', 'input_right.txt')

