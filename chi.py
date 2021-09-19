import numpy as np
import pandas as pd

decimals = 4
data = pd.read_csv("chi_data.txt", delimiter="\n", header=None)
data = data.round(decimals)
N = len(data[0].index)
dMax = data[0].max()
dMin = data[0].min()

classes = pd.DataFrame(columns=['interval', 'frequency'])
for i in range(c):
    lower = (dMin + (w * i))
    upper = dMin + w * (i + 1)
    classes.at[i, 'interval'] = '(' + str(round(lower, decimals)) + \
        ' - ' + str(round(upper, decimals)) + ']'
    classes.at[i, 'frequency'] = data[(
        data[0] >= lower) & (data[0] < upper)].shape[0]
