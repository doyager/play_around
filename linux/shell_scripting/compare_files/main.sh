#!/usr/local/bin/bash



file1=$1 #path
hostname1=$2
file2=$3
hostname2=$4

project_dir="."
temp_dir=$project_dir"/tmp_data"
log_dir=$project_dir"/logs"
log_file=$log_dir"/run_op.txt"

#creating log dir
mkdir -p $log_dir


#create temp data folder
mkdir -p $temp_dir

#copy files to local
#sftp user@hostname<<EOF
# get $file2 $temp_dir
# exit
#EOF


echo "########################"
echo "file 1 : "$file1
echo "file 2 : "$file2
echo "#######################"


#compare full file content
if cmp -s $file1 $file2
then
   echo "Both files are same, all values match!!"
else
   echo "The files are different"
fi

echo "#######################"


#extracting file name

file1_name=$(echo $file1 | awk -F/ '{print $NF}')
file2_name=$(echo $file2 | awk -F/ '{print $NF}')

#reading file content
file1_content=$(cat $file1)
file2_content=$(cat $file2)

#creating file content arr
arr_file1=($file1_content)
arr_file2=($file2_content)


declare -A keyval_file1

#create key value pair for both
for i in "${arr_file1[@]}"
do
	key=$(echo $i | cut -d '=' -f1)
	value=$(echo $i | cut -d '=' -f2)
	keyval_file1[$key]=$value
done

declare -A keyval_file2

for i in "${arr_file2[@]}"
do
	key=$(echo $i | cut -d '=' -f1)
	value=$(echo $i | cut -d '=' -f2)
	keyval_file2[$key]=$value
done

log_dir="./logs"
#creating log dir
mkdir -p $log_dir
log_file=$log_dir"/run_op.txt"

if [ ! -e "$log_file" ] ; then
    echo "Filename,Parameter,"$hostname1","$hostname2",IsDiff" > $log_file
fi

#comparing two file values and writing to log file
for key in "${!keyval_file1[@]}"
do

	val1=${keyval_file1[$key]}
	val2=${keyval_file2[$key]}
	if [ $val1 == $val2 ]
	then
	result="True"
	else
	result="False"
	fi
echo $file1_name","$key","$val1","$val2","$result >> $log_file
done


echo "Process completed !!!"
exit 1
