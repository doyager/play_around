

#Label Encoder:
"""
To convert this kind of categorical text data into model-understandable numerical data, we use the Label Encoder class. 
So all we have to do, to label encode the first column, is import the LabelEncoder class from the sklearn library, 
fit and transform the first column of the data, and then replace the existing text data with the new encoded data. 
Let’s have a look at the code.

encoding categorical values is to use a technique called label encoding. Label encoding is simply 
converting each value in a column to a number. For example, the body_style column contains 5 different values.
We could choose to encode it like this:

convertible -> 0
hardtop -> 1
hatchback -> 2
sedan -> 3
wagon -> 4


"""
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
x[:, 0] = labelencoder.fit_transform(x[:, 0])

# on only particular column

from sklearn.preprocessing import LabelEncoder

lb_make = LabelEncoder()
obj_df["make_code"] = lb_make.fit_transform(obj_df["make"]) . #this will only label encode make column 
obj_df[["make", "make_code"]].head(11)

"""
That’s all label encoding is about. But depending on the data, label encoding introduces a new problem. 
For example, we have encoded a set of country names into numerical data. This is actually categorical data and 
there is no relation, of any kind, between the rows.
So this is converating the three countries names into numerical values 0,1 and 2.

The problem here is, since there are different numbers in the same column, the model will 
misunderstand the data to be in some kind of order, 0 < 1 < 2. But this isn’t the case at all.
To overcome this problem, we use One Hot Encoder.
"""

#One Hot Encoder :
"""
Now, as we already discussed, depending on the data we have, we might run into situations where, after label encoding,
 we might confuse our model into thinking that a column has data with some kind of order or hierarchy, when we clearly 
 don’t have it. To avoid this, we ‘OneHotEncode’ that column.

What one hot encoding does is, it takes a column which has categorical data, which has been label encoded, and 
then splits the column into multiple columns. The numbers are replaced by 1s and 0s, depending on which column has 
what value. In our example, we’ll get three new columns, one for each country — France, Germany, and Spain.

For rows which have the first column value as France, the ‘France’ column will have a ‘1’ and the other two columns
will have ‘0’s. Similarly, for rows which have the first column value as Germany, the ‘Germany’ column will have a ‘1’ 
and the other two columns will have ‘0’s.
"""

#The Python code for one hot encoding is also pretty simple:

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()
"""
As you can see in the constructor, we specify which column has to be one hot encoded, [0] in this case. 
Then we fit and transform the array ‘x’ with the onehotencoder object we just created. And that’s it, we now
have three new columns in our dataset:

As you can see, we have three new columns with 1s and 0s, depending on the country that 
the rows represent.
"""
#########
# one hot examples 

# one hot coding

tmp_df = input_1M[['gender']].tail(20)
temp_df

       gender
999980      M
999981      M
999982      F
999983      F
999984      M
# apply on complete data set 
          tmp_df = pd.get_dummies(tmp_df, prefix=['gender'], drop_first=True)
                  gender_M
         999980         1
         999981         1
         999982         0
         999983         0
         999984         1
         999985         1



# apply on few columns from all columns [apply on one col of two columns]
      tmp_df = input_1M[['gender','formulary_status']].tail(20)

      tmp_df = pd.get_dummies(tmp_df, prefix=['gender'], columns=['gender'],drop_first=True)

      >>> tmp_df
             formulary_status  gender_M
      999980            FRMLY         1
      999981            FRMLY         1
      999982            FRMLY         0
      999983            FRMLY         0
      999984            FRMLY         1
      999985            FRMLY         1
      999986            FRMLY         0

 # apply on few columns from all columns [apply on 2 of 3 cols]
         tmp_df = input_1M[['gender','formulary_status','generic_cd']].tail(20)

         tmp_df = pd.get_dummies(tmp_df, prefix=['gender','formulary_status'], columns=['gender','formulary_status'],drop_first=True)

         tmp_df

                generic_cd  gender_M  formulary_status_NONF
         999950          G         1                      0
         999951          G         0                      0
         999952          G         1                      0
         999953          G         0                      0
         999954          G         0                      0
         999955          G         1                      0
         999956          G         0                      0
         999957          B         1                      1

