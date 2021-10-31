#include <TroykaLight.h>
TroykaLight sensorLight(A14);

float photoresisrot()    {
    // считывание данных с датчика освещённости
    sensorLight.read();
    // вывод показателей сенсора освещённости в люксахи
    //Serial.println(sensorLight.getLightLux());
    //delay(300);
    return(sensorLight.getLightLux());
}