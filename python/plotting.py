

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
