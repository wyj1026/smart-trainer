# coding: utf-8

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, "c:/Users/wangy/Desktop/smart-trainer/")

from matplotlib import animation
from ai.preprocess import *
from ai.data.joint_coords import columns

class ActionVisualizer(object):
    def __init__(self, data_path, key="NeckY", delta=10):
        self.key = key
        self.delta = delta
        self.data = data.read_data(data_path)
        self.data_frame = data.convert_data_into_DF(self.data, columns)
        self.indexs = segmentation.get_min_coords(self.data_frame.get(key), 50)
        self._repeats = segmentation.segment_data_into_repeats(self.data_frame, key, mn=True, delta=50)
        self.normalized_repeats = normalization.normalize(self._repeats)

    def test(self):
        self.draw_data_frame_with_split_lines(self.data_frame.get(self.key), self.indexs)
        #draw_reps(self.normalized_repeats)
        self.draw_single_frame(self.normalized_repeats[0].ix[0])
        self.draw_repeat(np.array(self.normalized_repeats[0]))
        self.draw_repeat(np.array(self.data_frame))

    def draw_data_frame_with_split_lines(self, df, lines):
        plt.plot(df)
        plt.plot(np.gradient(df)*10)
        #plt.plot(np.gradient(df*10))
        for l in lines:
            plt.axvline(l, color="r")
        plt.show()

    @staticmethod
    def draw_reps(reps, key="NeckY"):
        for i in range(len(reps)):
            plt.plot(reps[i].get(key), label=i)
        plt.legend(loc=0)
        plt.show()

    def get_xy(self, coords):
        x = [-1*coords[i] for i in range(0, coords.size) if i % 3 == 0]
        y = [-1*coords[i] for i in range(0, coords.size) if i % 3 == 1]
        return x, y

    def draw_single_frame(self, coords):
        x, y = self.get_xy(coords)
        plt.plot(x, y, linestyle='None', marker='o')
        plt.legend(loc=0)
        plt.show()

    def draw_repeat(self, repeat):
        frames = np.shape(repeat)[0]
        fig, ax = plt.subplots()
        x, y = self.get_xy(repeat[0])
        budy, = ax.plot(x, y, linestyle='None', marker='o')

        def init():
            return budy

        def update(newd):
            x, y = self.get_xy(repeat[newd])
            budy.set_data(x, y)
            return budy
    
        ani = animation.FuncAnimation(fig=fig, func=update, init_func=init, frames=frames, interval=50)
        plt.show()

if __name__ == '__main__':
    visualizer = ActionVisualizer("./ai/data/raw_squat_data/squatData33.txt", key="NeckY")
    #visualizer = ActionVisualizer("./ai/data/raw_squat_data/squatData50.txt", key="NeckY")
    visualizer.test()