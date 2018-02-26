# -*- coding: utf-8 -*-
import pandas
import numpy as np
import matplotlib.py as plt
import os
#データの入ったファイルパス指定
#一度.xlsx形式をexcelで開けた後/txtファイル形式(tab区切り)でデータを読み込む

over_sample_num = 100#タイムフィルタサイズ
sample_rate = 1000
filename ="./test_001.lvm"
data_size = 3

csv = pandas.read_csv(filename, sep='\t', encoding="shift-jis", error_bad_lines=False)
data = np.array(csv.ix[ : , 1:data_size+1],dtype = np.float32 ).T
print(data)
conv = np.ones(over_sample_num)
for i in range(data_size):
	tmp = np.convolve(data[i], conv, mode = 'full')
	tmp = tmp[over_sample_num:int(data.shape[1])-over_sample_num]/over_sample_num
	x = np.array(range(tmp.shape[0]))/sample_rate
	plt.plot(x, tmp)
plt.xlabel("time(sec)")
plt.ylabel("voltage")

plt.show() #見たければどうぞ