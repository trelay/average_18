#!/usr/bin/env python3
#coding=utf-8
import matplotlib.pyplot as plt
import tushare as ts
from pandas import DataFrame
import pandas as pd
import numpy as np
import math

code = "000651.SZ"

pro = ts.pro_api('418443b56e07ac5c235d232406b44db8f80484569f8240f4554c6d67')
df = pro.query('daily', ts_code=code, start_date='20171001', end_date='20190422')
df['trade_date'] = pd.to_datetime(df['trade_date'])

df.index = df.trade_date

fig = plt.figure()
gree_test = DataFrame(df, columns = ["open", "close", "high"])
print(gree_test)

gree_test = gree_test.sort_index(ascending=True)
gree_test.plot()
plt.show()
