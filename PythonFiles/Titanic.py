

import os
import pandas as pd
<<<<<<< HEAD
os.chdir("/Users/ariedamuco/Downloads")
=======
os.chdir("")
>>>>>>> 4841117c99172e801e581196b0b1f63179338a76
titanic_train= pd.read_csv("train.csv")

titanic_train.info()
titanic_train.describe()
titanic_train.columns
titanic_train.head()
titanic_train.tail()
titanic_train



titanic_train.isnull()
import seaborn as sns
sns.heatmap(titanic_train.isnull(), cmap="Oranges", cbar=False, yticklabels=False)


titanic_train.hist(column='Age', by='Survived')
sns.countplot(x='Survived', data=titanic_train, color="Grey")

sns.countplot(x='Survived', hue="Sex", data=titanic_train, palette="Purples")
sns.countplot(x='Survived', hue="Pclass", data=titanic_train, palette="Purples")

sns.distplot(titanic_train["Age"].dropna(), kde=False, bins=30)

titanic_train.Age.plot.hist(bins=30)
sns.countplot(x='SibSp', data=titanic_train, palette="Purples")
titanic_train.Fare.plot.hist(bins=30)


titanic_train['male']=pd.get_dummies(titanic_train['Sex'], drop_first=True)
titanic_train[['Port C','Port Q']]=pd.get_dummies(titanic_train['Embarked'])[["C","Q"]]
titanic_train.drop(['Sex','Embarked', 'Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1, inplace=True)

titanic_train['Age']=titanic_train['Age'].fillna(titanic_train['Age'].mean())
titanic_train=titanic_train.dropna()

titanic_test= pd.read_csv("test.csv")


titanic_test['male']=pd.get_dummies(titanic_test['Sex'], drop_first=True)
titanic_test[['Port C','Port Q']]=pd.get_dummies(titanic_test['Embarked'])[["C","Q"]]
titanic_test.drop(['Sex','Embarked', 'Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1, inplace=True)

titanic_test['Age']=titanic_test['Age'].fillna(titanic_test['Age'].mean())
titanic_test=titanic_test.dropna()
X_train=titanic_train.drop('Survived', axis=1)
Y_train=titanic_train['Survived']

from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression()

logistic.fit(X_train, Y_train)


class_predict = logistic.predict(titanic_test)


