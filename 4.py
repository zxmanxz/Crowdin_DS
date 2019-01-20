from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.3)

knn = KNeighborsClassifier(n_neighbors=9)

knn.fit(X_train, y_train)
from sklearn import metrics
y_pred = knn.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))