
#1. apply sqroot to all columns
import pandas as pd
df = pd.DataFrame([[4, 9],] * 3, columns=['A', 'B'])
df . #display
>>> df
   A  B
0  4  9
1  4  9
2  4  9

import numy as np
df1=df.apply(np.sqrt)
df1
>> df3
     A    B
0  2.0  3.0
1  2.0  3.0
2  2.0  3.0



# convert all arr elements to int 

import numpy as np
x= np.array([[12.0, 12.51], [2.34, 7.98], [25.23, 36.50]])
print("Original array elements:")
print(x)
print("Convert float values to integer values:")
print(x.astype(int))



# just to select col 1 for all rows
# arr[:,0]
"""
When you say arr2d[:, 0], you're saying give me the 0th index of all the rows in arr2d 
(this is another way of saying give me the 0th column).
"""
