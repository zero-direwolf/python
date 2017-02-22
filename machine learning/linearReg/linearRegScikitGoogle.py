from sklearn import tree

features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
print(features)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

pred = clf.predict([180,0])
print(pred)