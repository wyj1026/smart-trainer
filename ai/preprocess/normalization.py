# coding: utf-8

import numpy as np


def normalize(repeats):
    max_value = max([np.max(r.values) for r in repeats])
    min_value = min([np.min(r.values) for r in repeats])
    return list(map(lambda repeat: (repeat - min_value)/(max_value-min_value), repeats))
    