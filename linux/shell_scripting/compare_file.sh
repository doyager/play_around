#!/bin/bash


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

exit 1

#filename='company.txt'
n=1
while read line; do
# reading each line
echo "Line No. $n : $line"
n=$((n+1))
done < $file1
