# coding:utf-8

import copy

import numpy as np

from sklearn import metrics, tree, model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve, ShuffleSplit
from sklearn.preprocessing import StandardScaler
from tpot import TPOTClassifier
from matplotlib import pyplot as plt

from ai.classification.best_classifiers import classifiers

def train(X, Y, test_size=0.2, auto_ml=False, use_best_classifier=False, classifier_name=None):
    trained_classifiers = []
    x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=test_size)
    #x_scaler = StandardScaler()
    #x_train = x_scaler.fit_transform(x_train)
    #x_test = x_scaler.transform(x_test)

    if auto_ml:
        classifier = TPOTClassifier(generations=6, verbosity=2)
        classifier.fit(x_train, y_train)
    elif use_best_classifier and classifier_name:
        cls = copy.deepcopy(classifiers)
        estimator = cls[classifier_name].pop("estimator")
        classifier = estimator(**cls[classifier_name])
        classifier.fit(x_train, y_train)
    else:
        classifier = tree.DecisionTreeClassifier(max_depth=3, criterion="entropy")
        #classifier = LogisticRegression(C=15, dual=False)
        classifier.fit(x_train, y_train)
    
    predicted = classifier.predict(x_test)
    print("Classification report for classifier %s:\n%s\n"
        % (classifier.__class__, metrics.classification_report(y_test, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(y_test, predicted))
    trained_classifiers.append(classifier)
    return trained_classifiers


def plot_learning_curve(X, Y, classifier_name):
    cls = copy.deepcopy(classifiers)
    estimator = cls[classifier_name].pop("estimator")

    estimator(**cls[classifier_name])
    train_sizes, train_scores, test_scores = learning_curve(
        estimator(**cls[classifier_name]), X, Y, cv=9,
        train_sizes=[0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    train_loss_mean = np.mean(train_scores, axis=1)
    test_loss_mean = np.mean(test_scores, axis=1)

    plt.plot(train_sizes, train_loss_mean, 'o-', color="r",
             label="Training")
    plt.plot(train_sizes, test_loss_mean, 'o-', color="g",
             label="Testing")

    plt.xlabel("Training examples")
    plt.ylabel("Score")
    plt.legend(loc="best")
    plt.show()