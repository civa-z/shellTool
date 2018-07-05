for name_jpg in `ls *.jpg`
do
	name_png=`basename $name_jpg .jpg`".png"
        echo $name_jpg
	echo $name_png
	convert $name_jpg $name_png
done

