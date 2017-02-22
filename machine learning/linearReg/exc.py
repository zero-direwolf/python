#review


'''from numpy import *
from sklearn import tree
import pandas as pd

data = genfromtxt('ex1data2.txt',delimiter=',')
#print(data)

feature = data[:,1:2]
#feature = feature.reshape(-1,1)
label = data[:,2]
#label = label.reshape(-1,1)

#print(feature)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(feature,label)
pred1 = [1980,4]
pred1 = pred1.reshape(1,-1)
pred = clf.predict(pred1)
print(pred)

x = data[:,0]
x = x.reshape(-1,1)
print(x)


import pandas as pd
import numpy as np
from sklearn import tree

data = pd.read_csv('ex1data1.txt',delimiter=',')
features = np.array(data)[:,0:1]
labels = np.array(data)[:,1]
#print(features)

from sklearn.cross_validation import train_test_split
features_train , features_test , labels_train , labels_test = train_test_split(features,labels,test_size=.5)


#classifier = tree.DecisionTreeClassifier()
classifier = tree.DecisionTreeRegressor()
classifier.fit(features_train,labels_train)

predictions = classifier.predict( features_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test,predictions))

#pred = classifier.predict([6.3])
#print(pred)

'''
import numpy as np
import pandas as pd
from sklearn import tree

data = pd.read_csv('ex1data2.txt')
#print(data)

features = np.array(data)[:,0:2]
labels = np.array(data)[:,2]

from sklearn.cross_validation import train_test_split
features_train , features_test , labels_train , labels_test = train_test_split(features,labels,test_size=.5)
#print(features_train,labels_train)

classifier = tree.DecisionTreeClassifier()
classifier.fit(features_train,labels_train)

predictions = classifier.predict(features_test)
print([predictions,labels_train])

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test,predictions))