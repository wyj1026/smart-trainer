# coding:utf-8

from sklearn import svm, metrics, linear_model, tree

classifiers = [tree.DecisionTreeClassifier(max_depth=3, criterion="entropy"),
               svm.SVC(gamma=0.001),
               linear_model.LogisticRegression()]

def train(X, Y, classifiers=classifiers):
    trained_classifiers = []
    for classifier in classifiers:
        n = len(X)
        train_X = X[int(n/3):]
        train_Y = Y[int(n/3):]
        classifier.fit(X, Y)
        
        expected = Y[:int(n/3)]
        predicted = classifier.predict(X[:int(n/3)])
        print("Classification report for classifier %s:\n%s\n"
          % (classifier, metrics.classification_report(expected, predicted)))
        print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
        trained_classifiers.append(classifier)
    return trained_classifiers