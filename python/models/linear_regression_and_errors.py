let’s create a class to capture the four key statistics about our data.

######################
# data genertion :

import numpy as np

# reproducibility
np.random.seed(10)

# generate data
babies = range(10)
months = np.arange(13)
data = [(month, np.dot(month, 24.7) + 96 + np.random.normal(loc=0, scale=20))
        for month in months
        for baby in babies]
month_data = [element[0] for element in data]
weight_data = [element[1] for element in data]

# model
from sklearn.linear_model import LinearRegression

X = np.array(month_data).reshape(-1,1)
y = weight_data

lr = LinearRegression(fit_intercept=True)
lr.fit(X, y)



######################

#error metrics :

#Metrics To Assess Model
#We will investigate four key metrics:
#Sum of Squared Errors (SSE)
#Total Sum of Squares (SST)
#R^2
#Adjusted R^2


class Stats:

   def __init__(self, X, y, model):
       self.data = X
       self.target = y
       self.model = model
       ## degrees of freedom population dep. variable variance
       self._dft = X.shape[0] - 1
       ## degrees of freedom population error variance
       self._dfe = X.shape[0] - X.shape[1] - 1

   def sse(self):
       '''returns sum of squared errors (model vs actual)'''
       squared_errors = (self.target - self.model.predict(self.data)) ** 2
       return np.sum(squared_errors)

   def sst(self):
       '''returns total sum of squared errors (actual vs avg(actual))'''
       avg_y = np.mean(self.target)
       squared_errors = (self.target - avg_y) ** 2
       return np.sum(squared_errors)

   def r_squared(self):
       '''returns calculated value of r^2'''
       return 1 - self.sse()/self.sst()

   def adj_r_squared(self):
       '''returns calculated value of adjusted r^2'''
       return 1 - (self.sse()/self._dfe) / (self.sst()/self._dft)

#print function 
def pretty_print_stats(stats_obj):
   '''returns report of statistics for a given model object'''
   items = ( ('sse:', stats_obj.sse()), ('sst:', stats_obj.sst()),
            ('r^2:', stats_obj.r_squared()), ('adj_r^2:', stats_obj.adj_r_squared()) )
   for item in items:
       print('{0:8} {1:.4f}'.format(item[0], item[1]))
Now the report.

stats = Stats(X, y, lr)
pretty_print_stats(stats)
