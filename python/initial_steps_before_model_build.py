
# print all info about dataframe
print(df_flights.info())

# to create copy of data
cat_df_flights_lc = cat_df_flights.copy()

# mark category variables 
"""it's a good practice to typecast categorical features to a category dtype
because they make the operations on such columns much faster than the object dtype

"""
      cat_df_flights_lc['carrier'] = cat_df_flights_lc['carrier'].astype('category')
      cat_df_flights_lc['origin'] = cat_df_flights_lc['origin'].astype('category')                                                              

      print(cat_df_flights_lc.dtypes)
      #carrier    category
      #tailnum      object
      #origin     category

# null counts 
                # print all nulls in the df
                print(df_flights.isnull().values.sum())
                #o/p : 248
                
                # print column - wise null counts 
                print(df_flights.isnull().sum())
                        # o/p:
                        #carrier      0
                        #tailnum    248
                        #origin       0
                        #dest         0

# filter all non - numneric columns

df_nonNUm = df_flights.select_dtypes(include=['object']).copy()


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
        
        # method 2
        input_nbr = input_1M_tmp.select_dtypes(['number'])

       



# rename column name 

                input_1M = pd.read_csv("/Users/mac/test_444.csv")

                #new col names
                input_1M.columns = ['ckey', 'col2','co13']


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

                                        
 # EDA - Exploratory Data analysis
                                        
    # frequency districbution , sum of each value type per column
                                     print(cat_df_flights['carrier'].value_counts())
                                       # AS    62460
                                       # WN    23355
                                       # OO    18710
                                       # DL    16716
     
    # distinct values per column - dist count
                                       print(cat_df_flights['carrier'].value_counts().count())
                                       
                                        

                                        
# add new fields 
                                        
                                        
                    # add new filed called "OTHERS" for less frequent values 
                                        
                                        
                                         # method 0 : tested !! - working 
                                """
                                #Intial :
                                >>> input_1M_tmp2['member_relationship_cd'].value_counts()
                                18    849381
                                01    122356
                                19     27272
                                02       698
                                22       159
                                29        93
                                17        21
                                53         9
                                G8         8


                                #Add "other" as new  category :


                                >>> input_1M_tmp2_tmp['member_relationship_cd'].value_counts()
                                18       849381
                                01       122356
                                19        27272
                                02          698
                                22          159
                                29           93
                                17           21
                                53            9
                                G8            8
                                OTHER         0

                                #value counts after the converge action , Converge to other category
                                >>> input_1M_tmp2_tmp['member_relationship_cd'].value_counts()
                                18       849381
                                01       122356
                                19        27272
                                OTHER       988
                                G8            0
                                53            0
                                29            0
                                22            0
                                17            0
                                02            0
                                """

                        #member_relationship_cd
                        input_1M_tmp2_tmp['member_relationship_cd'] = input_1M_tmp2_tmp['member_relationship_cd'].astype('category')
                        relationship_other_label = 'OTHER'
                        #capture all  categories other than top 3
                        relationship_others = input_1M_tmp2_tmp['member_relationship_cd'].value_counts().index[3:]
                        input_1M_tmp2_tmp['member_relationship_cd'] = input_1M_tmp2_tmp['member_relationship_cd'].cat.add_categories([relationship_other_label])
                        input_1M_tmp2_tmp['member_relationship_cd'] = input_1M_tmp2_tmp['member_relationship_cd'].replace(relationship_others, relationship_other_label)

# Drop fields

# Drop any rows which have any nans
df.dropna()
# Drop columns that have any nans
df.dropna(axis=1)
# Only drop columns which have at least 90% non-NaNs
df.dropna(thresh=int(df.shape[0] * .9), axis=1)

# Drop records based on column values 


import pandas as pd
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'year': [2012, 2012, 2013, 2014, 2014],
        'reports': [4, 24, 31, 2, 3]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
# name not equal to Tina
df[df.name != 'Tina']

# name either TINA or Jason
df[(df.name == 'Tina') | (df.name == 'Jason')]

'''
Imp links :

https://medium.com/@rrfd/cleaning-and-prepping-data-with-python-for-data-science-best-practices-and-helpful-packages-af1edfbe2a3

'''
