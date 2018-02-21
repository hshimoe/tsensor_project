# -*- coding: utf-8 -*-
import pandas
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

data = np.arange(100)
window_size=10
shift_size = 5
data_size = 100
# for i in range(self.data_num):
tmp = np.empty((int(data_size/window_size)-1,0), int)
print(tmp)
for j in range(int(window_size/shift_size)):
	#print(data[shift_size*j: int(data_size/window_size-1)*window_size+shift_size*j])
	
	tmp =np.hstack((tmp, np.reshape(data[shift_size*j:int(data_size/window_size-1)*window_size+shift_size*j],(int(data_size/window_size)-1,window_size))))

print(tmp.reshape(-1,window_size))
	
	#tmp = np.reshape(,(window_size, data_size/window_size-1))
	#print(tmp)