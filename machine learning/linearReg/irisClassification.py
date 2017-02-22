from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
import pydotplus

iris = load_iris()
test_idx = [0,50,100]
'''print(iris.feature_names)
print(iris.target_names)
#print(iris)
print(iris.data[0])
print(iris.target[0])
for i in range(len(iris.target)):
	print('example %d: label %s: feature %d',i,iris.data[i],iris.target[i])
	pass
'''
#training data 
train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data,test_idx,axis=0)

#test data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data,train_target)

print(test_target)
print(clf.predict(test_data))
 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_pdf("iris.pdf") 

print(test_data[0],test_target[0])
print(iris.feature_names,iris.target_names)
'''from IPython.display import Image  
dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydotplus.graph_from_dot_data(dot_data)  
Image(graph.create_png()) '''