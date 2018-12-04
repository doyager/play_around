
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
