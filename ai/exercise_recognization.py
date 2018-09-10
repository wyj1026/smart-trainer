# coding: utf-8

import pickle
import logging
import sys

sys.path.insert(0, "c:/Users/wangy/Desktop/smart-trainer/")

import numpy as np

from ai.preprocess import *
from ai.data.joint_coords import columns
from ai.features import exercise_features_extractor
from ai.classification import classification


class Recognizer(object):
    def save(self, path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    
    def load(self, path):
        with open(path, "rb") as f :
            return pickle.load(f)
    
    """
    提取特征
    """
    def extract_features(self):
        self.features = exercise_features_extractor.extract_features(self.repeats)

    """
    训练模型
    """
    def train_classifier(self, auto_ml=False, use_best_classifier=False):
        classifier = classification.train(
            self.features,
            self.labels,
            auto_ml=auto_ml,
            use_best_classifier=use_best_classifier,
            classifier_name="exercise")
        self.classifier = classifier
    
    def classify(self, exercise, raw_data, key="SpineBaseY", delta=50):
        data_frame = data.convert_data_into_DF(raw_data, columns)
        repeats = segmentation.segment_data_into_repeats(data_frame, key, mn=True, delta=delta)
        normalized_repeats = normalization.normalize(repeats)
        extracted_features = exercise_features_extractor.extract_features(normalized_repeats)
        classifier = self.classifier
        return classifier.predict(extracted_features)


if __name__ == "__main__":
    recognizer = Recognizer()
    recognizer.repeats = []
    squats = recognizer.load("./ai/data/squat_data.pk")
    recognizer.repeats.extend(squats)
    recognizer.labels = [1]*len(squats)

    pushups = recognizer.load("./ai/data/pushup_data.pk")
    recognizer.repeats.extend(pushups)
    recognizer.labels.extend([0]*len(pushups))

    recognizer.extract_features()
    recognizer.train_classifier(auto_ml=False, use_best_classifier=True)
    recognizer.save("./ai/classification/exercise_classifier.pk", recognizer.classifier)
