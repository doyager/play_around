#python tutorials:

python3 -c 'print("hello world")'

#range
>>> range(5)
range(0, 5)
>>>
>>> list(range(5)) # list() call is not required in Python 2
[0, 1, 2, 3, 4]


#dictionary
header_dict1 = {'1':['A','B','C'], '2':['D'], '3':['E']}
>>> print(header_dict1)
{'1': ['A', 'B', 'C'], '2': ['D'], '3': ['E']}

# flatten dictionary

>>> cat_cols1 = header_dict1.values()
>>> print(cat_cols1)
dict_values([['A', 'B', 'C'], ['D'], ['E']])
>>> cat_cols2 = [item for sublist in cat_cols1 for item in sublist]
>>> print(cat_cols2)
['A', 'B', 'C', 'D', 'E']



#process time and time
import time

start_time = time.time()
    ####other process called ######
print("\n process finished in %s minutes \n" % ((time.time() - start_time) / 60))




###################
## pandas

#create df with out index_col
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)

#create df with index

import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print (df)
>>> print (df)
   Age   Name
0   28    Tom
1   34   Jack
2   29  Steve
3   42  Ricky

# create df - method 3
df = pd.DataFrame([[4, 9],] * 3, columns=['A', 'B'])
>>> df
   A  B
0  4  9
1  4  9
2  4  9

# create df - method 4
import pandas ad pd
import numpy as np

>>> df_repeat =  pd.DataFrame(np.repeat(df_key.values,"10",axis=0),columns=['id_new','VAR_new'])
>>> df_repeat
   id_new VAR_new
0  no_val       0
1  no_val       0
2  no_val       0
3  no_val       0
4  no_val       0
5  no_val       0
6  no_val       0
7  no_val       0
8  no_val       0
9  no_val       0


######
## shape - gives rows, cols
>>> df.shape  #gives (rows,cols)
(4, 2)
>>>
>>> df.shape[0] #gives only no of rows
4

## size
df.size
#8

## info - gives all column data types , object types , counts of non-null for each col
df.info()

# view options
# print options - to view full data 

#to print all rows ie. max 100
pd.set_option('display.max_rows', 100) 
print(pd.get_option("display.max_rows"))
#o/p : 100
# to n number of columns , so to view all the data
pd.set_option('display.max_columns',100)
print(pd.get_option("display.max_columns"))
#o/p: 100

pd.set_option('precision', 5)



## print column names
print(df.columns.values)


#show columns

>>> df.columns
Index(['Age', 'Name'], dtype='object')

# access col 'A' first value
 df['A'][0] # 1st value
 df['A'][1] #2nd value


########
#replace missing values 
# nulls
# count nulls

#total null count per column
print(input.isna().sum())

#Pandas provides the fillna() function for replacing missing values with a specific value. 
#Let's apply that with Mean Imputation.

import pandas as pd
import numpy as np

train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)
print("***** Train_Set *****")
print(train.describe())
train.isna().head()
# Fill missing values with mean column values in the train set
train.fillna(train.mean(), inplace=True)


#########
#correlation annalysis

# method: Spearman, Pearson, or Kendall. 
#If no method is specified, Pearson is used by default. 

import pandas as pd
path = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'

mpg_data = pd.read_csv(path, delim_whitespace=True, header=None,
            names = ['mpg', 'cylinders', 'displacement','horsepower',
            'weight', 'acceleration', 'model_year', 'origin', 'name'],
            na_values='?')

#eg : corr between two specific columsn
mpg_data['mpg'].corr(mpg_data['weight'])

#eg: correlation on all columns
mpg_data.drop(['model_year', 'origin'], axis=1).corr(method='spearman')

#########
# save df as pkl

df.to_pickle("/Users/mac/workspace/df.pkl")

# save df as csv

df.to_csv("/Users/mac/workspace/df.csv")


#change column types
 df = pd.DataFrame([[4, 9],] * 3, columns=['A', 'B'])
>>> df
   A  B
