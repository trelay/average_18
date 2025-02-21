#!/usr/bin/env python3
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import pandas as pd
import numpy as np
import math


df = ts.get_hist_data('000651')
print(df)
print(type(df.index[0]))
fig = plt.figure()
gree_test = DataFrame(df, columns = ["open", "close", "high"])
data_2019=gree_test["close"].sort_index(ascending=True)
data_2019.cumsum()
data_2019.plot()
plt.show()