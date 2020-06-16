#!/bin/bash

#run_MapAnnotation.sh input_tif output_ometif

# bfconvert -stitch 'LAM_cell2_<0-2>_t1.tif' test2_2.ome.tif

bfconvert $1 $2
tiffcomment $2 > ome_temp.xml

while read p; do
	stringarray=($p)

	key=${stringarray[0]}
	value=${stringarray[1]}

	str='<M K="'$key'">'$value'</M>'
	# str='<ROI ID="urn:lsid:export.openmicroscopy.org:ROI:'$count'"><Union><Rectangle ID="Shape:'$count':0" Height="'$height'.0" Width="'$width'.0" X="'$x'.0" Y="'$y'.0" /></Union></ROI>'
	echo $str >> key_value.xml
done < temp_key_value.txt

sed -i '' "s|</Pixels>.*</Image>|</Pixels><AnnotationRef ID=\"Annotation:1\"/></Image>|g" ome_temp.xml


STRING=''
for LINE in $(cat key_value.xml)
do
    STRING=$STRING" "$LINE
done
sed -i '' "s|</Image>.*</OME>|</Image><StructuredAnnotations><MapAnnotation ID=\"Annotation:1\"><Value>$STRING</Value></MapAnnotation></StructuredAnnotations></OME>|g" ome_temp.xml
sed -i '' "s|> <|><|g" ome_temp.xml

sed -i '' "s|<!--.*-->||g" ome_temp.xml

rm key_value.xml

xmlindent ome_temp.xml > ome_temp_indent.xml
tiffcomment -set "ome_temp_indent.xml" $2
rm ome_temp.xml
rm ome_temp_indent.xml