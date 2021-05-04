import numpy as np
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

rawData = open(f'all_probes/dataset-arm_raisings_forward.csv')  # тренировочные данные
dataset = np.genfromtxt(rawData, delimiter=",")

# for k in range(80,120):
#     clf = RandomForestClassifier(n_estimators=k, criterion="entropy")
#     # clf = KNeighborsClassifier(n_neighbors=k)
#     res = cross_val_score(clf, dataset[:, :-1], dataset[:, -1], cv=10) # cv - кол-во групп.

сlf = SVC()
# clf = KNeighborsClassifier(n_neighbors=k)
res = cross_val_score(clf, dataset[:, :-1], dataset[:, -1])

    print(res)
    # print(k, np.mean(res))
