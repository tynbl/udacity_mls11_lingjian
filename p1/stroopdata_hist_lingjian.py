# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# 设置绘图样式
plt.style.use('seaborn-colorblind')

# 读取数据
df = pd.read_csv('stroopdata.csv')

# 绘制直方图
df.plot(kind='hist', alpha=0.5).get_figure().savefig('stroopdata_hist.png')
