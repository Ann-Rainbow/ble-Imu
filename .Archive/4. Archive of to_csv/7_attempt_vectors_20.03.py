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
import csv
import os.path

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

for i in range(0, 121):
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
    vector = []
    for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
        vector.append(xa)
        vector.append(ya)
        vector.append(za)
        vector.append(xg)
        vector.append(yg)
        vector.append(zg)

    #print(vector)


    #print(len(vector))
    vectors.append(vector)

#print(vectors)

csvfile = open(f'all_probes/dataset.csv', 'w', newline='\n')
spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
for i in range(len(vectors)):
    with open(f'all_probes/{i+1}_probe/Result', 'r') as f:
        success = int(f.read())
    spamwriter.writerow(vectors[i] + [success])

# for i in range(1, 4):
#     csvfile = open(f'all_probes/{i}_probe/{i}_000probe.csv', 'w', newline='')
#     spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['vector', 'true or false'])
#     # for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
#     for vector in vectors:
#         spamwriter.writerow(vector + [])
#     csvfile.close()