import pandas as pd  #importing the data from the text file
import numpy as np   #we can perform matrix operations using this library
from sklearn.linear_model import LinearRegression  #the main library to perform Linear Regression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

#loading the data into a variable data
data = pd.read_csv('ex1data2.txt')
X = np.matrix(data)[:,0:2]  # assinging features to X
y = np.matrix(data)[:,2]    #assigning labels to y 

#spliting train and test data for better verification
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.3)

clf = LinearRegression()
clf.fit(X_train,y_train)  #training the model with the fit method
 
pred = clf.predict(X_test)  # we can now predict the random values we kept aside

m = clf.coef_
b = clf.intercept_

print(m,b)
