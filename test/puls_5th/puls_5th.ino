#include <TimerOne.h>
int main_flg = 0;
bool flg_13 =false;
bool flg_12 =false;
long hz = 1000;
long us = 1000;

void choice_pin(){
    if (main_flg == 1){
        switch_puls_13();
    }
    else if (main_flg == -1){
        switch_puls_12();
    }
    else{
        puls_stop();
    }
}

void setup() {
  // put your setup code here, to run once:
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  Serial.begin(9600);
  Timer1.initialize(100); 
  Timer1.attachInterrupt(choice_pin);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    int inputchar = Serial.read();
    switch(inputchar){
      case 'j':
        Serial.println("open");
        main_flg = 1;
      break;
      case 'k':
        Serial.println("close");
        main_flg = -1;
      break;
      case 'h':
        Serial.println("speed down");
        hz = hz - 100;
        us = 1000000/hz;
      break;
      case 'l':
        Serial.println("speed up");
         hz = hz + 100;
         us = 1000000/hz;
      break;
      case 's':
        Serial.println("stop");
        main_flg = 0;
      break;
    }
  }
}


void switch_puls_13(){
    digitalWrite(12, LOW);
    //Serial.println("open move");
    if(flg_13 ==true){
        digitalWrite(13, HIGH);
        flg_13 =false;
    }
    else{
        digitalWrite(13, LOW);
        flg_13 =true;
    }
    Timer1.setPeriod(us);
}

void switch_puls_12(){
    digitalWrite(13, LOW);
    //Serial.println("close move");
    if(flg_12 ==true){
        digitalWrite(12, HIGH);
        flg_12 =false;
    }
    else{
        digitalWrite(12, LOW);
        flg_12 =true;
    }
    Timer1.setPeriod(us);
}

void puls_stop(){
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
}
