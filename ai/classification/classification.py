# coding:utf-8

from sklearn import metrics, tree, model_selection
from sklearn.preprocessing import StandardScaler
from tpot import TPOTClassifier


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
        from ai.classification.best_classifiers import classifiers
        estimator = classifiers[classifier_name].pop("estimator")
        classifier = estimator(**classifiers[classifier_name])
        classifier.fit(x_train, y_train)
    else:
        classifier = tree.DecisionTreeClassifier(max_depth=3, criterion="entropy")
        classifier.fit(x_train, y_train)
    
    predicted = classifier.predict(x_test)
    print("Classification report for classifier %s:\n%s\n"
        % (classifier.__class__, metrics.classification_report(y_test, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(y_test, predicted))
    trained_classifiers.append(classifier)
    return trained_classifiers
