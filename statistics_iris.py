import pandas as pd
import numpy as np
from scipy import stats
from tabulate import tabulate
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def compute_list_median(x):
	x = np.sort(x)

	tmp = round(0.5 * x.shape[0])

	if x.shape[0] % 2:
	    median = x[tmp - 1]
	else:
	    median = x[tmp - 1] + (x[tmp] - x[tmp - 1]) / 2.
	    
	return median

# NOTE that this loads as a dictionairy
iris_data = load_iris()

train_data = np.array(iris_data.data)
train_labels = np.array(iris_data.target)

num_features = iris_data.data.shape[1]
unique_labels = np.unique(train_labels)
num_classes = len(unique_labels)


print("The iris dataset has " + str(num_features) + " features")
print(iris_data.feature_names)
print("The iris dataset has " + str(num_classes) + " classes")
print(iris_data.target_names)


# Strip for easier indexing
for i in range(len(iris_data.feature_names)):
	iris_data.feature_names[i] = iris_data.feature_names[i].replace(' (cm)','')

# Put everything into a Pandas DataFrame
data = pd.DataFrame(data=np.c_[train_data, train_labels], columns=iris_data.feature_names + ['class'])
# print(tabulate(data, headers='keys', tablefmt='psql'))



# Create histogram
hist_feature_name='sepal length'
bin_edges = np.arange(0, data[hist_feature_name].max() + 1, 1)
fig = plt.hist(data[hist_feature_name], bins=bin_edges)

plt.ylabel('count')
plt.xlabel(hist_feature_name)
# plt.show()



# Compute the mean sepal length and draw it on the same histogram
sepal_length_values = data['sepal length'].values 
mean_sepal_length = sum(i for i in sepal_length_values) / len(sepal_length_values)
mean_sepal_length = np.mean(sepal_length_values)
print("Mean sepal length (cm) = " + str(mean_sepal_length))

plt.axvline(mean_sepal_length, color='green', linewidth=2)



# Compute the variance of the sepal length feature and draw it on the same histogram
variance_sepal_length = sum([(i - mean_sepal_length)**2 for i in sepal_length_values]) / (len(sepal_length_values) - 1)
variance_sepal_length = np.var(sepal_length_values, ddof=1)

print("Variance of sepal length (cm) = " + str(variance_sepal_length))

plt.axvline(mean_sepal_length + variance_sepal_length, color='red', linewidth=2)
plt.axvline(mean_sepal_length - variance_sepal_length, color='red', linewidth=2)


# Other values
min_sepal_length = np.min(sepal_length_values)
print("Minimum sepal length (cm) = " + str(min_sepal_length))

max_sepal_length = np.max(sepal_length_values)
print("Maximum sepal length (cm) = " + str(max_sepal_length))

sorted_sepal_length_values = np.sort(sepal_length_values)
percentile_20th = sorted_sepal_length_values[round(0.25 * sorted_sepal_length_values.shape[0]) + 1]
percentile_80th = sorted_sepal_length_values[round(0.75 * sorted_sepal_length_values.shape[0]) + 1]
print("20th Percentile sepal length (cm) = " + str(percentile_20th))
print("80th Percentile sepal length (cm) = " + str(percentile_80th))

median_sepal_length = compute_list_median(sepal_length_values)
median_sepal_length = np.median(sepal_length_values)
print("Median sepal length (cm) = " + str(median_sepal_length))


plt.show()