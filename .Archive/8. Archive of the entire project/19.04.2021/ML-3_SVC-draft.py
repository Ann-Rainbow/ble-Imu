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

# Черновик попыток разных / Draft of various attempts

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


# probe1_folder = Path(r"C:\Users\Acer A315\Desktop\EDUCATION\1. Diploma\1. Sketches\_Server_\4. ArduinoPythonSrv-master - Modified\1_probe")
vectors = []

for i in range(0, 10):
    with open(f'all_probes/{i}_probe/accelx_data.txt', 'r') as f:
        ax = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'all_probes/{i}_probe/accely_data.txt', 'r') as f:
        ay = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'all_probes/{i}_probe/accelz_data.txt', 'r') as f:
        az = np.array([float(x) for x in f.read().split('\n')[:-1]])

    with open(f'all_probes/{i}_probe/gyrox_data.txt', 'r') as f:
        gx = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'all_probes/{i}_probe/gyrox_data.txt', 'r') as f:
        gy = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'all_probes/{i}_probe/gyrox_data.txt', 'r') as f:
        gz = np.array([float(x) for x in f.read().split('\n')[:-1]])

    # print("Usual ax", ax)

# for i in range(10, 15):
#     with open(f'all_probes/{i}_probe/{i}_probe.csv', 'r') as f:
#         csvreader = csv.reader(f, delimiter=',', quotechar='|')
#         j = 0
#         vector = []
#         for row in csvreader:
#             if j > 0:
#                 # print(row)
#                 vector += [float(x) for x in row]
#             j += 1
#         # print(vector)
#         vectors.append(vector)



    ax = median_filter(ax, 5)
    ay = median_filter(ay, 5)
    az = median_filter(az, 5)

    gx = median_filter(gx, 5)
    gy = median_filter(gy, 5)
    gz = median_filter(gz, 5)

    # print("Filtered ax", ax)


    with open(f'all_probes/all_data7.txt', "w") as f:
        for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
            # print("xa = ", xa) # нормально
            f.write(str (xa))
            f.write(", ")
            f.write(str (ya))
            f.write(", ")
            f.write(str (za))
            f.write(", ")
            f.write(str (xg))
            f.write(", ")
            f.write(str (yg))
            f.write(", ")
            f.write(str (zg))
            f.write(", ")
            # f.write("\n")


    # print(ax)

    # with open(f'all_probes/all_data.txt', "w") as f:
    #     f.write(ax)
    #     f.write(ay)
    #     f.write(az)
    #     f.write(gx)
    #     f.write(gy)
    #     f.write(gz)
    #     f.write(data.decode("utf-8")+ "\n")




    # with open(f'all_probes/all_data2.txt', "w") as f:
    #     for element in zip(ax, ay, az, gx, gy, gz):
    #         f.write(str(element))
    #         print(element)
    #         print("ax=", ax)
    #         print("ay=", ay)
    #         f.write("\n")


    # vector = []
    # for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
    #     vector.append(xa)
    #     vector.append(ya)
    #     vector.append(za)
    #     vector.append(xg)
    #     vector.append(yg)
    #     vector.append(zg)
    #
    # print(vector)

    # print(len(vector))
    # vectors.append(vector)

rawData = open("all_data8.txt'") # тренировочные данные
svmClass = SVC()
dataset = np.loadtxt(rawData, delimiter=",")

svmClass.fit(dataset[:, :-1], dataset[:, -1])  # обучение классификатора



testData = open("testData.txt") # тестовые данные

testSet = np.loadtxt(testData, delimiter=",")
testSet = np.reshape(testSet, (1, -1))

svmPredict = svmClass.predict(testSet)  # вызов метода predict
print(svmPredict)

# # print(vectors[0])
# # print(vectors)
# # lines = rawData.readlines()
# clf = SVC()
# X = np.array(vectors)
# # print(X.shape)
# # X = X.transpose()
# print(X.shape)
#
# # X = X.reshape([606, 2])
# y = np.array([1, 1, 1, 1, 0, 0, 0, 0])
# print(y.shape)
# X_train = np.array([X[0], X[1], X[2], X[3], X[5], X[6], X[7], X[8]])
# X_test = np.array([X[4], X[9]])
#
# # X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=2020)
# # print(X_test, Y_test)
# clf.fit(X_train, y)
# print(clf.predict(X_test))
# # resultX = []
# # # resultY = []
# # iris = load_iris()
# # X = iris.data
# # print(X[0])