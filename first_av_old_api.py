#!/usr/bin/env python3
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import datetime
import pandas as pd
import numpy as np
import math

now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-500)
start_time = yes_time.strftime('%Y-%m-%d')
end_time = now_time.strftime('%Y-%m-%d')

df = ts.get_hist_data('sh',start=start_time,end=end_time)

sh_df = DataFrame(df, columns = ["open", "close", "high"])
sh_df = sh_df.sort_index(ascending=True)
close = sh_df["close"]

av_18 = []
i=0
for date in close.index:
    av_18.append(close[:i][-18:].mean())
    i+=1
sh_df.insert(2, "av", av_18, True)


fig = plt.figure()
#fig = plt.figure(figsize=(19.20,10.80))
sh_df.plot()

plt.savefig("/home/trelay/sh.png", dpi =800)
plt.show()