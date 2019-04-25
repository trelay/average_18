#!/usr/bin/env python3
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import pandas as pd
import numpy as np
import math

code = "000001.sh"
pro = ts.pro_api('418443b56e07ac5c235d232406b44db8f80484569f8240f4554c6d67')
df = pro.query('daily', ts_code=code, start_date='20171001', end_date='20190422')
df['trade_date'] = pd.to_datetime(df['trade_date'])
df.index = df.trade_date

fig = plt.figure()
gree_test = DataFrame(df, columns = ["open", "close", "high"])
gree_test = gree_test.sort_index(ascending=True)
print(gree_test)
#----------------------------------------------------------
close = gree_test["close"]

av_18 = []
i=0
for date in close.index:
    av_18.append(close[:i][-18:].mean())
    i+=1
#----------------------------------------------------------
gree_test.insert(2, "av", av_18, True)

gree_test.plot()
plt.savefig("./{}.png".format(code),dpi=800, bbox_inches='tight')

plt.show()