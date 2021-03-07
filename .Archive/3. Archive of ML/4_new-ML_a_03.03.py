from sklearn.svm import SVC
import numpy as np

rawData = open("learnCoords.txt")
svmClass = SVC()
dataset = np.loadtxt(rawData, delimiter=",")

svmClass.fit(dataset[:, :-1], dataset[:, -1]) # обучение классификатора

testData = open("testData.txt")

testSet = np.loadtxt(testData, delimiter=",")
testSet = np.reshape(testSet, (1, -1))

svmPredict = svmClass.predict(testSet) # вызов метода predict
print(svmPredict)
