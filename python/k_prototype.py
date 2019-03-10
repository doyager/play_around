




############
# stocks.csv , replace space separator with comma

AAPL,738.5,tech,USA
XOM,369.5,nrg,USA
GOOGL	368.2	tech	USA
MSFT	346.7	tech	USA
BRK-A	343.5	fin	USA
WFC	282.4	fin	USA
CHL	282.1	tel	CN
JNJ	279.7	cons	USA
WMT	257.2	cons	USA
VZ	205.2	tel	USA
ORCL	192.1	tech	USA
RDS-A	195.7	nrg	NL



############
Model building:



#!/usr/bin/env python

import numpy as np
from kmodes.kprototypes import KPrototypes

# stocks with their market caps, sectors and countries
syms = np.genfromtxt('stocks.csv', dtype=str, delimiter=',')[:, 0]
X = np.genfromtxt('stocks.csv', dtype=object, delimiter=',')[:, 1:]
X[:, 0] = X[:, 0].astype(float)

kproto = KPrototypes(n_clusters=4, init='Cao', verbose=2)
clusters = kproto.fit_predict(X, categorical=[1, 2])

# Print cluster centroids of the trained model.
print(kproto.cluster_centroids_)
# Print training statistics
print(kproto.cost_)
print(kproto.n_iter_)

for s, c in zip(syms, clusters):
    print("Symbol: {}, cluster:{}".format(s, c))