0  4  9
1  4  9
2  4  9
>>> df.dtypes
A    int64
B    int64
dtype: object
>>> df['A']=df['A'].apply(str)
>>> df
   A  B
0  4  9
1  4  9
2  4  9
>>> df.dtypes
A    object
B     int64
dtype: object

##############
# save and read csv

#save to csv

pd.DataFrame({'Name':['Tom', 'Jack', 'Steve', 'Ricky', 'Ricky'],'Age':[28,34,29,42,42]}).to_csv('/Users/mac/df.txt')

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky', 'Ricky'],'Age':[28,34,29,42,42]}
pd.DataFrame(data).to_csv('/Users/mac/df1.txt')

# read from csv
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky', 'Ricky'],'Age':[28,34,29,42,42]}
pd.DataFrame(data).to_csv('/Users/mac/df1.txt')

df2=pd.read_csv('/Users/mac/df1.txt')
df2
   Unnamed: 0  Age   Name
0           0   28    Tom
1           1   34   Jack
2           2   29  Steve
3           3   42  Ricky
4           4   42  Ricky

###############
#print only particular col 

>>> df_repeat =  pd.DataFrame(np.repeat(df_key.values,"10",axis=0),columns=['id_new','VAR_new'])
>>> df_repeat
   id_new VAR_new
0  no_val       0
1  no_val       0
2  no_val       0
3  no_val       0
4  no_val       0
5  no_val       0
6  no_val       0
7  no_val       0
8  no_val       0
9  no_val       0

#all rows for col 'VAR_new'
>>> df_repeat['VAR_new']
0    0
1    0
2    0
3    0
4    0
5    0
6    0
7    0
8    0
9    0

#rows 2 and 3 , which is from index 1:3
>>> df_repeat['VAR_new'][1:3]
1    0
2    0

###############
#replace only particular col val using value from other Data frame

>>> df_repeat =  pd.DataFrame(np.repeat(df_key.values,"10",axis=0),columns=['id_new','VAR_new'])
>>> df_key = pd.DataFrame({'row': [0,0,0,0], 'VAR': ['No_VAR','No_VAR1','no_VAR2','no_VAR3']})
>>> df_key
       VAR  row
0   No_VAR    0
1  No_VAR1    0
2  no_VAR2    0
3  no_VAR3    0
>>> df_repeat['VAR_new'][1:3]
1    0
2    0
Name: VAR_new, dtype: object

        >>> df_key['VAR'][1:3]
1    No_VAR1
2    no_VAR2
Name: VAR, dtype: object
>>> df_repeat['VAR_new'][1:3]=df_key['VAR'][1:3]
>>> df_repeat['VAR_new'][1:3]
1    No_VAR1
2    no_VAR2
Name: VAR_new, dtype: object
>>> df_repeat
   id_new  VAR_new
0  no_val        0
1  no_val  No_VAR1
2  no_val  no_VAR2
3  no_val        0
4  no_val        0
5  no_val        0
6  no_val        0
7  no_val        0
8  no_val        0
9  no_val        0


###############
#sum row values and sum col values
df = pd.DataFrame([[4, 9],] * 3, columns=['A', 'B'])
>>> df
   A  B
0  4  9
1  4  9
2  4  9
>>> df.apply(np.sum,axis=0) #df.sum(0)
A    12
B    27
dtype: int64
>>> df.apply(np.sum,axis=1) #df.sum(1)
0    13
1    13
2    13
dtype: int64
>>> df.sum(0)
A    12
B    27
dtype: int64
>>> df.sum(1)
0    13
1    13
2    13
dtype: int64

###############
#joins
df = pd.DataFrame([[4, 9],] * 3, columns=['A', 'B'])
df1 = pd.DataFrame([[4, 10],] * 3, columns=['A', ' C'])
df
   A  B
0  4  9
1  4  9
2  4  9
>>> df1
   A   C
0  4  10
1  4  10
2  4  10
>>> df3 = pd.merge(df,df1,on='A', how='inner')
>>> df3
   A  B   C
