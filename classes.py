# -*- coding: utf-8 -*-
import pandas
import numpy as np
import os
import serial 
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import plot_model
from collections import deque
from keras import backend as K

class DQN:
    def __init__(self, learning_rate=0.001, gamma=0.99, batch_size=32, data_size = 20, dim_num=3 ,action_size = 2): #未記述アリ
        #初期定義
        self.gamma = gamma
        self.batch_size = batch_size
        self.data_size = data_size
        self.action_size = action_size
        self.dim_num = dim_num

        self.model = Sequential()
		self.model.add(Dense(64, activation='relu', input_dim=data_size * dim_num * 2+))
		self.model.add(Dense(32, activation='relu'))
		self.model.add(Dense(2, activation='liner'))
        ######
        # ここにモデル構造を記述
        # 記述方式
        # self.model.add(Dense(hidden_size, activation, input_dim=state_size))
        #####
        self.optimizer = Adam(lr=learning_rate) #とりあえずのAdam
		self.model.compile(loss='mse', optimizer=self.optimizer)
    
    def replay(self, min_batch):
        inputs = np.zeros((self.batch_size, self.data_size)) #入力データ(速度, データ)
		targets = np.zeros((self.batch_size, self.action_size))#出力データ(動作)
        
        for i, (state, next_state, speed, action, reward, flag) in enumerate(mini_batch):
			inputs[i:i + 1] = state
			target = reward 
            if flag: #終了時以外で呼び出し
				target_act = self.predict_action(next_state)
				target = reward_b + self.gamma * np.max(target_act)
			targets[i] = self.predict_action(state)    # Qネットワークの出力
			targets[i][action_b] = target              # 教師信号

		self.model.fit(inputs, targets, epochs=1, verbose=0)  # epochsは訓練データの反復回数、verbose=0は表示なしの設定
    
    def predict_action(self, data):
        return self.model.predict(data) 



class Actor:
    def __init__(self, ):
        self.action = 0
        self.counter =0

    def calc_explore(self):
        return explore_p = 0.01 + 0.99*np.exp(-0.0001*self.counter)

    def choice_action(self, model):
        if self.calc_explore() <= np.random.rand():#乱数の方が大きいならば,モデルを用いた行動
		    Qs = model.predict_action(state)
	    	action = np.argmax(Qs)
        else :
            action = np.random.choice([0, 1])
        return action

    def act_to_serial(self, ser):
        if self.action == 0:
            ser.right_speed_up()
        if self.action == 1:
            ser.left_speed_up()
    
    def act_stop(self, ser):
        ser.pulse_stop()

    def expirat_action(serial):


class Memory:
    def __init__(self):
		self.buffer = deque(maxlen=max_size)        
  
    def add(self):
        self.buffer.append(experience)
  
    def top(self):
        return self.buffer[-1]

    def get_min_batch(self, batch_size):
        idx = np.random.choice(np.arange(len(self.buffer)), size=batch_size, replace=False)
		return [self.buffer[ii] for ii in idx]


class Preprocessing:
    def __init__(self ,dim_num=3 ,init_speed=1000 ,init_action=0,filename="./test_001.lvm"):
        self.dim_num = dim_num

        self.old_data = np.array(pandas.read_csv(filename, sep='\t', encoding="shift-jis", error_bad_lines=False).ix[ : , 1:data_num+1],dtype = np.float32 ).T
        self.old_data = self.calc_FFT(self.old_data)#FFT項

        self.data = self.old_data
        self.spd = init_speed #[mm]
        self.act = init_action 
        self.rwd = self.calc_reward()
        self.flg = True 

    def updata(self, action, expirat_flag):
        self.old_data = self.data
        self.data = np.array(pandas.read_csv(filename, sep='\t', encoding="shift-jis", error_bad_lines=False).ix[ : , 1:data_num+1],dtype = np.float32 ).T
        self.data= self.calc_FFT(self.data) #FFT項

        self.spd = self.calc_speed(action)
        self.act = action
        self.rwd = self.calc_reward(expirat_flag)
        self.flg = self.calc_flag(expirat_flag)

    def calc_speed(self, action, acc_size = 100):
        speed = self.spd + action * acc_size
        return speed

    def calc_reward(self):
        #calc_FFTの実装次第で設計変わるので注意
        #peek_freq = np.argmax(self.data)
        peek_freq = self.data[0,0]
        if 110 < peek_freq < 130:
            reward = 1
        else:
            reward = 0
        #####
        #rewardの計算処理
        #目的値ならば1
        #目的以外ならば0
        #目的外終了ならば<0
        #ちょっと考える
        #####
        return reward

    def calc_flag(self, expirat_flag):
        flag = True
        if self.rwd < 0 or expirat_flag:
            flag = False
        return flag

    def calc_FFT(self):
        #fft > arg(hz)の上位20個を配列として返す?要相談
        hz_size = 20
        data_size =int(self.data.shape[1]/2)
        fft_data = np.empty((self.dim_num, 2, hz_size))
        for i in range(self.dim_num):
            fft_data[i,0] = (np.argsort(np.abs(np.fft.fft(data[i]))[:data_size])[::-1])[:hz_size]
            fft_data[i,1] = (np.sort(np.abs(np.fft.fft(data[i]))[:data_size])[::-1])[:hz_size]            
        return fft_data

    def get_param(self):
        return self.old_data, self.data, self.spd, self.act, self.rwd, self.flg


class StageController:
    def __init__(self, port_name):
        self.ser = serial.Serial(port_num,9600,timeout=1)
        
    def right_speed_up(self):
        flag=bytes('s','utf-8')
        self.ser.write(flag)
        
    def left_speed_up(self):
        flag=bytes('j','utf-8')
        self.ser.write(flag)

    def pulse_stop(self):
        flag=bytes('s','utf-8')
        self.ser.write(flag)

    def return_to_origin(self):
        flag=bytes('o','utf-8')
        self.ser.write(flag)
        #原点復帰命令をArduino側に記述