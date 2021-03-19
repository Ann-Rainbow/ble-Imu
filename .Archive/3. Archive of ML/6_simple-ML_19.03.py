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


def median_filter (x, k):
    """Apply a length-k median filter to a 1D array x.
    Boundaries are extended by repeating endpoints.
    """
    assert k % 2 == 1, "Median filter length must be odd."
    assert x.ndim == 1, "Input must be one-dimensional."
    k2 = (k - 1) // 2
    y = np.zeros ((len (x), k), dtype=x.dtype)
    y[:,k2] = x
    for i in range (k2):
        j = k2 - i
        y[j:,i] = x[:-j]
        y[:j,i] = x[0]
        y[:-j,-(i+1)] = x[j:]
        y[-j:,-(i+1)] = x[-1]
    return np.median (y, axis=1)

    ax = median_filter(ax, 5)
    ay = median_filter(ay, 5)
    az = median_filter(az, 5)

    gx = median_filter(gx, 5)
    gy = median_filter(gy, 5)
    gz = median_filter(gz, 5)

rawData = open(f'all_probes/dataset.csv') # тренировочные данные
svmClass = SVC()
dataset = np.genfromtxt(rawData, delimiter=",")
#print(dataset)
#dataset = np.loadcsv(rawData, delimiter=",")

svmClass.fit(dataset[:, :-1], dataset[:, -1])  # обучение классификатора

testData = open(f'all_probes/test-data.csv') # тестовые данные
testSet = np.genfromtxt(testData, delimiter=",")
testSet = np.reshape(testSet, (1, -1))
#print(testSet)


svmPredict = svmClass.predict(testSet)  # вызов метода predict
print(svmPredict)