# Python Data Science

## Description
A collection of data science scripts for data analysis in Python. 

Python libraries used:
- Numpy
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
- **explore_wine_data.py:** Exploratory data analysis of the wine dataset from sklearn. Includes data analysis using histogram, scatterplot, bee swarm plot, and cumulative distribution function.

### Information

#### Exploratory Data Analysis
- **Histogram:** A histogram is a graphical method of displaying quantitative data. A histogram displays the single quantitative variable along the x axis and frequency of that variable on the y axis. The distinguishing feature of a histogram is that data is grouped into "bins", which are intervals on the x axis.
- **Scatterplot:** A scatter plot is a graphical method of displaying the relationship between data points. Each feature variable is assigned an axis. Each data point in the dataset is then plotted based on its feature values.
- **Beeswarm Plot:** A Beeswarm plot is a two-dimensional visualisation technique where data points are plotted relative to a fixed reference axis so that no two datapoints overlap. The beeswarm plot is a useful technique when we wish to see not only the measured values of interest for each data point, but also the distribution of these values. 
- **Cumulative Distribution Function:** The cumulative distribution function (cdf) is the probability that a variable takes a value less than or equal to x. For example, we may wish to see what percentage of the data has a certain feature variable that is less than or equal to x.

#### Examples
![alt text](https://github.com/GeorgeSeif/Data-Science-Python/blob/master/Images/explore_wine_histogram.png)
![alt text](https://github.com/GeorgeSeif/Data-Science-Python/blob/master/Images/explore_wine_scattermatrix.png)
![alt text](https://github.com/GeorgeSeif/Data-Science-Python/blob/master/Images/explore_wine_beeswarm.png)
![alt text](https://github.com/GeorgeSeif/Data-Science-Python/blob/master/Images/explore_wine_cdf.png)