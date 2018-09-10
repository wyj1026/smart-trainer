# coding: utf-8

import math


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
    cos = min(abs(a*a+b*b-c*c)/(2*b*c), 1)
    cos = max(cos, -1)
    return math.acos(cos)


def extract_main_frames(repeat, key="SpineBaseY", gap_ratio=0.1):
    frames = []
    frame_num = repeat.shape[0] - 1
    ratio = 0
    while ratio <= 1:
        index = int(ratio*frame_num)
        ratio += gap_ratio
        frames.append(repeat.iloc[[index]])
    return frames


def extract_features_from_repeat(repeat):
    features = []
    for frame in repeat:
        features.append(float(frame["KneeLeftX"]) - float(frame["KneeRightX"]))
        features.append(float(frame["AnkleLeftX"]) - float(frame["AnkleRightX"]))
        left_bend_knees = calculate_angle(frame, 'AnkleLeft','KneeLeft','HipLeft')
        left_bend_hips = calculate_angle(frame,'SpineMid','HipLeft','KneeLeft')
        right_bend_knees = calculate_angle(frame,'AnkleRight','KneeRight','HipRight')
        right_bend_hips = calculate_angle(frame,'SpineMid','HipRight','KneeRight')

        features.append(left_bend_hips)
        features.append(right_bend_hips)
        features.append(left_bend_knees)
        features.append(right_bend_knees)
    return features

def extract_features(repeats, key="SpineBaseY"):
    return [extract_features_from_repeat(extract_main_frames(repeat, key))
        for repeat in repeats]
