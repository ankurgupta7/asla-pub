import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import KFold
from sklearn import svm
from sklearn import metrics
from sklearn import preprocessing
from sklearn.externals import joblib
#train and test data extraction
df = pd.read_csv('LeapData.csv')
df = df.drop_duplicates()
train_data = pd.DataFrame()
test_data = pd.DataFrame()
labels = set(df.sign)
for l in labels:
    temp = df[df['sign'] == l]
    temp = temp.reset_index(drop = True)
    train_data = train_data.append(temp.iloc[0:100])
    test_data = test_data.append(temp.iloc[100:140])

# resetting the index for both sets
test_data = test_data.reset_index(drop = True)
train_data = train_data.reset_index(drop = True)
#shuffling the rows in test and train data
train_data = train_data.iloc[np.random.permutation(len(train_data))]
test_data = test_data.iloc[np.random.permutation(len(test_data))]
test_data = test_data.reset_index(drop = True)
train_data = train_data.reset_index(drop = True)
x_train = train_data.ix[:, train_data.columns != 'sign']
y_train = train_data['sign']
x_test = test_data.ix[:, test_data.columns != 'sign']
y_test = test_data['sign']

#scaling the train data
scaler = preprocessing.StandardScaler().fit(x_train)
x_train_scaled = scaler.transform(x_train)
#x_train = x_train.as_matrix()

scores = []
for i in range(1,20):
    svc = svm.SVC(C=2*i, kernel='rbf')
    for train, valid in KFold(x_train_scaled.shape[0], 10,shuffle = True):
        scores.append(svc.fit(x_train_scaled[train],y_train[train]).score(x_train_scaled[valid],y_train[valid]))
    print ("CV accuracy: %0.2f (+/- %0.2f)" %(np.mean(scores), np.std(scores)**2)), 2*i



fin_model = svc.fit(x_train_scaled, y_train)
joblib.dump(fin_model, 'model_2.pkl')
joblib.dump(scaler, 'scaler_2.pkl')

#testing data prediction
scaler = preprocessing.StandardScaler().fit(x_test)
x_test_scaled = scaler.transform(x_test)

y_test_pred = svc.predict(x_test_scaled)
print metrics.classification_report(y_test, y_test_pred)