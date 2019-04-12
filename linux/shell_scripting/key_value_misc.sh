

# you need bash version 4 for this 

declare -A names
names[John]=Doe
names[Jane]=Doe
names[Jim]=Smith
names[Angela]=Merkel

for i in "${!names[@]}"
do
    first_name=$i
    last_name=${names[$i]}
    echo "$first_name : $last_name"
done

echo "test finished"



# assign a key value pair from a array of values by spliting each string in the arr

# sampel data
fs.aio-max-nr=1000
fs.file-max=61
fs.suid_dumpable=0
kernal.core_uses_pid=3
kernal.exec-shields=3

#!/bin/bash

file1=$1

# READING file contents into a variable 
file1_content=$(cat $file1)

#creating arr

arr_file1=($file1_content)

for i in "${arr_file1[@]}"
do
        echo "from arry loop"
        key=$(echo $i | cut -d '=' -f1)
        value=$(echo $i | cut -d '=' -f2)
        echo "key : " $key
        echo "val : " $value
        keyval_file1[$key]=$value
        echo "after assiging "
        val_print=${keyval_file1[$key]}
        echo "val print : " $val_print
done



# prijnt a key value pair
# For every key in the associative array..
for KEY in "${!ARRAY[@]}"; do
  # Print the KEY value
  echo "Key: $KEY"
  # Print the VALUE attached to that KEY
  echo "Value: ${ARRAY[$KEY]}"
done
