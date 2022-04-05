import numpy as np
# import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

# diabetes = datasets.load_diabetes()

# diabetes_X = diabetes.data
# diabetes_X = np.array([[1],[2],[3]])  
# array => [70-50, 75-55, 80-58, 85-60, 90-65, 95-70, 100-80, 105-90, 110-105 ]

diabetes_X_train = np.array(
  [
    # [area, hall, bedroom, kitchen, bathroom]
    [70, 4],
    [70, 5],
    [70, 6],
    [75, 4],
    [75, 5],
    [75,6]
  ])
diabetes_X_test = diabetes_X_train

diabetes_Y_train = np.array([[45],[50],[60],[55],[60],[70]])
diabetes_Y_test = diabetes_Y_train

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_Y_train)

diabetes_Y_predict = model.predict(diabetes_X_test)

print("Mean squared error is: ", mean_squared_error(diabetes_Y_predict, diabetes_Y_test))

print("Weights: ", model.coef_) #weight is just slope of line
print("Intercept: ", model.intercept_)

# plt.scatter(diabetes_X_train, diabetes_Y_train)
# plt.plot(diabetes_X_test, diabetes_Y_predict)
# print(model.predict(np.array([[205]])))
# plt.show()

while 1:
  num = input("Enter Area in sq meter:-\t")
  winn = input("Enter Number of Rooms:-\t")
  nnum = float(num)
  win = float(winn)
  if(nnum == 1):
    break
  print("Your Price of house with " + num + "sq meters and " + winn + "rooms will be: ", end="\t")
  print(model.predict(np.array([[nnum, win]]))[0][0], end="\n")
