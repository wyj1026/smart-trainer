# coding:utf-8

from sklearn import svm, metrics


def train_svm_classifier(X, Y, gamma=0.001):
    classifier = svm.SVC(gamma=gamma)

    n = len(X)
    train_X = X[int(n/3):]
    train_Y = Y[int(n/3):]
    classifier.fit(X, Y)
    
    expected = Y[:int(n/3)]
    predicted = classifier.predict(X[:int(n/3)])
    print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
    return classifier