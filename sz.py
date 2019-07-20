import tushare  as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = ts.get_h_data('399300',start='2010-01-01',end='2019-07-31',index=True)
df.head(10)

sz=df.sort_index(axis=0, ascending=True) #对index进行升序排列
sz_return=sz[['close']] #选取涨跌幅数据
train=sz_return[0:255] #划分训练集
test=sz_return[255:]   #测试集
#对训练集与测试集分别做趋势图
plt.figure(figsize=(10,5))
train['close'].plot()
plt.legend(loc='best')
#plt.show()
plt.figure(figsize=(10,5))
test['close'].plot(c='r')
plt.legend(loc='best')
plt.show()
