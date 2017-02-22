import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
#from sklearn.metrics import accuracy_score

data = pd.read_csv('ex1data1.txt')
print(data.head(3))

#screenData = data[~np.isnan(data['y'])]


X = np.matrix(data)[:,0]
y = np.matrix(data)[:,1]


X_train , X_test , y_train ,y_test = train_test_split(X,y,test_size=0.3)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train,y_train)

m = clf.coef_
b = clf.intercept_

predictions = clf.predict(X_test)
#from sklearn.metrics import accuracy_score
#print(accuracy_score(y_test,predictions))
'''
acc = clf.score(y_test,predictions)
#print(acc)
print(X_test,predictions,y_test)
'''

print('formula : y = {0}x + {1}'.format(m,b))


plt.scatter(X,y,color='black')
plt.plot(X_test,predictions,color='red',linewidth=3)
plt.show() 