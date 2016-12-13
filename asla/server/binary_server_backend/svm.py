#!/usr/bin/python

from sklearn import svm
from sklearn import preprocessing


def create_model(x_train, y_train):
    scaler = preprocessing.StandardScaler().fit(x_train)
    x_train_scaled = scaler.transform(x_train)
    svc = svm.SVC(C=1, kernel='linear', probability=True)
    fin_model = svc.fit(x_train_scaled, y_train)
    return fin_model, scaler
