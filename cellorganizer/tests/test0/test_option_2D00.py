from Options2txt import __options2txt
import filecmp

options = {}
options['targetDirectory'] = 'pwd'
options['prefix'] = 'img'
options['compression'] = 'lzw'
options['debug'] = False
options['verbose'] = True
options['display'] = False
options['numberOfSynthesizedImages'] = 1

__options2txt(options,"input.txt")
print filecmp.cmp('input.txt', 'input_right.txt')

