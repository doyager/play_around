


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




#Silhouette analysis

"""
Silhouette analysis can be used to study the separation distance between the resulting clusters.
The silhouette plot displays a measure of how close each point in one cluster is to points in the neighboring clusters 
and thus provides a way to assess parameters like number of clusters visually. This measure has a range of [-1, 1].

Silhouette coefficients (as these values are referred to as) near +1 indicate that the sample is far away from 
the neighboring clusters. A value of 0 indicates that the sample is on or very close to the decision boundary
between two neighboring clusters and negative values indicate that those samples might have been assigned 
to the wrong cluster.

+1  : indicate that the sample is far away from the neighboring clusters
0   :indicates that the sample is on or very close to the decision boundary between two neighboring clusters
-ve : negative values indicate that those samples might have been assigned to the wrong cluster.

Example :
In this example the silhouette analysis is used to choose an optimal value for n_clusters. 
The silhouette plot shows that the n_clusters value of 3, 5 and 6 are a bad pick for the given data due 
to the presence of clusters with below average silhouette scores and also due to wide fluctuations in the 
size of the silhouette plots. Silhouette analysis is more ambivalent in deciding between 2 and 4.

For n_clusters = 2 The average silhouette_score is : 0.7049787496083262
For n_clusters = 3 The average silhouette_score is : 0.5882004012129721
For n_clusters = 4 The average silhouette_score is : 0.6505186632729437
For n_clusters = 5 The average silhouette_score is : 0.56376469026194

"""

# link : https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#sphx-glr-auto-examples-cluster-plot-kmeans-silhouette-analysis-py


from __future__ import print_function

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
 
#Generating the sample data from make_blobs
# This particular setting has one distinct cluster and 3 clusters placed close
# together.
X, y = make_blobs(n_samples=500,
                  n_features=2,
                  centers=4,
                  cluster_std=1,
                  center_box=(-10.0, 10.0),
                  shuffle=True,
                  random_state=1)  # For reproducibility

range_n_clusters = [2, 3, 4, 5, 6]

for n_clusters in range_n_clusters:
    # Initialize the clusterer with n_clusters value and a random generator
    # seed of 10 for reproducibility.
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(X)

    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    silhouette_avg = silhouette_score(X, cluster_labels)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg
          
          
          
#####################
# Errors
 ###########
          
          
  """
  1.    memory error with  silhouette_score
  
  
           silhouette_avg = silhouette_score(X_np, cluster_labels)
python3(48549,0x7fff8fe69380) malloc: *** mach_vm_map(size=379372547317760) failed (error code=3)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/mac/workspace/softwares/installed/anaconda3/anaconda3/lib/python3.6/site-packages/sklearn/metrics/cluster/unsupervised.py", line 101, in silhouette_score
    return np.mean(silhouette_samples(X, labels, metric=metric, **kwds))
  File "/Users/mac/workspace/softwares/installed/anaconda3/anaconda3/lib/python3.6/site-packages/sklearn/metrics/cluster/unsupervised.py", line 169, in silhouette_samples
    distances = pairwise_distances(X, metric=metric, **kwds)
  File "/Users/mac/workspace/softwares/installed/anaconda3/anaconda3/lib/python3.6/site-packages/sklearn/metrics/pairwise.py", line 1247, in pairwise_distances
    return _parallel_pairwise(X, Y, func, n_jobs, **kwds)
  File "/Users/mac/workspace/softwares/installed/anaconda3/anaconda3/lib/python3.6/site-packages/sklearn/metrics/pairwise.py", line 1090, in _parallel_pairwise
    return func(X, Y, **kwds)
  File "/Users/mac/workspace/softwares/installed/anaconda3/anaconda3/lib/python3.6/site-packages/sklearn/metrics/pairwise.py", line 246, in euclidean_distances
    distances = safe_sparse_dot(X, Y.T, dense_output=True)
  File "/Users/mac/workspace/softwares/installed/anaconda3/anaconda3/lib/python3.6/site-packages/sklearn/utils/extmath.py", line 140, in safe_sparse_dot
    return np.dot(a, b)
MemoryError


"""
          
          

