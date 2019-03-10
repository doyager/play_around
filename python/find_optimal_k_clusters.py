


#Elbow method

"""

For each k value, we will initialise k-means and use the inertia attribute to 
identify the sum of squared distances of samples to the nearest cluster centre.


As k increases, the sum of squared distance tends to zero. Imagine we set k to its maximum 
value n (where n is number of samples) each sample will form its own cluster meaning sum of 
squared distances equals zero.
Below is a plot of sum of squared distances for k in the range specified above. If the plot 
looks like an arm, then the elbow on the arm is optimal k.

"""

Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(data_transformed)
    Sum_of_squared_distances.append(km.inertia_)


plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()



