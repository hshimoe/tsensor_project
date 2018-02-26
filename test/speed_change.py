#coding:utf-8

#シリアル通信で文字をArduino側に送信
#aが押されたら通信を中止するプログラム

import serial   #モジュール名はpyserialだが, importする際はserialである
port_num = "/dev/ttyACM0"
ser= serial.Serial(port_num,9600,timeout=1)

def right_speed_up():
    flag=bytes('s','utf-8')
    ser.write(flag)
    #ser.close()
        
def left_speed_up():
    flag=bytes('j','utf-8')
    ser.write(flag)
    #ser.close()

char = input()
if char == "1":
	print(char)
	right_speed_up()

char = input()
if char == "2":
	print(char)
	left_speed_up()
ser.close()
