# -*- coding: utf-8 -*-
import pandas
import numpy as np
import matplotlib.pyplot as plt
import os
#データの入ったファイルパス指定
#一度.xlsx形式をexcelで開けた後/txtファイル形式(tab区切り)でデータを読み込む

class SensorData:
	def __init__(self, data_size=3, sample_rate=25000,  filename="./test_001.lvm"):
		self.data = np.array(pandas.read_csv(filename, sep='\t', encoding="shift-jis", error_bad_lines=False).ix[ : , 1:data_size+1],dtype = np.float32 ).T
		self.data_size = data_size
		self.sample_rate = sample_rate

	def oversample(self, over_sample_num=1):
		conv = np.ones(over_sample_num)
		oversampled_data = np.empty((self.data_size, self.data.shape[1]-over_sample_num*2))
		for i in range(self.data_size):
			tmp = np.convolve(self.data[i], conv, mode = 'full')
			oversampled_data[i] = tmp[over_sample_num:int(self.data.shape[1])-over_sample_num]/over_sample_num
		return oversampled_data

	def prot(self):
		tmp = self.oversample()
		for i in range(self.data_size):
			x = np.array(range(tmp.shape[1]))/self.sample_rate
			plt.plot(x, tmp[i])
		plt.xlabel("time(sec)")
		plt.ylabel("voltage")
		plt.show()