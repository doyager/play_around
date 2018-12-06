
#################################### Typical Steps ####################
# Link: https://towardsdatascience.com/random-forest-in-python-24d0893d51c0


######## 0 # background

"""
# explnation of the data set

data size:
rows: 348
cols : 9

description:

year: 2016 for all data points

month: number for month of the year

day: number for day of the year

week: day of the week as a character string

temp_2: max temperature 2 days prior

temp_1: max temperature 1 day prior

average: historical average max temperature

actual: max temperature measurement           # this is the column we are trying to predict

friend: your friend’s prediction, a random number between 20 below the average and 20 above the average

"""

######## 1 # read data


# Pandas is used for data manipulation
import pandas as pd
# Read in data and display first 5 rows
features = pd.read_csv('temps.csv')
features.head(5)


###### 2 # print shape of data (rows,cols)
print('The shape of our features is:', features.shape)

###### 3 #summary statistics
# Descriptive statistics for each column
features.describe()

###### 4 # Plot data
#TODO


###### 5 # One-Hot Encoding - Categorical to Numerical Data
"""
How to Convert Categorical Data to Numerical Data?
This involves two steps:

Integer Encoding
One-Hot Encoding
1. Integer Encoding
As a first step, each unique category value is assigned an integer value.

For example, “red” is 1, “green” is 2, and “blue” is 3.

This is called a label encoding or an integer encoding and is easily reversible.

For some variables, this may be enough.

The integer values have a natural ordered relationship between each other and machine learning algorithms may be able to understand and harness this relationship.

For example, ordinal variables like the “place” example above would be a good example where a label encoding would be sufficient.

2. One-Hot Encoding
For categorical variables where no such ordinal relationship exists, the integer encoding is not enough.

In fact, using this encoding and allowing the model to assume a natural ordering between categories may result in poor performance or unexpected results (predictions halfway between categories).

In this case, a one-hot encoding can be applied to the integer representation. This is where the integer encoded variable is removed and a new binary variable is added for each unique integer value.

In the “color” variable example, there are 3 categories and therefore 3 binary variables are needed. A “1” value is placed in the binary variable for the color and “0” values for the other colors.

For example:


red,	green,	blue
1,		0,		0
0,		1,		0
0,		0,		1
1
2
3
4
red,	green,	blue
1,		0,		0
0,		1,		0
0,		0,		1
The binary variables are often called “dummy variables” in other fields, such as statistics.


One-Hot Encoding

The first step for us is known as one-hot encoding of the data. This process takes categorical variables, 
such as days of the week and converts it to a numerical representation without an arbitrary ordering. 
Days of the week are intuitive to us because we use them all the time. You will (hopefully) never 
find anyone who doesn’t know that ‘Mon’ refers to the first day of the workweek, but machines do not 
have any intuitive knowledge. What computers know is numbers and for machine learning we must accommodate 
them. We could simply map days of the week to numbers 1–7, but this might lead to the algorithm placing more 
importance on Sunday because it has a higher numerical value. Instead, we change the single column of weekdays
into seven columns of binary data. This is best illustrated pictorially. One hot encoding takes this:


and turns it into


So, if a data point is a Wednesday, it will have a 1 in the Wednesday column and a 0 in all other columns. 
This process can be done in pandas in a single line!
"""
# One-hot encode the data using pandas get_dummies
features = pd.get_dummies(features)
# Display the first 5 rows of the last 12 columns
features.iloc[:,5:].head(5)

#The shape of our data is now 349 x 15 and all of the column are numbers, just how the algorithm likes it!


######## 6 # Features and Targets and Convert Data to Arrays
"""
 we need to separate the data into the features and targets. The target, also known as the label,
 is the value we want to predict, in this case the actual max temperature and the features are all
 the columns the model uses to make a prediction.
"""

# Use numpy to convert to arrays
import numpy as np
# Labels are the values we want to predict
labels = np.array(features['actual'])           #'actual' is the name of the column we are trying to predict
# Remove the labels from the features
# axis 1 refers to the columns
features= features.drop('actual', axis = 1)

# Saving feature names for later use
feature_list = list(features.columns)

# Convert to numpy array
features = np.array(features)



######## 7 # split data : code splits the data sets
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

#####print test & train splits
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)

######## 8 # establish basline
"""
Before we can make and evaluate predictions, we need to establish a baseline, a sensible
measure that we hope to beat with our model. If our model cannot improve upon the baseline,
then it will be a failure and we should try a different model or admit that machine learning
is not right for our problem. The baseline prediction for our case can be the historical max
temperature averages. In other words, our baseline is the error we would get if we simply
predicted the average max temperature for all days.

"""
# The baseline predictions are the historical averages
baseline_preds = test_features[:, feature_list.index('average')]
# Baseline errors, and display average baseline error
baseline_errors = abs(baseline_preds - test_labels)
print('Average baseline error: ', round(np.mean(baseline_errors), 2))

######## 9 # create model and train model 

# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(train_features, train_labels);

######### 10 # test model
# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')


######### 11 # Determine Performance Metrics
"""
To put our predictions in perspective, we can calculate an accuracy using the mean average
percentage error subtracted from 100 %.
"""

# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')
Accuracy: 93.99 %.

######### 12 # visualize


# Import tools needed for visualization
from sklearn.tree import export_graphviz
import pydot
# Pull out one tree from the forest
tree = rf.estimators_[5]
# Import tools needed for visualization
from sklearn.tree import export_graphviz
import pydot
# Pull out one tree from the forest
tree = rf.estimators_[5]
# Export the image to a dot file
export_graphviz(tree, out_file = 'tree.dot', feature_names = feature_list, rounded = True, precision = 1)
# Use dot file to create a graph
(graph, ) = pydot.graph_from_dot_file('tree.dot')
# Write graph to a png file
graph.write_png('tree.png')

############################
#Random Forest


# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(train_features, train_labels);

#Making predictions with out model 
# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

# visualize Random forest
"""
One of the coolest parts of the Random Forest implementation in Skicit-learn is we can
actually examine any of the trees in the forest. We will select one tree, and save the
whole tree as an image.
"""

# Import tools needed for visualization
from sklearn.tree import export_graphviz
import pydot
# Pull out one tree from the forest
tree = rf.estimators_[5]
# Import tools needed for visualization
from sklearn.tree import export_graphviz
import pydot
# Pull out one tree from the forest
tree = rf.estimators_[5]
# Export the image to a dot file
export_graphviz(tree, out_file = 'tree.dot', feature_names = feature_list, rounded = True, precision = 1)
# Use dot file to create a graph
(graph, ) = pydot.graph_from_dot_file('tree.dot')
# Write graph to a png file
graph.write_png('tree.png')




##############################
