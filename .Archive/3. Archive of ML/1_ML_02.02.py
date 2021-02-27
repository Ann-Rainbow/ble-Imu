from sklearn.svm import SVC
import numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression
#  Другие методы МL, еще больше - в библиотеке.
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.svm import SVC

# probe1_folder = Path(r"C:\Users\Acer A315\Desktop\EDUCATION\1. Diploma\1. Sketches\_Server_\4. ArduinoPythonSrv-master - Modified\1_probe")
vectors = []
with open("1_probe/accelx_data.txt", 'r') as f:
    # print(f.read())
    ax = [float(x) for x in f.read().split('\n')[:-1]]
# print(ax)
with open('1_probe/accely_data.txt', 'r') as f:
    ay = [float(x) for x in f.read().split('\n')[:-1]]
with open('1_probe/accelz_data.txt', 'r') as f:
    az = [float(x) for x in f.read().split('\n')[:-1]]

with open('1_probe/gyrox_data.txt', 'r') as f:
    gx = [float(x) for x in f.read().split('\n')[:-1]]
with open('1_probe/gyrox_data.txt', 'r') as f:
    gy = [float(x) for x in f.read().split('\n')[:-1]]
with open('1_probe/gyrox_data.txt', 'r') as f:
    gz = [float(x) for x in f.read().split('\n')[:-1]]

vector = []
for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
    vector.append(xa)
    vector.append(ya)
    vector.append(za)
    vector.append(xg)
    vector.append(yg)
    vector.append(zg)

vectors.append(vector)

with open('2_probe/accelx_data.txt', 'r') as f:
    ax = [float(x) for x in f.read().split('\n')[:-1]]
with open('2_probe/accely_data.txt', 'r') as f:
    ay = [float(x) for x in f.read().split('\n')[:-1]]
with open('2_probe/accelz_data.txt', 'r') as f:
    az = [float(x) for x in f.read().split('\n')[:-1]]

with open('2_probe/gyrox_data.txt', 'r') as f:
    gx = [float(x) for x in f.read().split('\n')[:-1]]
with open('2_probe/gyrox_data.txt', 'r') as f:
    gy = [float(x) for x in f.read().split('\n')[:-1]]
with open('2_probe/gyrox_data.txt', 'r') as f:
    gz = [float(x) for x in f.read().split('\n')[:-1]]

vector = []
for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
    vector.append(xa)
    vector.append(ya)
    vector.append(za)
    vector.append(xg)
    vector.append(yg)
    vector.append(zg)

vectors.append(vector)

print(vectors)
# lines = rawData.readlines()
clf = SVC()
X = np.array(vectors)
# print(X.shape)
# X = X.reshape([606, 2])
y = np.array([0, 1])
clf.fit(X, y)
print(clf.predict(X))
resultX = []
# resultY = []

