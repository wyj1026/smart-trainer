# coding: utf-8

import sys
sys.path.insert(0, "c:/Users/wangy/Desktop/smart-trainer/")

import numpy as np

from ai.preprocess import *
from ai.data.joint_coords import columns
from ai.features import pushup_features_extractor
from ai.features import squat_features_extractor
from ai.classification import *

class AI(object):
    def __init__(self):
        self.data = {}
        self.repeats = {}
        self.features = {}
        self.labels = {}
        self.classifiers = {}
        
    def load_data(self, path, exercise="squat"):
        raw_data = data.read_data(path)
        if exercise in self.data:
            self.data[exercise].extend(data.convert_data_into_DF(raw_data, columns))
        else:
            self.data[exercise] = data.convert_data_into_DF(raw_data, columns)
    
    def process_data(self, exercise="squat", column="NeckY", delta=10):
        if not exercise in self.data:
            return
        repeats = segmentation.segment_data_into_repeats(self.data[exercise], column, mn=True, delta=delta)
        normalized_repeats = normalization.normalize(repeats)
        self.repeats[exercise] = normalized_repeats
        
    def extract_features(self, exercise="squat"):
        if exercise == "squat":
            self.features[exercise] = squat_features_extractor.extract_basic_features(self.repeats[exercise])
        
    def load_classifier(self):
        pass

    def save_classifier(self):
        pass

    def train_classifier(self, exercise):
        classifier = None
        self.classifiers[exercise] = classifier
    
    def classify(self):
        pass


if __name__ == "__main__":
    ai = AI()
    ai.load_data("./ai/data/squat_data/squatData12.txt")
    ai.process_data()
    ai.extract_features()
    print(ai.features["squat"][0].shape)