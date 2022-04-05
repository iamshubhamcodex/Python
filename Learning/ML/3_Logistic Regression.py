from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

iris = datasets.load_iris()
# print(list(iris.keys()))
x = iris["data"][:, 3:]
y = ( iris["target"] == 2 ).astype(np.int64)

clf = LogisticRegression()
clf.fit(x, y)
print((clf.predict([[1.6]])))
# print(y)

x_new = np.linspace(0, 3, 1000).reshape(-1,1)
# print(x_new)
y_prob = clf.predict_proba(x_new)
plt.plot(x_new, y_prob[:, 1], "g-",label="virginica")
plt.show()