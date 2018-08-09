# coding: utf-8

import unittest
import sys
import os

sys.path.insert(0, "c:/Users/wangy/Desktop/smart-trainer/")

from ai.preprocess import *
from ai.utils import *

class TestPreprocess(unittest.TestCase):
    def setUp(self):
        self.data = data.read_data("./ai/data/squat_data/squatData12.txt")

    def test_datareader(self):
        self.assertEqual(len(self.data), 599)

    def test_segmentation(self):
        from ai.data.joint_coords import columns
        self.data_frame = data.convert_data_into_DF(self.data, columns)
        x = segmentation.segment_data_into_repeats(self.data_frame, "NeckY")
        self.assertEqual(len(x), 9)


if __name__ == '__main__':
    unittest.main()