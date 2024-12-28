#!/bin/bash
echo "Image slicer script from http://www.discoverdigitalphotography.com/2012/slit-scan-object-photography-how-to/"
if [ ! -n "$1" ]
then
echo "Usage: image-slicer.sh \"/path/to/folder containing images to be processed\""
exit 1
fi
#check %1 is a directory
if [ ! -d "$1" ]
then echo "$1 is not a directory, exiting"
exit 1
fi
#Set the starting offset, default 0
if [ ! -n "$2" ]
then offset=0
else offset=$2
fi
echo "offset is $offset"
#height of each slice
slicesize=1

#Get the number of files
filecount=`ls -1 "$1/" | wc -l`
echo "Total $filecount files"
#Get the height of the image
for i in "$1"/*
do
	if [ -f "$i" ]
	then
		echo identify -quiet -format "%w" "$i"
		width=`identify -quiet -format "%w" "$i"`
		height=`identify -quiet -format "%h" "$i"`
		if [[ $height =~ ^[0-9]+$ ]]
		then break
		fi
	fi
done
echo "Width is $width and height is $height"
#check the height was set okay
if [[ ! $height =~ ^[0-9]+$ ]]
then echo "Couldn't detect image height, exiting"
exit 1
fi
#check the offset is smaller than the image height
if [ $offset -ge $height ]
then echo "Offset of $offset is greater than or equal to the image height of $height - nothing to do"
exit
fi
#create a dir to store the files in
if [ ! -d "$1/files" ] 
then
	mkdir "$1/files"
fi
#loop through the files until we have sliced the entire image height
while [ ! $offset -ge $height ]
do
	#loop through all files in the folder
	for i in "$1"/* 
	do 
		#Check we are dealing with a file and not the files directory
		if [ -f "$i" ]
		then
			filename=$(basename "$i")
			echo "filename is $filename"
			#If we are on the first file just copy it as the subsequent image will just be overlayed on top of it to create the slice
			if [ ! -n "$prevFile" ]
			then
				file="$1/files/0000$filename"
				cp "$i" "$file"
			#Otherwise slice the top off the image, then overlay it on top of the previous image
			else
				#increment the offset to start the slice from
				offset=$(($offset+$slicesize))
				echo "offset is $offset"
				#if we've reached the full height of the image, then exit the loop
				if [ $offset -ge $height ]
				then break
				fi
				offsetpad=`printf "%04d" $offset`
				file="$1/files/$offsetpad$filename"
				#Crop off the top of the image
				echo convert "$i" -crop 0x0+0+$offset "$file"
				convert "$i" -crop 0x0+0+$offset "$file"
				if [ $? -ne 0 ]
				then
					echo "ImageMagick failed to extract the image slice, exiting"
					exit 1
				fi
				#Overlay on top of the previous image
				echo "compositing file=$file prevFile=$prevFile"
				composite -compose Copy -gravity South "$file" "$prevFile" "$file"
				if [ $? -ne 0 ]
				then
					echo "ImageMagick failed to composite the image slice, exiting"
					exit 1
				fi
			fi
			#the current image will be the previous image for the next pass through the loop
			prevFile=$file
		fi
	done
done
