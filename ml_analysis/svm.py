#!/usr/bin/python

import glob
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn import metrics
from sklearn.externals import joblib
from sklearn.model_selection import KFold


def main():
    train_path = 'data/data-*.csv'
    test_path = 'test*.csv'
    flag = True
    num_files = 1
    for in_file in glob.glob(train_path):
        num_files += 1
        # train/val data
        print in_file
        data = np.genfromtxt(in_file, delimiter=',', skip_header=1)
        if flag:
            y_train = data[:, 0]
            print y_train
            x_train = data[:, 1:]
            flag = False
        else:
            y_train = np.append(y_train, data[:, 0], axis=0)
            x_train = np.vstack((x_train, data[:, 1:]))
    scaler = preprocessing.StandardScaler().fit(x_train)
    x_train_scaled = scaler.transform(x_train)
    svc = svm.SVC(C=1, kernel='linear')

    kf = KFold(n_splits=10, random_state=0, shuffle=True)
    for train_index, test_index in kf.split(x_train_scaled):
        svc.fit(x_train_scaled[train_index], y_train[train_index])
        y_pred = svc.predict(x_train_scaled[test_index])
        print metrics.classification_report(y_train[test_index], y_pred)
        print metrics.confusion_matrix(y_train[test_index], y_pred)


if __name__ == '__main__':
    main()
