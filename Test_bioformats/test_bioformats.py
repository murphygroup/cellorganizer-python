from .bioformats import xmlvalid
from .bioformats import xmlindent
from .bioformats import tiffcomment
from .bioformats import showinf

def test_xmlvalid_true():
    filename = "cell1.ome.tif"
    assert xmlvalid( filename ) == True

def test_xmlvalid_false():
    filename = "cell.ome.tif"
    assert xmlvalid( filename )== False

def test_tiffcomment_true():
    filename = "cell1.ome.tif"
    xml = 'SizeT="1" SizeX="757" SizeY="777" SizeZ="1" Type="uint8">'
    assert (xml in tiffcomment( filename )) == True

def test_tiffcomment_false():
    filename = "cell.ome.tif"
    assert tiffcomment( filename )== False

def test_xmlindent_true():
    filename = "cell1.ome.tif"
    xml = 'SizeT="1" SizeX="757" SizeY="777" SizeZ="1" Type="uint8">'
    assert (xml in xmlindent( filename )) == True 

def test_xmlindent_false():
    filename = "cell.ome.tif"
    assert xmlindent( filename )== False

def test_showinf_true():
    filename = "cell1.ome.tif"
    assert (('SizeZ = 1' in showinf( filename )) & (('SizeT = 1') in showinf( filename ))) ==True

def test_showinf_false():
    filename = "cell.ome.tif"
    assert showinf( filename )== False







