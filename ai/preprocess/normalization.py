# coding: utf-8

import numpy as np


def normalize(arr):
    max_value = np.max(arr)
    min_value = np.min(arr)
    return (arr - min_value)/(max_value-min_value)