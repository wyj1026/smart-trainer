from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier, ExtraTreesClassifier


classifiers = {
    "exercise": {
        "estimator": GaussianNB
    },
    "stance_shoulder_width": {
        "estimator": GradientBoostingClassifier,
        "learning_rate": 0.1,
        "max_depth": 4,
        "max_features": 0.55,
        "min_samples_leaf": 11,
        "min_samples_split": 20,
        "n_estimators": 100,
        "subsample": 0.3
    },
    "knees_over_toes": {
        "estimator": ExtraTreesClassifier,
        "bootstrap": False,
        "criterion": "gini",
        "max_features": 0.35,
        "min_samples_leaf": 1,
        "min_samples_split": 9,
        "n_estimators": 100
    },
    "bend_hips_knees": {
        "estimator": LogisticRegression,
        "C": 15,
        "dual": False,
        #"penalty": 12
    },
    "back_hip_angle": {
        "estimator": ExtraTreesClassifier,
        "bootstrap": False,
        "criterion": "entropy",
        "max_features": 0.9,
        "min_samples_leaf": 2,
        "min_samples_split": 3,
        "n_estimators": 100
    },
    "depth": {
        "estimator": ExtraTreesClassifier,
        "bootstrap": False,
        "criterion": "gini",
        "max_features": 0.7,
        "min_samples_leaf": 2,
        "min_samples_split": 6,
        "n_estimators": 100
    }
}