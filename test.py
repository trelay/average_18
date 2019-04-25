import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
data = pd.Series(np.random.randn(16), index=list('abcdefghijklmnop'))
data.plot(kind='bar', color='k', alpha=0.7)
plt.show()
