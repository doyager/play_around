

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
