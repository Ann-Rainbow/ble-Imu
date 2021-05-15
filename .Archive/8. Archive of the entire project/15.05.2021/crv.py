import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


from sklearn.model_selection import cross_val_score


rawData = open(f'all_probes/artts-different_speed.csv')  # тренировочные данные
dataset = np.genfromtxt(rawData, delimiter=",")

for k in range(1,101):
#
#
    #clf = RandomForestClassifier(n_estimators=k, criterion="gini", max_depth=100 ) #
    clf = DecisionTreeClassifier(max_depth=103, criterion="gini", min_samples_leaf = k) # random_state=k, max_features = 6
#       #clf = KNeighborsClassifier(n_neighbors=k)
#       n_classes = k
#       clf = GaussianNB(priors=n_classes)
#
    res = cross_val_score(clf, dataset[:, :-1], dataset[:, -1], cv=10) # cv - кол-во групп.
#     print(res)
    print(k, np.mean(res))
# clf = SVC()
#clf = LogisticRegression()
#clf = LinearRegression()

#for n_classes in range(0, 5):

#n_classes = [1]
#clf = GaussianNB(priors=None, var_smoothing=1e-09) #priors = n_classes
#clf = DecisionTreeClassifier(criterion="entropy")
#clf = LinearDiscriminantAnalysis()
#clf = KMeans()
#clf = KNeighborsClassifier()
#clf = RandomForestClassifier()

# clf = SVC(kernel='rbf', C=10) # оптимальный параметр для метода SVM
# clf = LogisticRegression(C=1.0, intercept_scaling=1, dual=False, fit_intercept=True, penalty='l2', tol=0.1)

# res = cross_val_score(clf, dataset[:, :-1], dataset[:, -1], cv=10) # cv - кол-во групп.
# print(res)
# print("Среднее значение правильных предсказаний:", np.mean(res))
    # print(res)
    #print(k, np.mean(res))
