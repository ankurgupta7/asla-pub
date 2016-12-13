#!/usr/bin/python
from abc import abstractmethod

from sklearn import svm
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


class Classifier:
    """Parent class for a classifier object"""

    def __init__(self):
        self.x_train_scaled = None
        self.scaler = None
        self.fin_model = None
        pass

    @abstractmethod
    def create_model(self, x, y):
        self.scaler = preprocessing.StandardScaler().fit(x)
        self.x_train_scaled = self.scaler.transform(x)


class SVM(Classifier):
    """Linear SVM Classifier"""
    def __init__(self):
        Classifier.__init__(self)

    def create_model(self, x, y):
        Classifier.create_model(self, x, y)
        svc = svm.SVC(C=1, kernel='linear', probability=True)
        self.fin_model = svc.fit(self.x_train_scaled, y)
        return self.fin_model, self.scaler


class KNN(Classifier):
    """Ball Tree K-Nearest Neighbour Classifier"""
    def __init__(self):
        Classifier.__init__(self)

    def create_model(self, x, y):
        Classifier.create_model(x, y)
        knc = KNeighborsClassifier(n_neighbors=5, algorithm='ball_tree')
        self.fin_model = knc.fit(self.x_train_scaled, y)
        return self.fin_model, self.scaler
