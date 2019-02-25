


#calculate no of numeric fields / print numeric fields

        import pandas as pd
        import numpy as np

        df = pd.DataFrame({'A': range(7, 10),
                           'B': np.random.rand(3),
                           'C': ['foo','bar','baz'],
                           'D': ['who','what','when']})
        df
        #    A         B    C     D
        # 0  7  0.704021  foo   who
        # 1  8  0.264025  bar  what
        # 2  9  0.230671  baz  when

        df_numerics_only = df.select_dtypes(include=[np.number])
        df_numerics_only
        #    A         B
        # 0  7  0.704021
        # 1  8  0.264025
        # 2  9  0.230671

        colnames_numerics_only = df.select_dtypes(include=[np.number]).columns.tolist()
        colnames_numerics_only
        # ['A', 'B']





# replace / fill missing values 

  # Fill NaN with ' '
  df['col'] = df['col'].fillna(' ')
  # Fill NaN with 99
  df['col'] = df['col'].fillna(99)
  # Fill NaN with the mean of the column
  df['col'] = df['col'].fillna(df['col'].mean())

  # forward filling 

        df = pd.DataFrame(data={'col1':[np.nan, np.nan, 2,3,4, np.nan, np.nan]})
          col1
      0   NaN
      1   NaN
      2   2.0
      3   3.0
      4   4.0 # This is the value to fill forward
      5   NaN
      6   NaN
      df.fillna(method='pad', limit=1)
          col1
      0   NaN
      1   NaN
      2   2.0
      3   3.0
      4   4.0
      5   4.0 # Filled forward
      6   NaN
  
  # backward filling 

            # Fill the first two NaN values with the first available value
      df.fillna(method='bfill')
          col1
      0   2.0 # Filled
      1   2.0 # Filled
      2   2.0 
      3   3.0
      4   4.0
      5   NaN
      6   NaN
      
   # condition based filling value or new column 

            # Follow this syntax
            np.where(if_this_condition_is_true, do_this, else_this)
            # Example
            df['new_column'] = np.where(df[i] > 10, 'foo', 'bar) 
      
      
      # Fill based on start with and end with clause 
              '''
              You’re able to do more complex operations like the one below. Here we are checking if the column record 
              starts with foo and does not end with bar. If this checks out we will return True else we’ll return the 
              current value in the column.
              '''
        df['new_column'] = np.where(df['col'].str.startswith('foo') and  
                                    not df['col'].str.endswith('bar'), 
                                    True, 
                                    df['col'])
                   
                   
             # Three level nesting with np.where
                  np.where(if_this_condition_is_true_one, do_this, 
                    np.where(if_this_condition_is_true_two, do_that, 
                      np.where(if_this_condition_is_true_three, do_foo, do_bar)))
                  # A trivial example
                  df['foo'] = np.where(df['bar'] == 0, 'Zero',
                                np.where(df['bar'] == 1, 'One',
                                  np.where(df['bar'] == 2, 'Two', 'Three')))

# Drop fields

# Drop any rows which have any nans
df.dropna()
# Drop columns that have any nans
df.dropna(axis=1)
# Only drop columns which have at least 90% non-NaNs
df.dropna(thresh=int(df.shape[0] * .9), axis=1)



'''
Imp links :

https://medium.com/@rrfd/cleaning-and-prepping-data-with-python-for-data-science-best-practices-and-helpful-packages-af1edfbe2a3

'''
