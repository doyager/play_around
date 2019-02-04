"""
Contents:

1.Axis
2. Read and write Pickle
3. open file ,types of opening .. r and rb


"""
############ 1.Axis

"""
It's perhaps simplest to remember it as 0=down and 1=across.

This means:

Use axis=0 to apply a method down each column, or to the row labels (the index).
Use axis=1 to apply a method across each row, or to the column labels.

So, concerning the method in the question, df.mean(axis=1), seems to be correctly defined.
It takes the mean of entries horizontally across columns, that is, along each individual row.
On the other hand, df.mean(axis=0) would be an operation acting vertically downwards across rows.

Similarly, df.drop(name, axis=1) refers to an action on column labels, because they intuitively 
go across the horizontal axis. Specifying axis=0 would make the method act on rows instead.

"""
#axis=0
#creatind df with axis = 0 , this wil apply repeat function vertically, meanind adding rows , so rows will be 5
>>> import numpy as np
>>> import pandas as pd
>>> df_key = pd.DataFrame({'id':[0],'VAL':['no_val']})
>>> df_key
      VAL  id
0  no_val   0
>>> df_repeat =  pd.DataFrame(np.repeat(df_key.values,"5",axis=0),columns=['id_new','VAR_new'])
>>> df_repeat
   id_new VAR_new
0  no_val       0
1  no_val       0
2  no_val       0
3  no_val       0
4  no_val       0
>>> df_repeat.shape
(5, 2)


#axis=1
#creating df with axis =1, this will apply the repeat function horizonatlly , meaning adding more cols ie.. 5 * no of cols in df_key
>>> import numpy as np
>>> import pandas as pd
>>> df_key = pd.DataFrame({'id':[0],'VAL':['no_val']})
>>> df_key
      VAL  id
0  no_val   0
>>> df_repeat_axis_is_1 =  pd.DataFrame(np.repeat(df_key.values,"5",axis=1))
>>> df_repeat_axis_is_1
        0       1       2       3       4  5  6  7  8  9
0  no_val  no_val  no_val  no_val  no_val  0  0  0  0  0
>>> df_repeat_axis_is_1.shape
(1, 10)


############ 2.Pickle
"""
Pickling:

Literally, the term pickle means storing something in a saline solution. 
Only here, instead of vegetables its objects. Not everything in life can 
be seen as 0s and 1s (gosh! philosophy), but pickling helps us achieve that
since it converts any kind of complex data to 0s and 1s (byte streams). 
This process can be referred to as pickling, serialization, flattening or 
marshalling. The resulting byte stream can also be converted back into Python 
objects by a process known as Unpickling.

The real world uses of Pickling and Unpickling are widespread as they allow you
to easily send data from one server to another, and store it in a file or database.

Advantages
Helps in saving complicated data.
Quite easy to use, doesn’t require several lines of code and hence not bulky.
Saved data is not so readable hence provides some data security.

"""

#pickle
import pickle
emp = {1:"A",2:"B",3:"C",4:"D",5:"E"}
pickling_on = open("Emp.pickle","wb")
pickle.dump(emp, pickling_on)
pickling_on.close()

#unpickle
pickle_off = open("Emp.pickle","rb")
emp = pickle.load(pickle_off)
print(emp)



############### 3. open files

#open files and modes

#To open a text file, use:
fh = open("hello.txt", "r")

#To read a text file, use:
fh = open("hello.txt","r")
print fh.read()

#To read one line at a time, use:
fh = open("hello".txt", "r")
print fh.readline()

#To read a list of lines use:
fh = open("hello.txt.", "r")
print fh.readlines()

#To write to a file, use:
fh = open("hello.txt","w")
write("Hello World")
fh.close()

#to write to a file, use:
fh = open("hello.txt", "w")
lines_of_text = ["a line of text", "another line of text", "a third line"]
fh.writelines(lines_of_text)
fh.close()

#To append to file, use:
fh = open("Hello.txt", "a")
write("Hello World again")
fh.close()

#To close a file, use
fh = open("hello.txt", "r")
print fh.read()
fh.close()

# On Windows, 'b' appended to the mode opens the file in binary mode, so there are also modes like 'rb', 'wb', and 'r+b'.

open("hello.txt","rb")

############
          
 #extract zip file       
 import zipfile
zip_ref = zipfile.ZipFile(zip_path, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()

print ("#" * 50)
######################
          
  # download files 
import wget
          
url='https://github.com/google/guava'
sample_data_dir="/Users/mac/workspace/personal/test_area/predict_lang/data/sample/"

wget.download(url, sample_data_dir)
