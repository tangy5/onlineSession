"""
This script is designed for CS1104 Online Session.
Mini project 1: Diabetes prediction

Author: Yucheng Tang
Date: June, 2020

"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

diabetes_file = '/Users/tangy5/Dropbox/teaching/cs1104/2020-1-summer/labs/lab02/diabetes/diabetes_digitalized.csv'

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

diabetes = pd.read_csv(diabetes_file, delim_whitespace=True)

diabetes = diabetes.loc[:, diabetes.columns != 'id']
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'outcome'], diabetes['outcome'], stratify=diabetes['outcome'], random_state=66)

#-----------------------------------------------------------------------KNN
training_accuracy = []
test_accuracy = []
# try n_neighbors from 1 to 10
neighbors_settings = range(1, 11)
for n_neighbors in neighbors_settings:
    # build the model
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    # record training set accuracy
    training_accuracy.append(knn.score(X_train, y_train))
    # record test set accuracy
    test_accuracy.append(knn.score(X_test, y_test))
plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.savefig('knn_compare_model')
#
# #---------------------------------------------------------------------logistic regression
# from sklearn.linear_model import LogisticRegression
# logreg = LogisticRegression().fit(X_train, y_train)
# print("Training set score: {:.3f}".format(logreg.score(X_train, y_train)))
# print("Test set score: {:.3f}".format(logreg.score(X_test, y_test)))
#
#
#
# #-----------------------------------------------------------SVM
# from sklearn.svm import SVC
# svc = SVC()
# svc.fit(X_train, y_train)
# print("Accuracy on training set: {:.2f}".format(svc.score(X_train, y_train)))
# print("Accuracy on test set: {:.2f}".format(svc.score(X_test, y_test)))
#
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.fit_transform(X_test)
# svc = SVC()
# svc.fit(X_train_scaled, y_train)
# print("Accuracy on training set: {:.2f}".format(svc.score(X_train_scaled, y_train)))
# print("Accuracy on test set: {:.2f}".format(svc.score(X_test_scaled, y_test)))

