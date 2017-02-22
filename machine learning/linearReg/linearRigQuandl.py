import quandl
import pandas as pd
import math	
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression

data = quandl.get("WIKI/GOOGL")
data = data[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

data['HL_PCT'] = (data['Adj. High'] - data['Adj. Low']) / data['Adj. Low'] * 100
data['OC_PCT'] = (data['Adj. Close'] - data['Adj. Open']) / data['Adj. Open'] * 100

data = data[['Adj. Close','HL_PCT','OC_PCT','Adj. Volume']]
#print(data.head())

forecast_col = 'Adj. Close'
data.fillna(-99999,inplace=True)

forecast_out = int(math.ceil(0.005*len(data))) #moves the Adj. Close values by 17 rows to top

data['label'] = data[forecast_col].shift(-forecast_out)
data.dropna(inplace=True)

X = np.array(data.drop(['label'],1))
y = np.array(data['label'])
X = preprocessing.scale(X)

X_train , X_test , y_train , y_test = cross_validation.train_test_split(X , y , test_size=0.3)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train,y_train)

accuracy = clf.score(X_test,y_test)

print(accuracy) 