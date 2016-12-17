#!/usr/bin/python

import glob
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import LeaveOneGroupOut
from sklearn import metrics
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectPercentile, f_classif


def main():
    train_path = 'data-*.csv'
    test_path = 'test*.csv'
    flag = True
    num_files = 1
    for in_file in glob.glob(train_path):
        num_files += 1
        # train/val data
        print in_file
        data = np.genfromtxt(in_file, delimiter=',')
        if flag:
            y_train = data[:, 0]
            x_train = data[:, 1:]
            flag = False
        else:
            y_train = np.append(y_train, data[:, 0], axis=0)
            x_train = np.vstack((x_train, data[:, 1:]))
    # groups = np.arange(1, num_files)
    # groups = np.repeat(groups, 25)
    # x_train = np.delete(x_train, [1, 2, 24], axis=1)

    scaler = preprocessing.StandardScaler().fit(x_train)
    x_train_scaled = scaler.transform(x_train)
    x_train_scaled = np.delete(x_train_scaled, [1, 2, 24], axis=1)
    plt.figure(1)
    plt.clf()
    X_indices = np.arange(x_train_scaled.shape[-1])
    selector = SelectPercentile(f_classif, percentile=10)
    selector.fit(x_train_scaled, y_train)
    scores = -np.log10(selector.pvalues_)
    scores /= scores.max()
    plt.bar(X_indices - .45, scores, width=.2,
            label=r'Univariate score ($-Log(p_{value})$)', color='darkorange')
    plt.show()
    # logo = LeaveOneGroupOut()
    # print logo
    # svc = svm.SVC(C=1, kernel='linear')
    # scores = [svc.fit(x_train_scaled[train], y_train[train]).score(x_train_scaled[test], y_train[test])
    #           for train, test in logo.split(x_train_scaled, y_train, groups=groups)]
    # print scores
    # print("CV Accuracy: %0.2f (+/- %0.2f)" % (np.mean(scores), np.std(scores) * 2))
    #
    # # Analysis
    # total = np.zeros(5, )
    # for train, test in logo.split(x_train_scaled, y_train, groups=groups):
    #     svc.fit(x_train_scaled[train], y_train[train])
    #     y_pred = svc.predict(x_train_scaled[test])
    #     print metrics.classification_report(y_train[test], y_pred)
    #     total = np.add(metrics.f1_score(y_train[test], y_pred, average=None), total)
    # print len(groups)
    # print np.divide(total, 4)
    # fin_model = svc.fit(x_train_scaled, y_train)
    # joblib.dump(fin_model, 'model.pkl')
    # joblib.dump(scaler, 'scaler.pkl')
    #
    # for test_file in glob.glob(test_path):
    #     num_files += 1
    #     # train/val data
    #     print test_file
    #     data = np.genfromtxt(test_file, delimiter=',')
    #     if flag:
    #         y_test = data[:, 0]
    #         x_test = data[:, 1:]
    #         flag = False
    #     else:
    #         y_test = np.append(y_train, data[:, 0], axis=0)
    #         x_test = np.vstack((x_train, data[:, 1:]))
    #     x_test_scaled = scaler.transform(x_test)
    #     y_test_pred = svc.predict(x_test_scaled)
    #     print metrics.classification_report(y_test, y_test_pred)


if __name__ == '__main__':
    one = ord(raw_input().upper()) - 64
    print one
    print chr(one + 64)
    le = preprocessing.LabelEncoder()
    le.fit(["a", "b", "c", "d", "e"])
    print le.classes_
    print le.transform(["a"])
    # main()
