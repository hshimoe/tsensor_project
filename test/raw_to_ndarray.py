# -*- coding: utf-8 -*-
import pandas
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

class SensorData:
	def __init__(self, data_num=3, sample_rate=25000,  filename="./test_001.lvm"):
		self.data = np.array(pandas.read_csv(filename, sep='\t', encoding="shift-jis", error_bad_lines=False).ix[ : , 1:data_num+1],dtype = np.float32 ).T
		self.data_size = self.data.shape[1]
		self.data_num = data_num
		self.sample_rate = sample_rate

	def make_dummy(self, dummy_num = 100):
		self.data = np.empty((0,dummy_num), int)
		for i in range(self.data_num):
			self.data = np.vstack((self.data,np.arange(dummy_num*i, dummy_num*(i+1))))
		self.data_size = dummy_num

	def oversample(self, over_sample_num=1):
		conv = np.ones(over_sample_num)
		oversampled_data = np.empty((self.data_num, self.data_size-over_sample_num))
		for i in range(self.data_num):
			tmp = np.convolve(self.data[i], conv, mode = 'full')
			oversampled_data[i] = tmp[:int(self.data_size)-over_sample_num]/over_sample_num
		self.data = oversampled_data

	def plot(self):
		tmp = self.data
		for i in range(self.data_num):
			x = np.array(range(data_size))/self.sample_rate
			plt.plot(x, tmp[i])
		plt.xlabel("time(sec)")
		plt.ylabel("voltage")
		plt.show()

	def split(self, window_size=1000, shift_size=1000):
		#エラー処理
		if window_size % shift_size != 0:
			print("value error :window_size must be divisible by shift_size")
			sys.exit()
		#データ格納用の変数
		split_data = np.empty((self.data_num,int(int(self.data_size/window_size-1)*window_size/shift_size),window_size)) 
		for i in range(self.data_num):
			tmp = np.empty((int(self.data_size/window_size)-1,0)) #初期化
			for j in range(int(window_size/shift_size)): 
				#スプリット分割,シフトして繰り返す
				tmp = np.hstack((tmp, np.reshape(self.data[i,shift_size*j:int(self.data_size/window_size-1)*window_size+shift_size*j],(int(self.data_size/window_size)-1,window_size))))
			#reshapeして目的の形に整形
			split_data[i]=tmp.reshape(-1,window_size)
		return split_data

	def get_data_x(self, num):
		return self.data[num]