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


# probe1_folder = Path(r"C:\Users\Acer A315\Desktop\EDUCATION\1. Diploma\1. Sketches\_Server_\4. ArduinoPythonSrv-master - Modified\1_probe")
vectors = []

for i in range(1, 11):
    with open(f'{i}_probe/accelx_data.txt', 'r') as f:
        ax = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'{i}_probe/accely_data.txt', 'r') as f:
        ay = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'{i}_probe/accelz_data.txt', 'r') as f:
        az = np.array([float(x) for x in f.read().split('\n')[:-1]])

    with open(f'{i}_probe/gyrox_data.txt', 'r') as f:
        gx = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'{i}_probe/gyrox_data.txt', 'r') as f:
        gy = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'{i}_probe/gyrox_data.txt', 'r') as f:
        gz = np.array([float(x) for x in f.read().split('\n')[:-1]])

    ax = median_filter(ax, 5)
    ay = median_filter(ay, 5)
    az = median_filter(az, 5)

    gx = median_filter(gx, 5)
    gy = median_filter(gy, 5)
    gz = median_filter(gz, 5)
    vector = []
    for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
        vector.append(xa)
        vector.append(ya)
        vector.append(za)
        vector.append(xg)
        vector.append(yg)
        vector.append(zg)

    # print(len(vector))
    vectors.append(vector)

# print(vectors[0])
# lines = rawData.readlines()
clf = SVC()
X = np.array(vectors)
# print(X.shape)
# X = X.transpose()
print(X.shape)
# X = X.reshape([606, 2])
y = np.array([1, 1, 1, 1, 0, 0, 0, 0])
print(y.shape)
X_train = np.array([X[0], X[1], X[2], X[3], X[5], X[6], X[7], X[8]])
X_test = np.array([X[4], X[9]])

# X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=2020)
# print(X_test, Y_test)
clf.fit(X_train, y)
print(clf.predict(X_test))
# resultX = []
# # resultY = []
# iris = load_iris()
# X = iris.data
# print(X[0])