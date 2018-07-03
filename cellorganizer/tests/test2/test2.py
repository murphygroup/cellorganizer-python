#options from demo3D11
from Options2txt import __options2txt
import filecmp

options = {}
options['sampling.method'] = 'disc'
options['debug'] = True
options['verbose'] = True
options['display'] = False
options['downsampling'] = [5,5,1]
options['train.flag'] = 'framework'
options['model.filename'] = '3D_HeLa_framework.xml'
options['model.name'] = '3d_hela_framework_model'
options['model.id'] = 'num2str(now)'
options['nucleus.type'] = 'cylindrical_surface'
options['nucleus.class'] = 'nuclear_membrane'
options['nucleus.name'] = 'all'
options['nucleus.id'] = 'num2str(now)'
options['cell.type'] = 'ratio'
options['cell.class'] = 'cell_membrane'   
options['cell.model'] = 'framework'
options['cell.id'] = 'num2str(now)'
options['model.resolution'] = [0.049, 0.049, 0.2000]
options['documentation.author'] = 'Murphy Lab'
options['documentation.email'] = 'murphy@cmu.edu'
options['documentation.website'] = 'murphy@cmu.edu'
options['documentation.description'] = 'This is the framework model is the result from demo3D11.'

options['documentation.date'] = 'date'
__options2txt(options,"input.txt")
 
print filecmp.cmp('input.txt', 'input_right.txt')
