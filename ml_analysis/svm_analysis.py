#!/usr/bin/python

import glob
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.externals import joblib
from sklearn.model_selection import KFold
import jsonpickle
import pickle
import pymongo
from pymongo import MongoClient
import gridfs
from bson.binary import Binary
from sklearn.model_selection import LeaveOneGroupOut
import matplotlib.pyplot as plt


def main():
    user_data = {}
    users = []
    groups = []
    train_path = 'data/*'
    flag = True

    for in_folder in glob.glob(train_path):
        current_user = in_folder.split('/')[1]
        users.append(current_user)
        print users
        # print 'folder', in_file
        count = 0
        for in_file in glob.glob(in_folder+'/*'):
            print in_file
            data = np.genfromtxt(in_file, delimiter=',', skip_header=1)
            if flag:
                count += 1
                y_train = data[:, 0]
                x_train = data[:, 1:]
                flag = False
            elif count < 10:
                y_train = np.append(y_train, data[:, 0], axis=0)
                x_train = np.vstack((x_train, data[:, 1:]))
            if current_user not in user_data:
                user_data[current_user] = data
            else:
                user_data[current_user] = np.vstack((user_data[current_user], data))
        print len(user_data[current_user])
        groups.extend(np.repeat(len(users), len(user_data[current_user])))
        #print groups

    scaler = preprocessing.StandardScaler().fit(x_train)
    x_train_scaled = scaler.transform(x_train)
    logo = LeaveOneGroupOut()
    #print logo\
    #param = np.linspace(50,5000,200)
    #avg = []
    #for p in param:
        #if p == 50:
            #rfc = RandomForestClassifier(max_depth = int(p), max_features = 'sqrt', n_estimators = 60, n_jobs=4)
            #res = [1 - rfc.fit(x_train_scaled[train], y_train[train]).score(x_train_scaled[test], y_train[test])
                      #for train, test in logo.split(x_train_scaled, y_train, groups=groups)]
            #avg.append(np.mean(res))
        #else:
        #rfc = RandomForestClassifier(max_depth = 50, max_features = 'sqrt', n_estimators = 60, n_jobs=4)
        #scores = [1 - rfc.fit(x_train_scaled[train], y_train[train]).score(x_train_scaled[test], y_train[test])
                  #for train, test in logo.split(x_train_scaled, y_train, groups=groups)]
        #res = np.vstack((res,scores))
            #print avg, p


    svc = svm.SVC(C = 1, kernel = 'linear')
    #scores = [rfc.fit(x_train[train], y_train[train]).score(x_train[test], y_train[test])
              #for train, test in logo.split(x_train, y_train, groups=groups)]
    #print np.mean(scores)
    tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                         'C': [0.0001, 0.001, 0.01, 0.1, 1]},
                        {'kernel': ['linear'], 'C': [0.0001, 0.001, 0.01, 1]}]
    CV_svm = GridSearchCV(estimator=svc, param_grid=tuned_parameters, cv= logo, n_jobs= 4)
    CV_svm.fit(x_train_scaled, y_train, groups = groups)
    print "Best params", CV_svm.best_params_
    print "Best score", CV_svm.best_score_
    print "Scorer function", CV_svm.scorer_


    #np.savetxt('knn_res',res)

    # plt.plot(param, res[:,0], c = 'g', label = 'group1')
    # plt.plot(param, res[:,1],c= 'y', label = 'group2')
    # plt.plot(param, res[:,2],c='b', label = 'group3')
    # plt.plot(param, res[:,3],c='m', label = 'group4')
    # plt.plot(param, np.mean(res,axis = 1), c='r', label='average', linewidth = 4)
    # plt.legend(loc = 'upper right')
    # plt.xlabel('Maximum depth', size = 15)
    # plt.ylabel('CV error', size = 15)
    # plt.title('Decision Tree Leave Group Out cross validation curve', size = 15)
    # plt.plot(param, avg,color = 'red')
    # plt.show()

    #print("CV Accuracy: %0.2f (+/- %0.2f)" % (np.mean(scores), np.std(scores) * 2))

        # print 'user_name', in_file.split('/')[1]
    # scaler = preprocessing.StandardScaler().fit(x_train)
    # x_train_scaled = scaler.transform(x_train)
    #
    # C = [1]
    # for param in C:
    #     svc = svm.SVC(C=param, kernel='linear', probability=True)
    #     scores = []
    #     kf = KFold(n_splits=10, random_state=0, shuffle=True)
    #     for train_index, test_index in kf.split(x_train_scaled):
    #         svc.fit(x_train_scaled[train_index], y_train[train_index])
    #         y_pred = svc.predict(x_train_scaled[test_index])
    #         scores.append(svc.fit(x_train_scaled[train_index], y_train[train_index]).score(x_train_scaled[test_index], y_train[test_index]))
    #         # print metrics.classification_report(y_train[test_index], y_pred)
    #         # print metrics.confusion_matrix(y_train[test_index], y_pred)
    #     print ("CV accuracy: %0.7f (+/- %0.7f)" % (np.mean(scores), np.std(scores) ** 2)), param
    # train_path = 'data/data-*.csv'
    # flag = True
    # num_files = 1
    # for in_file in glob.glob(train_path):
    #     num_files += 1
    #     # train/val data
    #     print in_file
    #     data = np.genfromtxt(in_file, delimiter=',', skip_header=1)
    #     if flag:
    #         y_train = data[:, 0]
    #         x_train = data[:, 1:]
    #         flag = False
    #     else:
    #         y_train = np.append(y_train, data[:, 0], axis=0)
    #         x_train = np.vstack((x_train, data[:, 1:]))
    # scaler = preprocessing.StandardScaler().fit(x_train)
    # x_train_scaled = scaler.transform(x_train)
    #
    # C = [1]
    # for param in C:
    #     svc = svm.SVC(C=param, kernel='linear', probability=True)
    #     scores = []
    #     kf = KFold(n_splits=10, random_state=0, shuffle=True)
    #     for train_index, test_index in kf.split(x_train_scaled):
    #         svc.fit(x_train_scaled[train_index], y_train[train_index])
    #         y_pred = svc.predict(x_train_scaled[test_index])
    #         scores.append(svc.fit(x_train_scaled[train_index], y_train[train_index]).score(x_train_scaled[test_index], y_train[test_index]))
    #         # print metrics.classification_report(y_train[test_index], y_pred)
    #         # print metrics.confusion_matrix(y_train[test_index], y_pred)
    #     print ("CV accuracy: %0.7f (+/- %0.7f)" % (np.mean(scores), np.std(scores) ** 2)), param
    # fin_model = svc.fit(x_train_scaled, y_train)
    # print type(fin_model)
    # test_obj = pickle.dumps(fin_model)
    # users.insert({"try": test_obj, "name": "2"})
    #
    #
    #
    # # with open("myfile.json", 'w') as myfile:
    # #     myfile.write(encoded)
    #
    # # actual_obj = pickle.loads(test_obj)
    #
    # joblib.dump(fin_model, '7pm_model.pkl')
    # joblib.dump(scaler, '7pm_scaler.pkl')

if __name__ == '__main__':
    main()

# SVM C= 0.04 81%
# RF Number of trees = 60 83%
# Knn #Neighbors = 10 72%
# Decision 3000 69%
