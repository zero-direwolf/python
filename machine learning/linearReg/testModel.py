import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from matplotlib import pyplot as plt

data = pd.read_csv('ex1data1.txt')
X = np.matrix(data)[:,0]
y = np.matrix(data)[:,1]

X_train , X_test , y_train ,y_test = train_test_split(X,y,test_size=0.3)

clf = LinearRegression()
clf.fit(X_train,y_train)

# y = mx + b
m = clf.coef_
b = clf.intercept_

predictions  = clf.predict(X_test)

print('formula : y = {0}x + {1}'.format(m,b))
pred = ((X_test * m) + b)
print(len(pred))
#print(len(predictions))

plt.scatter(X,y,color='black')
plt.plot(X_test,pred,'r. ',markersize=5,)
plt.show()
plt.scatter(X,y,color='black')
plt.plot(X_test,predictions,color='green',markersize=3)
plt.show()