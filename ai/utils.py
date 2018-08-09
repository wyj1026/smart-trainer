# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

def draw_data_frame(df):
    plt.plot(df)
    plt.show()


def draw_data_frame_split_lines(df, lines):
    plt.plot(df)
    for l in lines:
        plt.axvline(l, color="r")
    plt.show()


def draw_reps(reps):
    for r in reps:
        plt.plot(r)
    plt.show()