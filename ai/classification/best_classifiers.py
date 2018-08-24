from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


s = {
    "back_hip_angle": RandomForestClassifier(LogisticRegression(None, C=0.5, dual=False),
                                             bootstrap=True,
                                             criterion="entropy",
                                             max_features=0.7,
                                             min_samples_leaf=5,
                                             min_samples_split=15),
    "stance_shoulder_width": tree.DecisionTreeClassifier(class_weight=None, criterion="entropy", max_depth=3),
    "knees_over_toes": tree.DecisionTreeClassifier(class_weight=None, criterion="entropy", max_depth=3),
    "back_hip_angle": tree.DecisionTreeClassifier(class_weight=None, criterion="entropy", max_depth=3),
    "depth": tree.DecisionTreeClassifier(class_weight=None, criterion="entropy", max_depth=3)
}