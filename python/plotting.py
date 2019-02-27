

# Line graph 
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.xlabel('Progamming Languages')
plt.ylabel('Counts')
plt.show()
'''
You may be wondering why the x-axis ranges from 0-3 and the y-axis from 1-4. If you provide a single
list or array to the plot() command, matplotlib assumes it is a sequence of y values, and automatically
generates the x values for you. Since python ranges start with 0, the default x vector has the same length
as y but starts with 0. Hence the x data are [0,1,2,3].
'''



# Categorical plotting
# 1 * 3 plot , plotting BAR & Scatter & Line grpahs side by side with same set of data
# Link : https://matplotlib.org/gallery/lines_bars_and_markers/categorical_variables.html
import matplotlib.pyplot as plt

data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')




# Categorical plotting - Example with data

import matplotlib.pyplot as plt
import collections


code_languages =[ "java","java","js","js","js","c","c","c","c","c","c","py","py","py","py"]
#print(code_lines)
print(code_languages)
print("count : "+str(count))

#to convert code_languages list to key values pair of counts
print("code_languages stats: ")
counter=collections.Counter(code_languages)
print(counter)
# o/p: Counter({'c': 6, 'py': 4, 'js': 3, 'java': 2})
# we can even assign the value to dictornray 
# counter={'c': 28290, 'js': 15360, 'java': 3177, 'py': 2407}




names = list(counter.keys())
values = list(counter.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Count per Group Plotting')
plt.show()  # this will finally show the graph



# bar graph & pie chart for same data


    #bar graph
          import pandas as pd
          import numpy as np
          import copy
          %matplotlib inline
          df_flights = pd.read_csv('https://raw.githubusercontent.com/ismayc/pnwflights14/master/data/flights.csv')
          cat_df_flights = df_flights.select_dtypes(include=['object']).copy()

          %matplotlib inline
          import seaborn as sns
          import matplotlib.pyplot as plt
          carrier_count = cat_df_flights['carrier'].value_counts()
          sns.set(style="darkgrid")
          sns.barplot(carrier_count.index, carrier_count.values, alpha=0.9)
          plt.title('Frequency Distribution of Carriers')
          plt.ylabel('Number of Occurrences', fontsize=12)
          plt.xlabel('Carrier', fontsize=12)
          plt.show()
          
     #pie chart

          labels = cat_df_flights['carrier'].astype('category').cat.categories.tolist()
          counts = cat_df_flights['carrier'].value_counts()
          sizes = [counts[var_cat] for var_cat in labels]
          fig1, ax1 = plt.subplots()
          ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True) #autopct is show the % on plot
          ax1.axis('equal')
          plt.show()