# apply on list of columns , when list is big 

        len(df.columns) = 50
        non_dummy_cols = ['A','B','C'] 
        # Takes all 47 other columns
        dummy_cols = list(set(df.columns) - set(non_dummy_cols))
        df = pd.get_dummies(df, columns=dummy_cols)

# MultiLabelBinarizer
            import pandas as pd
            from sklearn.preprocessing import MultiLabelBinarizer

            df = pd.DataFrame(
                {'groups':
                    [['a','b','c'],
                    ['c'],
                    ['b','c','e'],
                    ['a','c'],
                    ['b','e']]
                }, columns=['groups'])

            s = df['groups']

            mlb = MultiLabelBinarizer()

            pd.DataFrame(mlb.fit_transform(s),columns=mlb.classes_, index=df.index)
            #Result:

                a   b   c   e
            0   1   1   1   0
            1   0   0   1   0
            2   0   1   1   1
            3   1   0   1   0
            4   0   1   0   1

##################################################

#Custom Binary Encoding
"""
Depending on the data set, you may be able to use some combination of label encoding and one hot encoding
to create a binary column that meets your needs for further analysis.

In this particular data set, there is a column called engine_type that contains several different values:

obj_df["engine_type"].value_counts()
ohc      148
ohcf      15
ohcv      13
l         12
dohc      12
rotor      4
dohcv      1
Name: engine_type, dtype: int64
For the sake of discussion, maybe all we care about is whether or not the engine is an Overhead Cam (OHC) or not. 
In other words, the various versions of OHC are all the same for this analysis. If this is the case, then we could
use the str accessor plus np.where to create a new column the indicates whether or not the car has an OHC engine.
"""
obj_df["OHC_Code"] = np.where(obj_df["engine_type"].str.contains("ohc"), 1, other=0)




#BackwardDifferenceEncoder :

#scikit-learn contrib package call categorical-encoding which implements many of these approaches

import pandas as pd
import numpy as np

# Define the headers since the data does not have any
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/autos/imports-85.data",
                  header=None, names=headers, na_values="?" )
import category_encoders as ce

# Get a new clean dataframe
obj_df = df.select_dtypes(include=['object']).copy()

# Specify the columns to encode then fit and transform
encoder = ce.backward_difference.BackwardDifferenceEncoder(cols=["engine_type"])
encoder.fit(obj_df, verbose=1)

# Only display the first 8 columns for brevity
encoder.transform(obj_df).iloc[:,0:7].head()
"""
col_engine_type_0	col_engine_type_1	col_engine_type_2	col_engine_type_3	col_engine_type_4	col_engine_type_5	col_engine_type_6
0	1.0	0.142857	0.285714	0.428571	0.571429	0.714286	-0.142857
1	1.0	0.142857	0.285714	0.428571	0.571429	0.714286	-0.142857
2	1.0	0.142857	0.285714	0.428571	0.571429	0.714286	0.857143
3	1.0	-0.857143	-0.714286	-0.571429	-0.428571	-0.285714	-0.142857
4	1.0	-0.857143	-0.714286	-0.571429	-0.428571	-0.285714
"""





######################################################################################
# polynomial encoding, 
#we get a different distribution of values used to encode the columns:

import pandas as pd
import numpy as np

# Define the headers since the data does not have any
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/autos/imports-85.data",
                  header=None, names=headers, na_values="?" )
# Get a new clean dataframe
obj_df = df.select_dtypes(include=['object']).copy()
encoder = ce.polynomial.PolynomialEncoder(cols=["engine_type"])
encoder.fit(obj_df, verbose=1)
encoder.transform(obj_df).iloc[:,0:7].head()

"""
col_engine_type_0	col_engine_type_1	col_engine_type_2	col_engine_type_3	col_engine_type_4	col_engine_type_5	col_engine_type_6
0	1.0	-5.669467e-01	5.455447e-01	-4.082483e-01	0.241747	-1.091089e-01	0.032898
1	1.0	-5.669467e-01	5.455447e-01	-4.082483e-01	0.241747	-1.091089e-01	0.032898
2	1.0	3.779645e-01	3.970680e-17	-4.082483e-01	-0.564076	-4.364358e-01	-0.197386
3	1.0	1.347755e-17	-4.364358e-01	1.528598e-17	0.483494	8.990141e-18	-0.657952
4	1.0	1.347755e-17	-4.364358e-01	1.528598e-17	0.483494	8.990141e-18
"""
