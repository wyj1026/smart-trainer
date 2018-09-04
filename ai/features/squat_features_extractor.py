# coding: utf-8

import math

import numpy as np

from .features import squat_features


"""
求两点距离
"""
def calculate_distance(point1, point2):
    su = 0
    for k in point1.keys():
        su += math.pow(point1[k] - point2[k], 2)
    return math.sqrt(su)


"""
求三点夹角（二维或三维）
"""
def calculate_angle(squat_frame, left_point_name, central_point_name, right_point_name, dimention=('X', 'Y', 'Z')):
    left_point = {}
    central_point = {}
    right_point = {}
    for d in dimention:
        left_point[d] = squat_frame.get(left_point_name + d)
        central_point[d] = squat_frame.get(central_point_name + d)
        right_point[d] = squat_frame.get(right_point_name + d)
    a = calculate_distance(left_point, central_point)
    b = calculate_distance(right_point, central_point)
    c = calculate_distance(left_point, right_point)
    return math.acos(abs(a*a + b*b - c*c)/(2*b*c+0.01))


"""
对蹲起提取一些关键帧
"""
def extract_main_frames(squat, key="NeckY", gap_ratio=0.2):
    frames = []
    squat_frames_num = squat.shape[0] - 1
    ratio = 0
    while ratio <= 1:
        index = int(squat_frames_num*ratio)
        ratio += gap_ratio
        frames.append(squat.iloc[[index]])
    return frames

"""
提取蹲起的特征
"""
def extract_features(squats, targets=squat_features):
    return [extract_features_from_squat(extract_main_frames(squat), targets) for squat in squats]


"""
对于给定的squat， 以二维数组返回其所有的features，每一行为一个feature
"""
def extract_features_from_squat(squat, targets=squat_features):
    extracted_features = []
    features_funcs_dict = {}
    function_name = "extract_{}"
    for feature_name in targets:
        features_funcs_dict[feature_name] = globals().get(function_name.format(feature_name))

    for feature_name in targets:
        func = features_funcs_dict[feature_name]
        extracted_features.append(func(squat))
    return extracted_features


def extract_stance_shoulder_width(squat):
    features = []
    for frame in squat:
        features.append(float(frame["AnkleLeftX"] - frame["ShoulderLeftX"]))
        features.append(float(frame["AnkleRightX"] - frame["ShoulderRightX"]))
    return features


def extract_knees_over_toes(squat):
    features = []
    for frame in squat:
        features.append(float(frame["KneeLeftZ"] - frame["AnkleLeftZ"]))
        features.append(float(frame["KneeRightZ"] - frame["AnkleRightZ"]))
    return features


def extract_bend_hips_knees(squat):
    features = []
    left_bend_knees = [calculate_angle(state, 'AnkleLeft','KneeLeft','HipLeft') for state in squat]
    left_bend_hips = [calculate_angle(state,'SpineMid','HipLeft','KneeLeft') for state in squat]
    right_bend_knees = [calculate_angle(state,'AnkleRight','KneeRight','HipRight') for state in squat]
    right_bend_hips = [calculate_angle(state,'SpineMid','HipRight','KneeRight') for state in squat]
    #ratios = np.concatenate([get_angle_changes(left_bend_hips,left_bend_knees),get_angle_changes(right_bend_hips,right_bend_knees)])
    
    features.extend(left_bend_hips) 
    features.extend(right_bend_hips) 
    features.extend(left_bend_knees) 
    features.extend(right_bend_knees)
    return features

def extract_depth(squat, key="SpineBaseY"):
    features = []
    lowest = max(squat, key=lambda x: float(x[key]))
    features.append(float(lowest["HipLeftY"]))
    features.append(float(lowest["HipRightY"]))
    left_angle = calculate_angle(lowest, "AnkleLeft", "KneeLeft", "HipLeft")
    right_angle = calculate_angle(lowest, "AnkleRight", "KneeRight", "HipRight")
    features.append(left_angle)
    features.append(right_angle)
    return features


def extract_back_hip_angle(squat):
    features = []
    for frame in squat:
        h = abs(float(frame['NeckY']) - float(np.average([float(frame['HipLeftY']), float(frame['HipRightY'])])))
        b = float(frame['NeckZ'] - np.average([float(frame['HipLeftZ']), float(frame['HipRightZ'])]))
        features.append(h/b)      
    return features