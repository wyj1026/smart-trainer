# coding: utf-8

import pickle
import sys
sys.path.insert(0, "c:/Users/wangy/Desktop/smart-trainer/")

import numpy as np

from ai.preprocess import *
from ai.data.joint_coords import columns
from ai.features import pushup_features_extractor
from ai.features import squat_features_extractor
from ai.classification import classification

class AI(object):
    def __init__(self):
        self.data = {}
        self.repeats = {}
        self.features = {}
        self.raw_labels = {}
        self.labels = {}
        self.classifiers = {}
        
    """
    读取单个文件，测试用，不应该再被使用
    """
    def read_file(self, path, exercise="squat"):
        raw_data = data.read_data(path)
        if exercise in self.data:
            self.data[exercise].extend(data.convert_data_into_DF(raw_data, columns))
        else:
            self.data[exercise] = data.convert_data_into_DF(raw_data, columns)

    """
    读取某目录下的所有文件
    """
    def read_files(self, directory, exercise="squat"):
        raw_data = data.read_all_available_data(directory)
        for k in raw_data.keys():
            raw_data[k] = data.convert_data_into_DF(raw_data[k], columns)
        self.data[exercise] = raw_data

    def read_raw_labels(self, exercise="squat"):
        lbs = {}
        if exercise == "squat":
            from ai.data import squat_labels as labels
        elif exercise == "pushup":
            from ai.data import pushup_labels as labels

        for attr in dir(labels):
            if attr.startswith("labels"):
                lbs[attr] = getattr(labels, attr)
        self.raw_labels[exercise] = lbs

    def save(self, path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    
    def load(self, path):
        with open(path, "rb") as f :
            return pickle.load(f)
    
    def process_data(self, exercise="squat", column="NeckY", delta=50):
        if not exercise in self.data:
            return
        self.repeats[exercise] = []
        self.labels[exercise] = []
        raw_data = self.data[exercise]
        raw_labels = self.raw_labels[exercise]
        for label_key in raw_labels.keys():
            data_keys = data.data_labels_key_map(label_key)
            repeats = []
            for data_key in data_keys:
                repeats.extend(segmentation.segment_data_into_repeats(raw_data[data_key], column, mn=True, delta=delta))
            if not len(repeats) == len(raw_labels[label_key]):
                print("label: {} SEGMENTATION ERROR! {} repeats with {} labels".format(
                    label_key,
                    len(repeats),
                    len(raw_labels[label_key])))
                # return 
            else:
                print("label: {}  {} repeats with {} labels".format(
                    label_key,
                    len(repeats),
                    len(raw_labels[label_key])))
                self.repeats[exercise].extend(repeats)
                self.labels[exercise].extend(raw_labels[label_key])

        normalized_repeats = normalization.normalize(self.repeats[exercise])
        self.repeats[exercise] = normalized_repeats
        
    def extract_features(self, exercise="squat"):
        if exercise == "squat":
            self.features[exercise] = squat_features_extractor.extract_basic_features(self.repeats[exercise])
        
    def load_classifier(self):
        pass

    def save_classifier(self):
        pass

    def train_classifier(self, exercise="squat"):
        classifier = classification.train_svm_classifier(self.features[exercise], [x[-3] for x in self.labels[exercise]])
        self.classifiers[exercise] = classifier
    
    def classify(self):
        pass


if __name__ == "__main__":
    ai = AI()
    #ai.read_raw_labels()
    #ai.read_files("./ai/data/raw_squat_data/")
    #ai.process_data()
    #ai.save("./ai/data/squat_data.pk", ai.repeats["squat"])
    #ai.save("./ai/data/squat_labels.pk", ai.labels["squat"])
    #ai.extract_features()
    #print(ai.features["squat"][0].shape)
    ai.repeats["squat"] = ai.load("./ai/data/squat_data.pk")
    ai.labels["squat"] = ai.load("./ai/data/squat_labels.pk")
    ai.extract_features()
    ai.train_classifier()