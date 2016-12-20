#!/usr/bin/python
from abc import abstractmethod

from sklearn import svm
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


class Classifier:
    """Parent class for the classifier.
    A classifier object is used to train and generate a new model for prediction.
    Allows for more classifiers to be added at a later stage.
    """
    def __init__(self):
        self.x_train_scaled = None
        self.scaler = None
        self.fin_model = None
        pass

    @abstractmethod
    def create_model(self, x, y):
        """
        :param x: Features of data to be trained on
        :type x: 2D numpy array, 2d list, or a data frame
        :param y: Labels of the corresponding features
        :type y: 1D numpy array or list
        :return: model and scaler
        :rtype: object
        """
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
    """k-Nearest Neighbours Classifier"""
    def __init__(self):
        Classifier.__init__(self)

    def create_model(self, x, y):
        Classifier.create_model(x, y)
        knc = KNeighborsClassifier(10)
        self.fin_model = knc.fit(self.x_train_scaled, y)
        return self.fin_model, self.scaler


class RFC(Classifier):
    """Random forest Classifier"""
    def __init__(self):
        Classifier.__init__(self)

    def create_model(self, x, y):
        Classifier.create_model(x, y)
        rfc = RandomForestClassifier(max_depth=800, n_estimators=800, max_features='auto', n_jobs=8)
        self.fin_model = rfc.fit(self.x_train_scaled, y)
        return self.fin_model, self.scaler


class DTC(Classifier):
    """Decision Tree Classifier"""
    def __init__(self):
        Classifier.__init__(self)

    def create_model(self, x, y):
        Classifier.create_model(x, y)
        dtc = DecisionTreeClassifier(max_depth=3000)
        self.fin_model = dtc.fit(self.x_train_scaled, y)
        return self.fin_model, self.scaler
