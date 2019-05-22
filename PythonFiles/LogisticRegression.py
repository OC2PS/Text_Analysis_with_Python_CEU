
# Data Imports
import pandas as pd


# Plot imports
import seaborn as sns
sns.set_style('whitegrid')

# Machine Learning Imports
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# For evaluating our ML results
from sklearn import metrics

import os
os.chdir("/Users/ariedamuco/Dropbox (CEU Econ)/TextAnalysisCEU")
data= pd.read_csv("Input/Social_Network_Ads.csv")

data.info()

#summary statistics on the data
data.describe()

#columns names
data.columns

# Preview
data.head()
# Preview
data.tail()

# DataFrame Check
data

# Create a set of dummy variables from the sex variable
df_sex = pd.get_dummies(data['Gender'])
# Join the dummy variables to the main dataframe

df= pd.concat([data, df_sex], axis=1)


#apparently males, older and richer are more likely to purchase
df.groupby('Purchased').mean()

#some graphical analysis
ax=data.hist(column='EstimatedSalary', by='Purchased')
ax.set_xlabel('EstimatedSalary')
ax.set_ylabel('Purchased')


data.hist(column='Age', by='Purchased')



#drop user id and gender and male as we do not need them , axis=1 along the columns 
df.drop(df.columns[[0, 1,-1]], axis=1, inplace=True)

#inplace : boolean, default False. Modify the DataFrame in place (do not create a new object)
"""
The reason to drop male is to avoid multicollinearity.
Multicollinearity occurs due to the dummy variables we created. 

"""
#Set Y as Target class, Purchased
Y = df.Purchased

# Preview
Y.head()

#get the rest of the observations in the X vector
X=df.drop(['Purchased'],axis=1)


#Just like we did for the Linear Regression case, we splitt
# our data into training and testing data sets using SciKit Learn's built-in 
#train_test_split method

# Split the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=103)

# Make a new log_model
logistic = LogisticRegression()

# Now fit the new model
logistic.fit(X_train, Y_train)


# Predict the classes of the testing data set
class_predict = logistic.predict(X_test)

# Compare the predicted classes to the actual test classes
print ("METRIC SCORE: ", metrics.accuracy_score(Y_test,class_predict))

#72 percent accuracy score which is an ok score. Maybe with inclusion of more predictors
#we could improve the fit. Check fit better.

from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(Y_test,class_predict).ravel()



