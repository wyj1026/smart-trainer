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

        indexs = segmentation.get_min_coords(self.data_frame.get("NeckY"), 10)
        #draw_data_frame_with_split_lines(self.data_frame.get("NeckY"), indexs)
        
        x = segmentation.segment_data_into_repeats(self.data_frame, "NeckY", mn=True, delta=10)
        x = normalization.normalize([np.array(df) for df in x])
        draw_reps(x)
        self.assertEqual(len(x), 10)


if __name__ == '__main__':
    unittest.main()