from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
# rawData = open("learnCoords.txt")
svmClass = SVC()
dataset = np.genfromtxt('all_probes/dataset.csv',delimiter=',')
# dataset = np.loadtxt(rawData, delimiter=",")
print(dataset)
X = dataset[:, :-1]
Y = np.array(list(map(int, dataset[:, -1])))
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.08, random_state=5)
# X_train = X[:-1]
# Y_train = Y[:-1]
# X_test = [X[-1]]
svmClass.fit(X_train, Y_train) # обучение классификатора
# testData = open("testData.txt")
# testSet = np.loadtxt(testData, delimiter=",")
# testSet = np.reshape(testSet, (1, -1))
svmPredict = svmClass.predict(X_test) # вызов метода predict
print(svmPredict == Y_test)


# from sklearn.svm import SVC
# from sklearn.model_selection import train_test_split
# import numpy as np
#
# svmClass = SVC()
# dataset = np.genfromtxt('all_probes/dataset.csv',delimiter=',')
# X = dataset[:, :-1]
# Y = np.array(list(map(int, dataset[:, -1])))
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.08, random_state=5)
# svmClass.fit(X_train, Y_train)
# svmPredict = svmClass.predict(X_test)
# print(svmPredict == Y_test)

