#include <Arduino.h>
#include <GParser.h>
#include <Ultrasonic.h>
#include <Servo.h>

#define LASER A0
#define LED1 5
#define GND_led 4
#define POT A1
#define VCC_sensor 11


Servo servo1;
Ultrasonic ultrasonic(12, 13);

void setup() {
  pinMode(GND_led, OUTPUT); digitalWrite(GND_led, 0);
  pinMode(LED1, OUTPUT); 
  pinMode(LASER, OUTPUT);
  pinMode(VCC_sensor, OUTPUT); digitalWrite(VCC_sensor, 1);

  servo1.attach(3); //Пин для серво
  servo1.write(100);

  Serial.begin(9600);
}

void loop() {
  // //З ПК на Arduino
  // 0 - Servo
  // 1 - Laser
  // 2 - LED1

// // Парсер // //
  if (Serial.available()) {
    char buf[50];
    Serial.readBytesUntil(";", buf, 50);
    GParser data(buf, ",");
    int ints[10];
    data.parseInts(ints);
    
    switch (ints[0]){
      case 0: servo1.write(ints[1]);
        break;
      case 1: digitalWrite(LASER, ints[1]); Serial.print(ints[1]);
        break;
      case 2: digitalWrite(LED1, ints[1]);
        break;
    }

  }
  // servo1.write(90);
  // digitalWrite(LASER, 1);
  // digitalWrite(LED1, 1);





// //-------------//
// // //З Arduino
// // 0 - Ultrasonic
  // static uint32_t tmr = 0;
  // if (millis() - tmr > 100){ tmr = millis(); //Таймер на відправку даних з сенсора
  //   // Serial.print(0);
  //   // Serial.print(",");
  //   Serial.println(ultrasonic.distanceRead());
  // }





}

