import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneGroupOut
from sklearn import preprocessing, metrics


import glob
# This script is used for comparing the performance of various classifiers.
# Currently, SVM and RandomForest perform the best

names = ["Nearest Neighbors", "Linear SVM",
         "Decision Tree", "Random Forest"]

classifiers = [
    KNeighborsClassifier(10),
    SVC(kernel="linear", C=0.04),
    DecisionTreeClassifier(max_depth=3000),
    RandomForestClassifier(max_depth=50, n_estimators=60, max_features=15)]


user_data = {}
users = []
groups = []
train_path = 'data/*'
flag = True

for in_folder in glob.glob(train_path):
    current_user = in_folder.split('/')[1]
    users.append(current_user)
    # print 'folder', in_file
    for in_file in glob.glob(in_folder+'/*'):
        data = np.genfromtxt(in_file, delimiter=',', skip_header=1)
        if flag:
            y_train = data[:, 0]
            x_train = data[:, 1:]
            flag = False
        else:
            y_train = np.append(y_train, data[:, 0], axis=0)
            x_train = np.vstack((x_train, data[:, 1:]))
        if current_user not in user_data:
            user_data[current_user] = data
        else:
            user_data[current_user] = np.vstack((user_data[current_user], data))
    groups.extend(np.repeat(len(users), len(user_data[current_user])))

scaler = preprocessing.StandardScaler().fit(x_train)
x_train_scaled = scaler.transform(x_train)
logo = LeaveOneGroupOut()

for name, clf in zip(names, classifiers):
    scores = []
    print '###########################################################################'
    print 'Classifier: ', name

    for train, test in logo.split(x_train_scaled, y_train, groups=groups):
        clf.fit(x_train_scaled[train], y_train[train])
        scores.append(clf.score(x_train_scaled[test], y_train[test]))
        y_predicted = clf.predict(x_train_scaled[test])
        # print metrics.classification_report(y_train[test], y_predicted)
    print scores
    print("CV Accuracy: %0.2f (+/- %0.2f)" % (np.mean(scores), np.std(scores) * 2))
