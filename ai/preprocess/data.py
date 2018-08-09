import pandas as pd

"""
根据文件名读取文件数据，并且以逗号分割后转化为数组。
"""
def read_data(filename):
    with open(filename, "r") as f:
        data = []
        for l in f:
            data.append(list(map(lambda x: float(x), l.strip().split(","))))
    return data


"""
把数据转化成pandas的DataFrame
"""
def convert_data_into_DF(data, columns):
    if data and len(data[0]) == len(columns):
        return pd.DataFrame(data, columns=columns)
    
    
