import os

import pandas as pd

"""
根据文件名读取文件数据，并且以逗号分割后转化为数组。
"""
def read_data(filename):
    with open(filename, "r") as f:
        data = []
        for l in f:
            try:
                values = l.strip().split(",")
                if values and values[-1] == "":
                    values.remove("")
                if len(values) != 75:
                    continue
                data.append(list(map(lambda x: float(x), values)))
            except ValueError as e:
                raise e
    return data


"""
读取文件目录下所有的数据
"""
def read_all_available_data(directory, endswith=".txt"):
    all_available_data = {}
    all_files = os.listdir(directory)
    for filename in all_files:
        if filename.endswith(endswith):
            file_data = read_data(directory + filename)
            all_available_data[filename] = file_data
    return all_available_data


"""
把数据转化成pandas的DataFrame
"""
def convert_data_into_DF(data, columns):
    if data and len(data[0]) == len(columns):
        return pd.DataFrame(data, columns=columns)
    

"""
labels 与 data文件名 对应函数

labels13--->squatData13.txt
"""
def data_labels_key_map(labels_key, exercise="squat"):
    num_list = labels_key[6:].split("_")
    data_keys = []
    data_key = "{}Data{}.txt"
    for num in num_list:
        data_keys.append(data_key.format(exercise, num))
    return data_keys

    if len(num_list) == 1:
        data_keys.append(data_key.format(exercise, num_list[0]))
    else:
        for num in range(int(num_list[0]), int(num_list[-1]) + 1):
            data_keys.append(data_key.format(exercise, num))
    return data_keys