#coding:utf-8

#シリアル通信で文字をArduino側に送信
#aが押されたら通信を中止するプログラム

import serial   #モジュール名はpyserialだが, importする際はserialである

port_num = "COM1"
def right_speed_up():
    with serial.Serial(port_num,9600,timeout=1) as ser:
        flag=bytes('l')
        ser.write(flag)
        ser.close()
        
def left_speed_up():
    with serial.Serial(port_num,9600,timeout=1) as ser:
        flag=bytes('r')
        ser.write(flag)
        ser.close()