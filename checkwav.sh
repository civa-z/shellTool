#!/bin/bash

dir=$1
echo $dir
echo
dirlist=`ls $dir`

for subdir in $dirlist;do
    subdirpath="$dir/$subdir"
    if [ -d $subdirpath -a $subdir != "." -a $subdir != "annotations" ];then
        checkresult=`ls -la "$subdirpath/audio/" | awk 'BEGIN{size=-1;flag="true";} \
            {if($5 && $5!=4096){if(size==-1){size=$5} else if (size!=$5){flag="false"}}}\
            END{ if(flag=="true"){print "OK"}else{print "NOK"}}'`
        echo $subdirpath $checkresult
        #exit
    fi
done
