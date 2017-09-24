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
- **ml_helpers.py:** Machine Learning helper functions. Adapted from my [Python Machine Learning](https://github.com/GeorgeSeif/Python-Machine-Learning) repository
- **plt_helpers:** Helper functions to make plotting easy in Matplotlib.
- **explore_wine_data.py:** Exploratory data analysis of the wine dataset from sklearn using visualisations. Includes data analysis using histogram, scatterplot, bee swarm plot, and cumulative distribution function.
- **statistics_iris.py:** Compute various statistics of the iris dataset features such as histogram, min, max, median, mean, and variance.
- **covariance_boston.py:** Compute the covariance matrix of the Boston Housing dataset. These matrices can sometimes give faster insight into which variables are related rather than creating scatter plots.

## Information

### Visualisations
- **Histogram:** A histogram is a graphical method of displaying quantitative data. A histogram displays the single quantitative variable along the x axis and frequency of that variable on the y axis. The distinguishing feature of a histogram is that data is grouped into "bins", which are intervals on the x axis.
- **Scatterplot:** A scatter plot is a graphical method of displaying the relationship between data points. Each feature variable is assigned an axis. Each data point in the dataset is then plotted based on its feature values.
- **Beeswarm Plot:** A Beeswarm plot is a two-dimensional visualisation technique where data points are plotted relative to a fixed reference axis so that no two datapoints overlap. The beeswarm plot is a useful technique when we wish to see not only the measured values of interest for each data point, but also the distribution of these values. 
- **Cumulative Distribution Function:** The cumulative distribution function (cdf) is the probability that a variable takes a value less than or equal to x. For example, we may wish to see what percentage of the data has a certain feature variable that is less than or equal to x.
- **Bar Plots:** Classical bar plots that are good for visualisation and comparison of different data statistics, especially comparing statistics of feature variables.

### Statistics
- **Mean and Median:** Both of these show a type of "average" or "center" value for a particular feature variable. The mean is the more literal and precise center; however median is much more robust to outliers which may pull the mean value calculation far away from the majority of the values. 
- **Variance and Standard Deviation:** Useful for seeing to what degree the feature variable of a dataset varies across all example i.e are most of the values for this particular feature variable similar across the dataset or are they all very different.  
- **Kurtosis:** Measures the "sharpness" of a distribution. If a distribution has a high kurtosis value (>3) then it's data will be highly concentrated around the same value. If K=3 then the distribution is normal (zero-mean, unit-variance). If K < 3 then the values of the distribution will be spread out. 
- **Skewness:** Measures the asymmetry of a distribution. Positive skewness means values are concentrated on the left (lower); negative skewness means values are concentrated on the right (higher). 
- **Covariance:** The covariance of two variables measures how "correlated" they are. If the two variables have a positive covariance, then one when variable increases so does the other; with a negative covariance the values of the feature variables will change in opposite directions. 
- **Correlation:** Correlation is simply the normalized (scaled) covariance where we divide by the product of the standard deviation of the two variables being analyzed. While the covariance always changes with changes in units and lies between -\infty and \infty, corellation stays the same with any units and lies between -1 and 1. As stated above, covariance measures variables that have different units of measurement. Using covariance, you could determine whether units were increasing or decreasing, but it was impossible to measure the degree to which the variables moved together because covariance does not use one standard unit of measurement. To measure the degree to which variables move together, you must use correlation. The magnitude of the correlation tells us how strongly the features are correlated. If the _correlation coefficient_ is one, the variables have a perfect positive correlation. This means that if one variable moves a given amount, the second moves proportionally in the same direction. A positive correlation coefficient less than one indicates a less than perfect positive correlation, with the strength of the correlation growing as the number approaches one. If _correlation coefficient is zero_, no relationship exists between the variables. If one variable moves, you can make no predictions about the movement of the other variable; they are uncorrelated.
If _correlation coefficient is –1_, the variables are perfectly negatively correlated (or inversely correlated) and move in opposition to each other. If one variable increases, the other variable decreases proportionally. A negative correlation coefficient greater than –1 indicates a less than perfect negative correlation, with the strength of the correlation growing as the number approaches –1.
- **PCA Dimensionality Reduction:** Principal Component Analysis (PCA) is a technique commonly used for dimensionality reduction. PCA computes the feature vectors along which the data has the highest variance. Since these feature vectors have the highest variance they also hold most of the information that the data represents. Therefore we can project the data on to these feature vectors, reducing the dimensionality of the data which makes analysis easier and more clear. 
- **Data Shuffling:** Shuffling the data prior to applying a machine learning algorithm has been proven to improve the performance. 


### Pandas Data Science

#### Basic Dataset Information
- **Read in a CSV dataset:** `pd.DataFrame.from_csv("csv_file")` OR `pd.read_csv("csv_file")`
- **Read in an Excel dataset:** `pd.read_excel("excel_file")`
- **Basic dataset feature info:** `df.info()`
- **Basic dataset statistics:** `print(df.describe())` 
- **Print dataframe in a table:** `print(tabulate(print_table, headers=headers))` where "print_table" is a list of lists and "headers" is a list of the string headers

#### Basic Data Handling
- **Drop missing data:** `df.dropna(axis=0, how='any')` Return object with labels on given axis omitted where alternately any or all of the data are missing
- **Replace missing data:** `df.replace(to_replace=None, value=None)` Replace values given in "to_replace" with "value".
- **Check for NANs:** `pd.isnull(object)` Detect missing values (NaN in numeric arrays, None/NaN in object arrays)
- **Drop a feature:** `df.drop('feature_variable_name', axis=1)` axis is either 0 for rows, 1 for columns
- **Convert object type to float:** `pd.to_numeric(df["feature_name"], errors='coerce')` Convert object types to numeric to be able to perform compuations
- **Convert DF to numpy array:** `df.as_matrix()`
- **Get first "n" rows:** `df.head([n])`
- **Get data by feature name:** `df.loc[feature_name]`

#### Basic Plotting
- **Area plot:** `df.plot.area([x, y])`	
- **Vertical bar plot:** `df.plot.bar([x, y])`
- **Horizontal bar plot:** `df.plot.barh([x, y])`	
- **Boxplot:** `df.plot.box([by])`
- **Histogram:** `df.plot.hist([by, bins])`
- **Line plot:** `df.plot.line([x, y])`	
- **Pie chart:** `df.plot.pie([y])`	



### Examples
![alt text](https://github.com/GeorgeSeif/Data-Science-Python/blob/master/Images/explore_wine_scattermatrix.png)