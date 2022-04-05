from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

iris = datasets.load_iris()
features = iris.data
labels = iris.target

# print(iris.DESCR)
# print(features[0], labels[0])

clf = KNeighborsClassifier()
clf.fit(features, labels)

pred = clf.predict([[15, 1, 1, 1]])
# print(pred)

plt.plot(features, labels)
plt.show()