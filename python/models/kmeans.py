# Dependencies

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Load the train and test datasets to create two DataFrames

train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)
test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

print("***** Train_Set *****")
print(train.head())
print("\n")
print("***** Test_Set *****")
print(test.head())

print("***** Train_Set *****")
print(train.describe())
print("\n")
print("***** Test_Set *****")
print(test.describe())

print(train.columns.values)

# For the test set
test.isna().head()

# total number of missing values in both datasets.

print("*****In the train set*****")
print(train.isna().sum())
print("\n")
print("*****In the test set*****")
print(test.isna().sum())


#Pandas provides the fillna() function for replacing
#missing values with a specific value. Lets apply that with Mean Imputation.

# Fill missing values with mean column values in the train set
train.fillna(train.mean(), inplace=True)
# Fill missing values with mean column values in the test set
test.fillna(test.mean(), inplace=True)

#check for missing values against
print(train.isna().sum())

print(test.isna().sum())

#check info about all cols , so that we consider only numeric for our model
train.info()

#before we convert all req cols to numeric, lets drop all unnecessary fields which are not significant for our kmeans model  i.e. feature engineering
train = train.drop(['Name','Ticket', 'Cabin','Embarked'], axis=1)
test = test.drop(['Name','Ticket', 'Cabin','Embarked'], axis=1)



#Now that the dropping part is done lets convert the Sex feature to a numerical one (only Sex is remaining now
#which is a non-numeric feature). You will do this using a technique called Label Encoding.

labelEncoder = LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex'] = labelEncoder.transform(train['Sex'])
test['Sex'] = labelEncoder.transform(test['Sex'])

# Lets investigate if you have non-numeric data left

train.info()

test.info()


# If we have no non-numeric column left , then we are good for K-Means modelling

#first drop the Survival column from the data with the drop() function.

X = np.array(train.drop(['Survived'], 1).astype(float))
y = np.array(train['Survived'])

#review all the features you are going to feed to the algorithm with
train.info()

########################################################################
# model build - iter 1

kmeans = KMeans(n_clusters=2) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(X)
# o/p :   KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',random_state=None, tol=0.0001, verbose=0)


# lets check how correctly means clustered our records into survived and non survived for above config
correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print(correct/len(X))
#o/p: 0.5084175084175084
# 50% accuary for the above config


########################################################################


# improve model performance
# we need to tweak few model paramters to improve efficiency , like algorithm, max_iter , n_jobs

# model build - iter 2
kmeans = kmeans = KMeans(n_clusters=2, max_iter=600, algorithm = 'auto')
kmeans.fit(X)
#o/p : KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=600,n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',random_state=None, tol=0.0001, verbose=0)

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print(correct/len(X))
#o/p : 0.49158249158249157  , 49% Accuary , so it dropped

#You can see a decrease in the score. One of the reasons being you have not scaled the values of the different
#features that you are feeding to the model. The features in the dataset contain different ranges of values. So,
#what happens is a small change in a feature does not affect the other feature. So, it is also important to scale
#the values of the features to a same range.

#Let's do that now and for this experiment you are going to take 0 - 1 as the uniform value range across all the features.

########################################################################

#scaling
#Let's do that now and for this experiment you are going to take 0 - 1 as the uniform value range across all the features.
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# model build - iter 3
kmeans.fit(X_scaled)
#KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=600,n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',random_state=None, tol=0.0001, verbose=0)
correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print(correct/len(X))
#0.6262626262626263 , 62% Accuary , so it increased


#reference reading 
#link :  https://www.datacamp.com/community/tutorials/k-means-clustering-python
