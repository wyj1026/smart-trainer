# coding: utf-8

import pickle
import logging
import sys

sys.path.insert(0, "c:/Users/wangy/Desktop/smart-trainer/")

import numpy as np

from ai.preprocess import *
from ai.data.joint_coords import columns
from ai.features import pushup_features_extractor
from ai.features import squat_features_extractor
from ai.classification import classification
from ai.data.squat_labels import label_names as squat_label_names


class Trainer(object):
    def __init__(self, targets):
        self.targets = targets
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

    """
    读取标记好的label
    """
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
    
    """
    对原始的数据进行处理
    """
    def process_data(self, exercise="squat", column="SpineBaseY", delta=50):
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
        self.labels[exercise] = data.convert_data_into_DF(self.labels[exercise], squat_label_names)

    
    """
    提取特征
    """
    def extract_features(self, exercise="squat"):
        if exercise == "squat":
            self.features[exercise] = squat_features_extractor.extract_features(
                self.repeats[exercise],
                targets=self.targets)
        
    """
    训练模型
    """
    def train_classifier(self, exercise="squat", auto_ml=False, use_best_classifier=False):
        self.classifiers[exercise] = {}
        for i in range(len(self.targets)):
            f = [s_f[i] for s_f in self.features[exercise]]
            classifier = classification.train(
                f,
                self.labels[exercise].get(self.targets[i]),
                auto_ml=auto_ml,
                use_best_classifier=use_best_classifier,
                classifier_name=self.targets[i])
            self.classifiers[exercise][self.targets[i]] = classifier
    
    def classify(self, exercise, raw_data, key="SpineBaseY", delta=50):
        data_frame = data.convert_data_into_DF(raw_data, columns)
        repeats = segmentation.segment_data_into_repeats(data_frame, key, mn=True, delta=delta)
        normalized_repeats = normalization.normalize(repeats)
        if exercise == "squat":
            extracted_features = squat_features_extractor.extract_features(repeats, targets=self.targets)
        classifiers = self.classifiers[exercise]

        return [self.predict(features_list, classifiers) for features_list in extracted_features]

    def predict(self, features_list, classifiers):
        features = dict(zip(self.targets, features_list))
        result = []
        for feature_name in features.keys():
            if feature_name in classifiers.keys():
                result.extend(classifiers[feature_name][0].predict([features[feature_name]]))
        return result


if __name__ == "__main__":
    targets = ["stance_shoulder_width", "knees_over_toes", "bend_hips_knees", "back_hip_angle", "depth"]
    ai = Trainer(targets)
    """
    ai.read_raw_labels()
    ai.read_files("./ai/data/raw_squat_data/")
    ai.process_data(delta=30)
    ai.save("./ai/data/squat_data.pk", ai.repeats["squat"])
    ai.save("./ai/data/squat_labels.pk", ai.labels["squat"])
    ai.extract_features()
    ai.train_classifier()
    """

    ai.repeats["squat"] = ai.load("./ai/data/squat_data.pk")
    #import pandas as pd
    #pd.set_option('display.max_columns', None)
    #print(ai.repeats["squat"][0].head())
    ai.labels["squat"] = ai.load("./ai/data/squat_labels.pk")
    ai.extract_features()
    ai.train_classifier(auto_ml=False, use_best_classifier=True)
    ai.save("./ai/classification/squat_classifiers.pk", ai.classifiers["squat"])

    """
    # 使用
    ai.classifiers["squat"] = ai.load("./ai/classification/squat_classifiers.pk")
    raw_data = data.read_data("./ai/data/raw_squat_data/squatData14.txt")
    r = ai.classify("squat", raw_data)
    print(r)
    """
