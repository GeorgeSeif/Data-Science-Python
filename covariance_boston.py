import pandas as pd
import numpy as np
from scipy import stats
import seaborn.apionly as sns
from tabulate import tabulate
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

import ml_helpers as helpers

# NOTE that this loads as a dictionairy
boston_data = load_boston()

train_data = np.array(boston_data.data)
train_labels = np.array(boston_data.target)

num_features = boston_data.data.shape[1]
unique_labels = np.unique(train_labels)
num_classes = len(unique_labels)


print("The boston dataset has " + str(num_features) + " features")
print(boston_data.feature_names)



# Put everything into a Pandas DataFrame
data = pd.DataFrame(data=np.c_[train_data], columns=boston_data.feature_names)
# print(tabulate(data, headers='keys', tablefmt='psql'))



# Compute the covariance matrix
cov_mat_boston = np.cov(train_data.T)
print("Covariance matrix")
print(cov_mat_boston)



# Normalize the data and then recompute the covariance matrix
normalized_train_data = helpers.normalize_data(train_data)
normalized_cov_mat_boston = np.cov(normalized_train_data.T)
print("Normalized data covariance matrix")
print(normalized_cov_mat_boston)



# create scatterplot matrix
fig = sns.pairplot(data=data, hue='CRIM')

plt.show()