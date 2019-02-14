

# hello world

import matplotlib.pyplot as plt 
improt numpy as np

x = np.linespace(0,5,11)
y = x**2

fig = plt.figure()

axes1 = fig.add_axes{[0.1, 0.1, 0.7, 0.7]}
axes2 = fig.add_axes{[0.5,0.2,0.4,0.4]}

axes1.set_title("Big plot")
axes2.set_title("Small plot")

axes1.plot(x,y)
axes2.plot(y,x)

plt.show()







# pie chart

import matplotlib.pyplot as plt
 
# Data to plot
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
