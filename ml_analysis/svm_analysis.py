#!/usr/bin/python

import glob
import numpy as np
from sklearn import svm
from sklearn import preprocessing
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
        print groups

    scaler = preprocessing.StandardScaler().fit(x_train)
    x_train_scaled = scaler.transform(x_train)
    logo = LeaveOneGroupOut()
    print logo
    svc = svm.SVC(C=1, kernel='linear')
    scores = [svc.fit(x_train_scaled[train], y_train[train]).score(x_train_scaled[test], y_train[test])
              for train, test in logo.split(x_train_scaled, y_train, groups=groups)]
    print scores
    print("CV Accuracy: %0.2f (+/- %0.2f)" % (np.mean(scores), np.std(scores) * 2))

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
