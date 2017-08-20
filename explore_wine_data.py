import pandas as pd
import numpy as np
from tabulate import tabulate
import seaborn.apionly as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Read in the data
# NOTE that this loads as a dictionairy
wine_data = load_wine()

train_data = np.array(wine_data.data)
train_labels = np.array(wine_data.target)

num_features = wine_data.data.shape[1]
unique_labels = np.unique(train_labels)
num_classes = len(unique_labels)


print("The wine dataset has " + str(num_features) + " features")
print(wine_data.feature_names)
print("The wine dataset has " + str(num_classes) + " classes")
print(wine_data.target_names)


# Put everything into a Pandas DataFrame
data = pd.DataFrame(data=np.c_[train_data, train_labels], columns=wine_data.feature_names + ['class'])
# print(tabulate(data, headers='keys', tablefmt='psql'))



# Create histogram
hist_feature_name='color_intensity'
bin_edges = np.arange(0, data[hist_feature_name].max() + 1, 1)
fig = plt.hist(data[hist_feature_name], bins=bin_edges)

plt.ylabel('count')
plt.xlabel(hist_feature_name)
plt.show()



# Create scatterplot
scatter_feature_name_1='color_intensity'
scatter_feature_name_2='alcohol'
fig = plt.scatter(data[scatter_feature_name_1], data[scatter_feature_name_2])

plt.xlabel(scatter_feature_name_1)
plt.ylabel(scatter_feature_name_2)
plt.show()



# Create scatterplot matrix
fig = sns.pairplot(data=data[['alcohol', 'color_intensity', 'malic_acid', 'magnesium', 'class']], hue='class')

plt.show()



# Create bee swarm plot
sns.swarmplot(x='class', y='total_phenols', data=data)
plt.show()




# Cumulative Distribution Function Plots


# Sort and normalize data
x = np.sort(data['hue'])
y = np.arange(1, x.shape[0] + 1, dtype='float32') / x.shape[0]

plt.plot(x, y, marker='o', linestyle='')

plt.ylabel('ECDF')
plt.xlabel('hue')

eightieth_percentile = x[y <= 0.75].max()

plt.axhline(0.75, color='black', linestyle='--')
plt.axvline(eightieth_percentile, color='black', label='75th percentile')
plt.legend()
plt.show()