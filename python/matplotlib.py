

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
