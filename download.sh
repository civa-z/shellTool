#!/bin/bash

dir=wavdir
if [ ! -x $dir ];then
    mkdir -p $dir;
fi

while read line;do
    if [ "$line" != "" ]; then
	filename=`basename $line` 
	filepath="./$dir/$filename"
        echo "$line to $filepath"
	wget $line -O $filepath
    fi
done < url.txt


