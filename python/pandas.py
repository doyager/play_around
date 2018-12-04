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
>>> df.shape  #gives (rows,cols)
(4, 2)
>>>
>>> df.shape[0] #gives only no of rows
4

#show columns

>>> df.columns
Index(['Age', 'Name'], dtype='object')

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
