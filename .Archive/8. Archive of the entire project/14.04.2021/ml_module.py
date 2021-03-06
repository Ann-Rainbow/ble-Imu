from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np
import pickle
from pathlib import Path
from sklearn.linear_model import LogisticRegression
#  Другие методы МL, еще больше - в библиотеке.
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.svm import SVC
def modelTraining():
    rawData = open(f'all_probes/dataset.csv')  # тренировочные данные
    svmClass = SVC()
    dataset = np.genfromtxt(rawData, delimiter=",")
    svmClass.fit(dataset[:, :-1], dataset[:, -1])  # обучение классификатора
    clsfile = open("all_probes/classifier_SVC", "wb")
    pickle.dump(svmClass, clsfile)
    clsfile.close()

# modelTraining()

def getPrediction(testData):
    # print(dataset)
    # dataset = np.loadcsv(rawData, delimiter=",")
    clsfile = open("all_probes/classifier", "rb")
    svmClass = pickle.load(clsfile)
    clsfile.close()
    # testData = open(f'all_probes/{testFileName}')  # тестовые данные
    # testSet = np.genfromtxt(testData, delimiter=",")
    testSet = np.array(testData)
    print(testSet.shape)
    testSet = np.reshape(testSet, (1, -1))
    # print(testSet)
    svmPredict = svmClass.predict(testSet)  # вызов метода predict
    #print(svmPredict)
    return bool(svmPredict)


# testFileName = "test-data.csv"
# print(getPrediction(testFileName))
if __name__ == '__main__':
    modelTraining()