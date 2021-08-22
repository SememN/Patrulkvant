//for split func
#include <bits/stdc++.h>
using namespace std;

//GYROSCOPE
#include "I2Cdev.h"
#include "MPU6050_6Axis_MotionApps_V6_12.h"
#include "Wire.h"
MPU6050 mpu;

float angleX = 0;
float angleY = 0;
float angleZ = 0;
//GYROSCOPE

//SERVO
#include <Servo.h> // подключаем библиотеку для работы с сервоприводом
Servo servo1; // объявляем переменную servo типа "servo1"
//SERVO

//GPS
#include <SoftwareSerial.h>
SoftwareSerial mySerial(8, 7);
//GPS

void setup() {
  //GYROSCOPE
  Wire.begin();
  Wire.setClock(400000ul);
  Serial.begin(9600);
  mpu.initialize();
  initDMP();
  const float toDeg = 180.0 / M_PI;
  uint8_t mpuIntStatus; // holds actual interrupt status byte from MPU
  uint8_t devStatus; // return status after each device operation (0 = success, !0 = error)
  uint16_t packetSize; // expected DMP packet size (default is 42 bytes)
  uint16_t fifoCount; // count of all bytes currently in FIFO
  uint8_t fifoBuffer[64]; // FIFO storage buffer
  Quaternion q; // [w, x, y, z] quaternion container
  VectorFloat gravity; // [x, y, z] gravity vector
  float ypr[3]; // [yaw, pitch, roll] yaw/pitch/roll container and gravity vector
  //GYROSCOPE

  //SERVO
  servo1.attach(4); // привязываем сервопривод к аналоговому выходу 11
  //SERVO

  //GPS
  while (!Serial); // wait for Serial to be ready
  Serial.begin(9600); 
  mySerial.begin(9600);
  //GPS

  //MOTOR
  pinMode(12,OUTPUT); //this is superMotor 12 pin
  //MOTOR
}

void loop() {
  String command = Serial.read();
  if (command){
    String sensor = getValue(command, '$', 0);
    //GYROSCOPE
    if (sensor == "gyroscope"){
      Serial.end();
      Serial.begin(9600);
      mainGyro();
      delay(2000);
      Serial.end();
    }
    //GYROSCOPE
    
    //SERVO
      if (sensor == "servo"){
      Serial.end();
      Serial.begin(9600);
      mainServo(command);
      delay(2000);
      Serial.end();
      }
    //SERVO

    //GPS
    if (sensor == "gps"){
      mySerial.end();
      mySerial.begin(9600);
      delay(10000);
      mySerial.end();
    }
    //GPS

    //MOTOR
    if (sensor == "motor"){
      if (getValue(command, '$', 2) == '2'){
        digitalWrite(12, 1);
      }
      if (getValue(command, '$', 2) == '32'){
        digitalWrite(12, 0);
      }
    }
    //MOTOR
  }
}

//GYROSCOPE
void mainGyro(){
  getAngles();
  Serial.println(angleZ);
  delay(2000);

void initDMP() {
  devStatus = mpu.dmpInitialize();
  mpu.setDMPEnabled(true);
  mpuIntStatus = mpu.getIntStatus();
  packetSize = mpu.dmpGetFIFOPacketSize();
}

void getAngles() {
  if (mpu.dmpGetCurrentFIFOPacket(fifoBuffer)) {
    mpu.dmpGetQuaternion(&q, fifoBuffer);
    mpu.dmpGetGravity(&gravity, &q);
    mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
    angleX = ypr[2] * toDeg;
    angleY = ypr[1] * toDeg;
    angleZ = ypr[0] * toDeg;
  }
}
//GYROSCOPE

//SERVO
String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void mainServo(String command){
    int degrees = (getValue(command, '$', 1).toInt();
    servo1.write(degrees);
}
//SERVO
