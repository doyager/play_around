#!/bin/bash


# run :   ./compare_file_v1.sh /path/file1.txt /path/file2.txt

file1=$1 #path
file2=$2


echo "########################"
echo "file 1 : "$file1
echo "file 2 : "$file2
echo "#######################"


#compare full file content
if cmp -s $file1 $file2
then
   echo "The files same, all values match!!"
else
   echo "The files are different"
fi

echo "#######################"


#file name

file1_name=$(echo $file1 | awk -F/ '{print $NF}')
file2_name=$(echo $file2 | awk -F/ '{print $NF}')

echo "file 1 name :" $file1_name
echo "file 2 name :" $file2_name

file1_content=$(cat $file1)
file2_content=$(cat $file2)


echo " "
echo "file 1 contents: "
echo $file1_content

#exit 1


#creating arr

arr_file1=($file1_content)

echo "${arr_file1[2]}"


arr_file2=($file2_content)


#create key value pair for both
#compare the key value pairs and print simultanesouly to a log
#exit 1


declare -A keyval_file1

for i in "${arr_file1[@]}"
do
   	echo "from arry loop"
	key=$(echo $i | cut -d '=' -f1)
	value=$(echo $i | cut -d '=' -f2)
	echo "key : " $key
	echo "val : " $value
done

keyval_file1[""]

exit 1

# converting to key value pair and printing

declare -A arr

arr["key1"]=val1

arr+=( ["key2"]=val2 ["key3"]=val3 )

for key in ${!arr[@]}; do
    echo ${key} ${arr[${key}]}
done



# print each line of file
#filename='company.txt'
n=1
while read line; do
# reading each line
echo "Line No. $n : $line"
n=$((n+1))
done < $file1