0  4  9  10
1  4  9  10
2  4  9  10
3  4  9  10
4  4  9  10
5  4  9  10
6  4  9  10
7  4  9  10
8  4  9  10
>>> df4 = pd.merge(df,df1,on='A', how='left')
>>> df4
   A  B   C
0  4  9  10
1  4  9  10
2  4  9  10
3  4  9  10
4  4  9  10
5  4  9  10
6  4  9  10
7  4  9  10
8  4  9  10
>>> df4 = pd.merge(df,df1,on='A', how='right')
>>> df4
   A  B   C
0  4  9  10
1  4  9  10
2  4  9  10
3  4  9  10
4  4  9  10
5  4  9  10
6  4  9  10
7  4  9  10
8  4  9  10


#################    
# apply lambda functions
>>> df = pd.DataFrame([[4, 9],] * 3, columns=['A', 'B'])
>>> df.apply(lambda x: x**2)
    A   B
0  16  81
1  16  81
2  16  81
>>> df.apply(lambda x: x*x)
    A   B
0  16  81
1  16  81
2  16  81
>>> df.apply(lambda x: x**3)
    A    B
0  64  729
1  64  729
2  64  729


##################
# pandas dataframe df vs series

# Series is a one-dimensional labeled array capable of holding any data type. To read data in form of panda Series:
import pandas as pd
ds = pd.Series(data, index=index)

#DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
import pandas as pd
df = pd.DataFrame(data, index=index)
In both of the above index is list

#for example: I have a csv file with following data:
,country,popuplation,area,capital
BR,Brazil,10210,12015,Brasile
RU,Russia,1025,457,Moscow
IN,India,10458,457787,New Delhi

#To read above data as series and data frame:

import pandas as pd
file_data = pd.read_csv("file_path", index_col=0)
d = pd.Series(file_data.country, index=['BR','RU','IN'] or index =  file_data.index)
#output:
>>> d
BR           Brazil
RU           Russia
IN            India

df = pd.DataFrame(file_data.area, index=['BR','RU','IN'] or index = file_data.index )
#output:
>>> df
      area
BR   12015
RU     457
IN  457787
##################





#drop drop_duplicates
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky', 'Ricky'],'Age':[28,34,29,42,42]}
df = pd.DataFrame(data)
>>> print(df)
   Age   Name
0   28    Tom
1   34   Jack
2   29  Steve
3   42  Ricky
4   42  Ricky
>>> df1 = df['Name'].drop_duplicates()
>>> print(df1)
0      Tom
1     Jack
2    Steve
3    Ricky
Name: Name, dtype: object

# pandas - data frame merge or joins

#join on single col
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print pd.merge(left,right,on='id')

   Name_x  id_x   subject_id   Name_y   id_y
0     Alex   1.0         sub1      NaN    NaN
1      Amy   2.0         sub2    Billy    1.0
2    Allen   3.0         sub4    Brian    2.0
3    Alice   4.0         sub6    Bryce    4.0
4   Ayoung   5.0         sub5    Betty    5.0
5      NaN   NaN         sub3     Bran    3.0

#join on multiple col
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print pd.merge(left,right,on=['id','subject_id'])

    Name_x   id_x   subject_id   Name_y   id_y
0      Amy      2         sub2    Billy      1
1    Allen      3         sub4    Brian      2
2    Alice      4         sub6    Bryce      4
3   Ayoung      5         sub5    Betty      5




#connect DB - odbc
import pyodbc
import os
import pandas as pd

uid = ""
pwd = ""
dbcname = "machine.com.company"
odbc_string = "DRIVER={Teradata};DBCNAME=" + dbcname + ";UID=" + uid + ";PWD=" + pwd + ";QUIETMODE=YES;Authentication=LDAP;"
conn = pyodbc.connect(odbc_string)
query = """select * from test"""
raw_data = pd.read_sql(query, conn)
print(raw_data)
row_dict = raw[key].drop_duplicates()  #drop d
n_claims = row_dict.shape[0]
