#include <iarduino_DHT.h>   // подключаем библиотеку для работы с датчиком DHT
iarduino_DHT sensor(52);     // объявляем  переменную для работы с датчиком DHT, указывая номер цифрового вывода к которому подключён датчик (сейчас 2pin)

float hum(){
  switch(sensor.read()){    // читаем показания датчика
    case DHT_OK:               
      return(sensor.hum);  
      break;
    
  }    
}
float tem(){     
      return (sensor.tem); 
}