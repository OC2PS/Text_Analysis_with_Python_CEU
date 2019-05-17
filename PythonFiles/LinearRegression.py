
#import libraries
import pandas as pd
from pandas import DataFrame
import os
#YOUR directory
os.chdir("/Users/ariedamuco/Dropbox (CEU Econ)/TextAnalysisCEU")
#from sklearn import linear_model
data= pd.read_csv("Input/USA_Housing.csv")

#let's get the information about the data
data.info()

#summary statistics on the data
data.describe()

#columns names
data.columns

#get the y variable

y=data['Price']

import matplotlib.pyplot as plt

#plot the outcome variable
plt.hist(data['Price'], bins=30)
plt.xlabel('Housing Prices')
plt.ylabel('Frequency')
plt.savefig('Outputs/HistPrice.png')


#select all up to the last two columns, in x we are going to store our regressors (features)
x=data.iloc[:, 1:6]

#out of date command
#x=data1.ix[:,1:6]

#explore the regressors
x.head()

import seaborn as sns

sns.pairplot(data)
plt.savefig('Outputs/pairwise_corr.png')

#heatmap of the correlations
#sns.heatmap(data.corr(), annot=True)


from sklearn.model_selection import train_test_split

#make the train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=850112)

"""
http://machinelearningmastery.com/evaluate-performance-machine-learning-algorithms-python-using-resampling/
Train and Test Sets.
K-fold Cross Validation.
Leave One Out Cross Validation.
Repeated Random Test-Train Splits
"""

from sklearn import linear_model

#create the linear regression object
reg = linear_model.LinearRegression()

#use method fit in order to fit the model in the training data
reg.fit(x_train, y_train)

#show coefficients
reg.coef_

#show intercept
reg.intercept_ 


# Set a DataFrame from the Features in the original dataset
coeff_data = DataFrame(data.columns)
#attribute a name of the colum
coeff_data.columns = ['Features']

# Set a new column lining up the coefficients from the linear regression
coeff_data["Coefficient Estimate"] = pd.Series(reg.coef_)

# Show
coeff_data
#alternatively you can do:
#estimated_coeff=pd.DataFrame(reg.coef_, x.columns, columns=['Features'])

#we want to check correctedness of our model using the testing data
yhat=reg.predict(x_test)
yhat_train= reg.predict(x_train)

plt.scatter(yhat, y_test)



#distribution of the residuals
#create the residuals
error=yhat-y_test
sns.distplot(error)
#plt.hist(error, bins=30)
plt.show()

"""
Usually, to evaluate the models, we use the root mean squared error.
Other ways to evaluate models are mean absolute error (MAE) and mean squared error (MSE)
MSE is preferred to MAE because it punished harsher larger errors
RMSE is preferred to the above because is interpretable in units of y
"""
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, yhat, multioutput='raw_values')

import numpy as np
np.sqrt(mean_squared_error(y_test, yhat, multioutput='raw_values'))

plt.scatter(error, y_test)




# Using seabron to create a linear fit
#sns.lmplot('Price','Avg. Area Income', data=data)
