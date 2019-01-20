from reportlab import xrange
from sklearn import datasets

iris=datasets.load_iris()

print(iris.data)
print(iris.target)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(iris.data,iris.target,test_size=0.33)

from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier(n_neighbors=3).fit(x_train,y_train)

#import accuracy metric

from sklearn.metrics import accuracy_score
print("accuracy is ")
print(accuracy_score(y_test,clf.predict(x_test)))

#we got accuracy of 96 when we use k=3, now lets try to plot graph with k and accuracy

import matplotlib.pyplot as plt

#we now iterate our classifier and init it different k values and find accuracy

accuracy_values=[]

for x in xrange(1,x_train.shape[0]):
	clf=KNeighborsClassifier(n_neighbors=x).fit(x_train,y_train)
	accuracy=accuracy_score(y_test,clf.predict(x_test))
	accuracy_values.append([x,accuracy])
	pass

import numpy as np
accuracy_values=np.array(accuracy_values)

plt.plot(accuracy_values[:,0],accuracy_values[:,1])
plt.xlabel("K")
plt.ylabel("accuracy")
plt.show()



