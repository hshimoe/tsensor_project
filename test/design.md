# モデル構造記述

## DQNmodel 
### init
初期化
#### input
learning_rate(int)
state_size(int)
action_size(int)
hidden_size(int)
#### variable
model (keras)
Optimizer(標準の場合はこちらへ/改変する場合はメソッドへ)
gamma_number(float)
batch_size(int)
### replay
モデルの学習
#### inputda
mini_batch (buffer)
#### variable
Input(ndarray[data_size][data_num])
target(ndarray[action_num][data_num])

## Memory
### init
初期化
#### input
Buffer_size
#### variable
Buffer/deque(stock data)
### add
データの追加
#### input
new_data(ndarray[data_size][data_num])
data(ndarray[data_size][data_num])
Speed(float)
Reaward(int)
### top
最終追加データの出力
#### output
new_data(ndarray[data_size][data_num])
data(ndarray[data_size][data_num])
Speed(float)
Reaward(int)
### get_min_batch
#### input
batch_size(int)
#### output
mini_batch(buffer)


## Data_exchanger
### init
#### input
Datafile
#### variables
old_data[ndarray]
data[ndarray]
speed[floar]
Reward(int)
### file_to_data
ファイルをndarrayに変換
#### input
file(data_file)
data_num(int)
#### output
ndarray(ndarray[data_size][data_num])
#### variable 
### data_convolved(予定)
ファイルサイズや学習データ増加のための分割
### #input
window_size(int)
slide_size(int)
#### output
data(ndarray[windowsize, len/windowsize][window_size/slide_size])
### calc_reward
報酬値の計算
#### input
data(ndarray[data_size][data_num])
#### output
reward(int)
### get_param
#### output
data[ndarray]
old_data[ndarray]
speed[floar]
Reward(int)

## Actor
### init
#### input
Serial port name(string)
#### variable
action
ser1(serial connection)
ser2
move_size
explore
Timer
### calc_explore
ランダムアクション確率の計算
#### input
counter(int)
#### output
explore(float)
### calc_move_size
実際の動作量を計算
#### input
timer
action
#### output
move_size
### action_choice
行動方針の選択
#### input
model
#### out_put
choice_action_num(int)
### act_to_serial
Actionに対応したシリアルを出力する
### reset_move
初期位置へ戻る方向へ行動を制御
#### input
move_size
#### output
serial_com
timer
### read_end_point
#### input
move_size
#### output
flag(boolean)
###     
対応するシリアル通信制御
#### input
com(string)
ser
#### output
Serial_com