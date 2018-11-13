# importing basic libraries

import numpy as np

import pandas as pd

from pandas import Series, DataFrame

from sklearn.model_selection import train_test_split

import test and train file

train = pd.read_csv('Train.csv')

test = pd.read_csv('test.csv')

# importing linear regressionfrom sklearn

from sklearn.linear_model import LinearRegression

lreg = LinearRegression()

splitting into training and cv for cross validation

X = train.loc[:,['Outlet_Establishment_Year','Item_MRP']]

x_train, x_cv, y_train, y_cv = train_test_split(X,train.Item_Outlet_Sales)

training the model

lreg.fit(x_train,y_train)

predicting on cv

pred = lreg.predict(x_cv)

calculating mse

mse = np.mean((pred - y_cv)**2)

In this case, we got mse = 19,10,586.53, which is much smaller than our model 2. Therefore predicting with the help of two features is much more accurate.

Let us take a look at the coefficients of this linear regression model.

# calculating coefficients

coeff = DataFrame(x_train.columns)

coeff['Coefficient Estimate'] = Series(lreg.coef_)

coeff

r-square for the above model.

lreg.score(x_cv,y_cv)

# more variables

X = train.loc[:,['Outlet_Establishment_Year','Item_MRP','Item_Weight']]

splitting into training and cv for cross validation

x_train, x_cv, y_train, y_cv = train_test_split(X,train.Item_Outlet_Sales)

## training the model

lreg.fit(x_train,y_train)

ValueError: Input contains NaN, infinity or a value too large for dtype(‘float64’).

It produces an error, because item weights column have some missing values. So let us impute it with the mean of other non-null entries.

train['Item_Weight'].fillna((train['Item_Weight'].mean()), inplace=True)

Let us try to run the model again.

training the model lreg.fit(x_train,y_train)

## splitting into training and cv for cross validation

x_train, x_cv, y_train, y_cv = train_test_split(X,train.Item_Outlet_Sales)

## training the model lreg.fit(x_train,y_train)

predicting on cv pred = lreg.predict(x_cv)

calculating mse

mse = np.mean((pred - y_cv)**2)

mse

1853431.59

## calculating coefficients

coeff = DataFrame(x_train.columns)

coeff['Coefficient Estimate'] = Series(lreg.coef_)



calculating r-square

lreg.score(x_cv,y_cv) 0.32942
