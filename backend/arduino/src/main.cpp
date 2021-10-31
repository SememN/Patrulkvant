#include <Arduino.h>
#include <t_and_h.h>
#include "mpu6050.h"
#include "photoresistor.h"
#include "motors.h"

String res ="";

void setup(){
  
  mpu6050_begin();
  motor_begin();

  Serial.begin(115200);
  delay(3000);              // выполняем задержку для перехода датчиков в активное состояние
  Serial.setTimeout(1000);
  
}

void loop(){
  
  //mpu6050();      //гироском-акселерометр
  //tem();      //температура-влажность
  //hum();
  //photoresisrot();      //освещенность
  
  if (Serial.available()>0){
    char key = Serial.read();
    int val = Serial.parseInt();
    switch (key) {
      case 'd':
        res = "d";
        // res += (String) mpu6050();
        // res += ",";
        res += (String) photoresisrot();
        res += ",";
        res += (String) tem();
        res += ",";
        res += (String) hum();
        res += ";";
        Serial.println(res);
        val = 0;
        break;
      case 'g':   //go прямая езда веперед
        go(-1, val);
        break;
      case 'b':   //back прямая езда назад
        go(1, val);
        break;
      case 't':   // -3.14 < turn < 3.14 разворот
        turn(val);
        key = 'a';
        break;
      case 's':
        go(0, 1);
        break;
      default:
        break;
    }
      
    
  }

}



