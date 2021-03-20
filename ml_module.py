from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression
#  Другие методы МL, еще больше - в библиотеке.
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.svm import SVC

def getPrediction(testFileName):
    rawData = open(f'all_probes/dataset.csv')  # тренировочные данные
    svmClass = SVC()
    dataset = np.genfromtxt(rawData, delimiter=",")
    # print(dataset)
    # dataset = np.loadcsv(rawData, delimiter=",")
    svmClass.fit(dataset[:, :-1], dataset[:, -1])  # обучение классификатора
    testData = open(f'all_probes/{testFileName}')  # тестовые данные
    testSet = np.genfromtxt(testData, delimiter=",")
    testSet = np.reshape(testSet, (1, -1))
    # print(testSet)
    svmPredict = svmClass.predict(testSet)  # вызов метода predict
    #print(svmPredict)
    return bool(svmPredict)


testFileName = "test_false2.csv"
print(getPrediction(testFileName))
