
file_list=`find ./ -name '*.wav'`
echo $file_list
for wav_file in $file_list
do
    echo $wav_file
    wav_file_temp=$wav_file.tmp
    cat $wav_file | awk 'BEGIN{flag=0} {if ($1~"^RIFF"){flag=1;} if(flag==1){print}}' > $wav_file_temp
    mv $wav_file_temp $wav_file
done

