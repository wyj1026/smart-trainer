# coding: utf-8

import numpy as np
from .data import read_data


"""
对给定的坐标，找出其中最小的点用来分割动作
"""
def get_min_coords(coords, delta, ctn=10):
    indexs = []
    min_coord = np.min(coords)
    i = 0
    index = 0
    while i < np.size(coords):
        current_min_coord = np.max(coords)
        index = 0
        continuation = 0
        while(i < np.size(coords) and abs(coords[i] - min_coord) < delta):
            if coords[i] < current_min_coord:
                index = i
                current_min_coord = coords[i]
            i = i + 1
            continuation = continuation + 1
        if index and continuation >= ctn:
            indexs.append(index)
        i = i + 1
    return indexs


"""
对给定的坐标，找出其中最大的点用来分割动作
"""
def get_max_coords(coords, delta):
    indexs = []
    max_coord = np.max(coords)
    i = 0
    index = 0
    while i < np.size(coords):
        current_max_coord = 0.
        index = 0
        while(i < np.size(coords) and abs(coords[i] - max_coord) < delta):
            if coords[i] > current_max_coord:
                index = i
                current_max_coord = coords[i]
            i = i + 1
        if index:
            indexs.append(index)
        i = i + 1
    return indexs


"""
对已经粗略划分的动作进行微调保证每个动作所占帧相同
"""
def repeat_tunning(coords, index):
    pass


"""
把原始数据分割成一个个动作，delta表示最大距离，如果原始数据的最大值为x，
那么从每个x-delta开始会更新一个最大值，根据不同的动作可能需要修改
mn表示是否以最小值划分
"""
def segment_data_into_repeats(data_frame, column, mn=True, delta=20):
    repeats = []
    coords = data_frame.get(column)
    coords = np.array(coords)
    if mn:
        coord_indexs = get_min_coords(coords, delta)
    else:
        coord_indexs = get_max_coords(coords, delta)
    
    if coord_indexs:
        start = coord_indexs[0]
        for i in range(1, len(coord_indexs)):
            repeats.append(data_frame[start: coord_indexs[i]].reset_index(drop=True))
            start = coord_indexs[i]
    return repeats
