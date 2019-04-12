#!/usr/local/bin/bash

: <<'END'
# to compare two property files and print out put to a log 
# usage : ./main.sh ./sysctl_host1.txt hstmc1 ./sysctl_host2.txt hstmc2

cat ./logs/run_op.txt 
Parameter,hstmc1,hstmc2,Result
kernal.core_uses_pid,3,3,True
fs.aio-max-nr,1000,1000,True
fs.suid_dumpable,0,0,True
fs.file-max,61,62,False
kernal.exec-shields,3,3,True

comments end !!
END


file1=$1 #path
hostname1=$2
file2=$3
hostname2=$4


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


#create key value pair for both
#compare the key value pairs and print simultanesouly to a log
#exit 1


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

log_file="./logs/run_op.txt"

echo "FileName,Parameter,"$hostname1","$hostname2",IsDiff" >> $log_file

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
