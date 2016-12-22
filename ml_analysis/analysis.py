import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneGroupOut
from sklearn import preprocessing, metrics
import matplotlib.pyplot as plt
import string

import glob
# This script is used for comparing the performance of various classifiers.
# Currently, SVM and RandomForest perform the best

names = ["Nearest Neighbors", "Linear SVM",
         "Decision Tree", "Random Forest"]

classifiers = [
    KNeighborsClassifier(10),
    SVC(kernel="linear", C=0.04),
    DecisionTreeClassifier(max_depth=3000),
    RandomForestClassifier(max_depth=800, n_estimators=800, max_features='auto', n_jobs=8)]

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
accuracy = {}

for name, clf in zip(names, classifiers):
    scores = []
    score_per_label = []
    print '###########################################################################'
    print 'Classifier: ', name
    confusion_mat = np.zeros(shape=(26, 26))
    for train, test in logo.split(x_train_scaled, y_train, groups=groups):
        clf.fit(x_train_scaled[train], y_train[train])
        scores.append(clf.score(x_train_scaled[test], y_train[test]))
        y_predicted = clf.predict(x_train_scaled[test])
        score_per_label.append(metrics.f1_score(y_train[test], y_predicted, average=None))
        confusion_mat = confusion_mat + metrics.confusion_matrix(y_train[test], y_predicted)
    print scores
    print("CV Accuracy: %0.2f (+/- %0.2f)" % (np.mean(scores), np.std(scores) * 2))
    accuracy[name] = [np.mean(scores), np.std(scores) * 2]
    print np.shape(np.mean(np.array(score_per_label), axis=0))
    print
    print 'SCORES PER LABEL \n'
    print '| Label         | Accuracy      |'
    print '|:-------------:|:-------------:|'
    for label, acc in zip(list(string.ascii_uppercase), np.mean(np.array(score_per_label), axis=0)):
        print '|', label, '|', '%0.2f ' % acc, '|'
    print '\n'
    print 'CONFUSION MATRIX\n'
    for i, acc in enumerate(np.mean(np.array(score_per_label), axis=0)):
        if acc < 0.61:
            raw = confusion_mat[i]
            norm = [float(j) / sum(raw) for j in raw]
            c = []
            for alpha, conf in zip(list(string.ascii_uppercase), norm):
                if conf > 0.05:
                    c.append((alpha, conf))
            print '|', list(string.ascii_uppercase)[i], '|', c, '|'

bar_width = 0.2
opacity = 0.6
error_config = {'ecolor': '0.3'}
fig, ax = plt.subplots()
index = 0
colors = ['g', 'b', 'y', 'r']
for key, value in accuracy.items():
    rects1 = plt.bar(index + bar_width, value[0], bar_width,
                     alpha=opacity,
                     color=colors[index],
                     yerr=value[1],
                     error_kw=error_config,
                     label=key)
    ax.text(index + bar_width, value[0]+value[1] + 0.02, "%0.2f" % (value[0]), color='black', fontweight='bold')
    index += 1
    # print key, value

ax.set_aspect('auto')
index = np.arange(4)
plt.ylabel('Accuracy')
plt.title('Accuracy by Classifiers')
plt.xticks(index + bar_width + 0.1, ('RF', 'SVM', 'kNN', 'DT'), rotation=70)
# plt.tight_layout()
plt.show()
