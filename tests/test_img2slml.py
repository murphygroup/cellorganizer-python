from cellorganizer import img2slml

options = {'targetDirectory':'pwd',
            'prefix':'imgs',
            'compression':'lzw',
            'debug':False,
            'temporary_results':"pwd filesep 'temporary_results'",
            'verbose':False,
            'display':False,

dim = '2D'
dna = ['dna_image1','dna_image2','dna_image3']
cell = ['cell_image1','cell_image2','cell_image3']
protein = ['protein_image1','protein_image2','protein_image3']

img2slml(dim, dna, cell, protein, options)
