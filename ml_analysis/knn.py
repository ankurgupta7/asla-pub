#!/usr/bin/python

import glob
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
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
            x_train = data[:, 1:]
            flag = False
        else:
            y_train = np.append(y_train, data[:, 0], axis=0)
            x_train = np.vstack((x_train, data[:, 1:]))
    scaler = preprocessing.StandardScaler().fit(x_train)
    x_train_scaled = scaler.transform(x_train)


    neighbors = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for param in neighbors:
        kneighboursClassifier = KNeighborsClassifier(n_neighbors=param, algorithm='ball_tree')
        scores = []
        kf = KFold(n_splits=20, random_state=0, shuffle=True)
        for train_index, test_index in kf.split(x_train_scaled):
            kneighboursClassifier = kneighboursClassifier.fit(x_train_scaled[train_index], y_train[train_index])
            #y_pred = kneighboursClassifier.predict(x_train_scaled[test_index])
            scores.append(kneighboursClassifier.fit(x_train_scaled[train_index], y_train[train_index]).score(x_train_scaled[test_index], y_train[test_index]))
            #print metrics.classification_report(y_train[test_index], y_pred)
            #print metrics.confusion_matrix(y_train[test_index], y_pred)
        print ("CV accuracy: %0.7f (+/- %0.7f)" % (np.mean(scores), np.std(scores) ** 2)), param
    #fin_model = svc.fit(x_train_scaled, y_train)
    # joblib.dump(fin_model, '6am_model.pkl')
    # joblib.dump(scaler, '6am_scaler.pkl')

if __name__ == '__main__':
    main()