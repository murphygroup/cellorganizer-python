docker-python
=============

The docker-python project strives to be a Python 3 package to manage the binaries used in Docker for CellOrganizer.

Prototypes 
==========

slml2img
--------

```
# answer = slml2img( list_of_models, options )
# list_of_models is a list
# options is a dictionary

from cellorganizer import slml2img
list_of_models = [ 'model1.mat', 'model2.mat' ]
options['targetDirectory'] = '/path/to/folder'
options['prefix'] = 'img'
options['debug'] = False;

answer = slml2img( list_of_models, options )
```