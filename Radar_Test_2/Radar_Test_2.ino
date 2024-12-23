#include <Servo.h>
#include <Arduino.h>
#include <Ultrasonic.h>


#define VCC_sensor 11
#define motor 3

Ultrasonic ultrasonic(12, 13);
Servo myServo;
int pos = 0;

int sped_time = 20;
int angle = 180;

void setup() {
  Serial.begin(9600);
  myServo.attach(motor);
  myServo.write(90);
  pinMode(VCC_sensor, OUTPUT); digitalWrite(VCC_sensor, 1);
}

void loop() {
  static uint32_t tmr = 0;
  if (millis() - tmr > 100){ //Таймер на відправку даних з сенсора
    tmr = millis(); 
    Serial.print("1,");
    Serial.println(ultrasonic.distanceRead());
  }
}



