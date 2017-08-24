# Python Data Science

## Description
A collection of data science scripts for data analysis in Python. Please also see my related repository [Python Machine Learning](https://github.com/GeorgeSeif/Python-Machine-Learning) which contains many implementations of Machine Learning algorithms including _regression_, _classification_, and _clustering_. The algorithms are implemented in two ways: from scratch in Python and using Scikit Learn functions. 

Python libraries used:
- Numpy
- Scipy
- Scikit Learn
- Pandas
- Seaborn
- Matplotlib

## Installation
To install all of the libraries, run the commands in the "install.txt" file. These are:

- `sudo apt-get install python-pip`
- `sudo pip install numpy scipy`
- `sudo pip install pandas`
- `sudo apt-get install python-matplotlib`
- `sudo pip install -U scikit-learn`
- `sudo pip install tabulate`

## Files
- **helpers.py:** Helper functions. adapted from the [Python Machine Learning](https://github.com/GeorgeSeif/Python-Machine-Learning) repository
- **explore_wine_data.py:** Exploratory data analysis of the wine dataset from sklearn using visualisations. Includes data analysis using histogram, scatterplot, bee swarm plot, and cumulative distribution function.
- **statistics_iris.py:** Compute various statistics of the iris dataset features such as histogram, min, max, median, mean, and variance.
- **covariance_boston.py:** Compute the covariance matrix of the Boston Housing dataset. These matrices can sometimes give faster insight into which variables are related rather than creating scatter plots.

## Information

#### Visualisations
- **Histogram:** A histogram is a graphical method of displaying quantitative data. A histogram displays the single quantitative variable along the x axis and frequency of that variable on the y axis. The distinguishing feature of a histogram is that data is grouped into "bins", which are intervals on the x axis.
- **Scatterplot:** A scatter plot is a graphical method of displaying the relationship between data points. Each feature variable is assigned an axis. Each data point in the dataset is then plotted based on its feature values.
- **Beeswarm Plot:** A Beeswarm plot is a two-dimensional visualisation technique where data points are plotted relative to a fixed reference axis so that no two datapoints overlap. The beeswarm plot is a useful technique when we wish to see not only the measured values of interest for each data point, but also the distribution of these values. 
- **Cumulative Distribution Function:** The cumulative distribution function (cdf) is the probability that a variable takes a value less than or equal to x. For example, we may wish to see what percentage of the data has a certain feature variable that is less than or equal to x.
- **Bar Plots:** Classical bar plots that are good for visualisation and comparison of different data statistics, especially comparing statistics of feature variables.

#### Statistics
- **Mean and Median:** Both of these show a type of "average" or "center" value for a particular feature variable. The mean is the more literal and precise center; however median is much more robust to outliers which may pull the mean value calculation far away from the majority of the values. 
- **Variance and Standard Deviation:** Useful for seeing to what degree the feature variable of a dataset varies across all example i.e are most of the values for this particular feature variable similar across the dataset or are they all very different.  
- **Covariance Matrix:** The covariance of two variables measures how "correlated" they are. If the two variables have a positive covariance, then one when variable increases so does the other; with a negative covariance the values of the feature variables will change in opposite directions. The magnitude of the covariance determines how strongly the features are correlated. A high covariance value means that when one of the feature variables changes by an amount x, the other will change by an amount very close to x; vice versa for low covariance values. 
- **PCA Dimensionality Reduction:** Principal Component Analysis (PCA) is a technique commonly used for dimensionality reduction. PCA computes the feature vectors along which the data has the highest variance. Since these feature vectors have the highest variance they also hold most of the information that the data represents. Therefore we can project the data on to these feature vectors, reducing the dimensionality of the data which makes analysis easier and more clear. 
- **Data Shuffling:** Shuffling the data prior to applying a machine learning algorithm has been proven to improve the performance. 


#### Examples
![alt text](https://github.com/GeorgeSeif/Data-Science-Python/blob/master/Images/explore_wine_scattermatrix.png)