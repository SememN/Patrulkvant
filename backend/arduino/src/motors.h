int motor[4][2] = {{44,45},{46,47},{48,49},{50,51}}; //motor 1,2,3,4; [dir], [enable];
float val1;

void motor_begin(){
    for (int i=0;i<4;i++)
        for (int j=0;j<2;j++)
            pinMode(motor[i][j], OUTPUT);
}

void go (bool dir, int enable){
    if (enable == 1){
        digitalWrite(motor[0][1], 1);
        digitalWrite(motor[1][1], 1);
        digitalWrite(motor[2][1], 1);
        digitalWrite(motor[3][1], 1);
    }
    else{
        digitalWrite(motor[0][1], 0);
        digitalWrite(motor[1][1], 0);
        digitalWrite(motor[2][1], 0);
        digitalWrite(motor[3][1], 0);
        if(dir == 1){
            digitalWrite(motor[0][1], 1);
            digitalWrite(motor[1][1], 1);
            digitalWrite(motor[2][1], 1);
            digitalWrite(motor[3][1], 1);
        }
        if(dir == 0){
            digitalWrite(motor[0][1], 0);
            digitalWrite(motor[1][1], 0);
            digitalWrite(motor[2][1], 0);
            digitalWrite(motor[3][1], 0);
        }
    }

}


void turn (float rad){
    
    mpu.initialize();
    mpu.dmpInitialize();
    mpu.setDMPEnabled(true);
    digitalWrite(motor[0][1], 0);       //выключаем enable
    digitalWrite(motor[1][1], 0);
    digitalWrite(motor[2][1], 0);
    digitalWrite(motor[3][1], 0);
    Serial.println("hello");
    Serial.println(mpu6050());
    if (rad >= 0 and rad <=3.14){
        digitalWrite(motor[0][1], 1);   //включаем поворот двигателей по часовой стрелки
        digitalWrite(motor[1][1], 1);
        digitalWrite(motor[2][1], 1);
        digitalWrite(motor[3][1], 1);
        val1 = 0;
        while (val1<rad){
            val1 = mpu6050();
        }
        digitalWrite(motor[0][1], 0);   //выключаем двигатели
        digitalWrite(motor[1][1], 0);
        digitalWrite(motor[2][1], 0);
        digitalWrite(motor[3][1], 0);
        Serial.println("hello2");
    }
    if (rad < 0 and rad >= -3.14){
        digitalWrite(motor[0][1], 1);   //включаем поворот двигателей против часовой стрелки
        digitalWrite(motor[1][1], 1);
        digitalWrite(motor[2][1], 1);
        digitalWrite(motor[3][1], 1);
        val1 = 0;
        while (val1>rad){
            val1 = mpu6050();
        }
        digitalWrite(motor[0][1], 0);   //выключаем двигатели
        digitalWrite(motor[1][1], 0);
        digitalWrite(motor[2][1], 0);
        digitalWrite(motor[3][1], 0);
        Serial.println("hello3");
        // Serial.println(mpu6050());
    }
}