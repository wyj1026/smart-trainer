# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

def draw_data_frame(df):
    plt.plot(df)
    plt.show()


def draw_data_frame_with_split_lines(df, lines):
    plt.plot(df)
    for l in lines:
        plt.axvline(l, color="r")
    plt.show()


def draw_reps(reps):
    for i in range(len(reps)):
        plt.plot(reps[i], label=i)
    plt.legend(loc=0)
    plt.show()