# coding: utf-8

import matplotlib.pyplot as plt
from matplotlib import animation
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


def get_xy(coords):
    x = [-1*coords[i] for i in range(0, coords.size) if i % 3 == 0]
    y = [-1*coords[i] for i in range(0, coords.size) if i % 3 == 1]
    return x, y

def draw_single_frame(coords):
    x, y = get_xy(coords)
    plt.plot(x, y, linestyle='None', marker='o')
    plt.show()


def draw_repeat(repeat):
    print(repeat.size)
    fig, ax = plt.subplots()
    x, y = get_xy(repeat[0])
    budy, = ax.plot(x, y, linestyle='None', marker='o')

    def init():
        return budy

    def update(newd):
        x, y = get_xy(repeat[newd])
        budy.set_data(x, y)
        return budy
    
    ani = animation.FuncAnimation(fig=fig, func=update, init_func=init, frames=40, interval=20)
    plt.show()