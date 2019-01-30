

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
