# coding: utf-8

import numpy as np

from .features import squat_features

"""
对蹲起提取基本德特征，包括开始位置、中间位置、结束位置各个关节坐标
"""
def extract_basic_features(squats, key="NeckY"):
    extracted_features = []
    for squat in squats:
        features = []
        features.extend(squat.ix[0].tolist())
        mid_index = squat[key].values.argmax()
        features.extend(squat.ix[mid_index].tolist())
        features.extend(squat.ix[squat.shape[0]-1].tolist())
        extracted_features.append(np.array(features))
    return np.array(extracted_features)


def extract_all(squats):
    return [extract_features_from_squat(squat) for squat in squats]


def extract_features_from_squat(squat, features=squat_features):
    extracted_features = []
    features_funcs_dict = {}
    function_name = "extract_{}"
    for feature_name in features:
        features_funcs_dict[feature_name] = globals().get(function_name.format(feature_name))

    for feature_name in features:
        func = features_funcs_dict[feature_name]
        extracted_features.append(func())
    return extracted_features


def extract_stance_shoulder_width():
    pass


def extract_stance_straightness():
    pass
    

def extract_feet():
    pass


def extract_bend_hips_knees():
    pass


def extract_back_straight():
    pass


def extract_head_aligned_back():
    pass


def extract_depth():
    pass


def extract_back_hip_angle():
    pass


def extract_():
    pass