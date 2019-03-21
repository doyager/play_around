
#link : https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html
# https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html


import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier

# Build a classification task using 3 informative features
X, y = make_classification(n_samples=1000,
                           n_features=10,
                           n_informative=3,
                           n_redundant=0,
                           n_repeated=0,
                           n_classes=2,
                           random_state=0,
                           shuffle=False)
