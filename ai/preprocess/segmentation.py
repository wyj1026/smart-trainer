# coding: utf-8

import numpy as np
from .data import read_data

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
        while(abs(coords[i] - max_coord) < delta):
            if coords[i] > current_max_coord:
                index = i
                current_max_coord = coords[i]
            i = i + 1
        if index:
            indexs.append(index)
        i = i + 1
    return indexs


"""
把原始数据分割成一个个动作，delta表示最大距离，如果原始数据的最大值为x，
那么从每个x-delta开始会更新一个最大值，根据不同的动作可能需要修改
"""
def segment_data_into_repeats(data_frame, column, delta=20):
    repeats = []
    coords = data_frame.get(column)
    coords = np.array(coords)
    max_coord_indexs = get_max_coords(coords, delta)
    
    if max_coord_indexs:
        start = max_coord_indexs[0]
        for i in range(1, len(max_coord_indexs)):
            repeats.append(coords[start: max_coord_indexs[i]])
            start = max_coord_indexs[i]
    return repeats
