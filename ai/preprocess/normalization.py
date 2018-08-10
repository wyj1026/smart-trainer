# coding: utf-8

import numpy as np


def normalize(repeats):
    max_value = max([np.max(r) for r in repeats])
    min_value = min([np.min(r) for r in repeats])
    return list(map(lambda arr: (arr - min_value)/(max_value-min_value), repeats))
    