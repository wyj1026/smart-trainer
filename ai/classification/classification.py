# coding:utf-8

from sklearn import svm, metrics, linear_model, tree, model_selection
from tpot import TPOTClassifier


def train(X, Y, test_size=0.2):
    trained_classifiers = []
    x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=test_size)

    classifier = tree.DecisionTreeClassifier(max_depth=3, criterion="entropy")
    classifier.fit(x_train, y_train)
    
    predicted = classifier.predict(x_test)
    print("Classification report for classifier %s:\n%s\n"
        % (classifier, metrics.classification_report(y_test, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(y_test, predicted))
    trained_classifiers.append(classifier)
    return trained_classifiers


def find_best_classifier(X, Y, test_size=0.2):
        x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=test_size)
        tpot = TPOTClassifier(generations=6, verbosity=2)
        tpot.fit(x_train, y_train)
        tpot.score(x_test, y_test)
        tpot.export("tpot_pipeline.py")
