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
  pinMode(VCC_sensor, OUTPUT); digitalWrite(VCC_sensor, 1);
}

void loop() {
  for (pos = 1; pos <= angle; pos++){
    Serial.print(pos);
    Serial.print(",");
    Serial.println(ultrasonic.distanceRead());

    myServo.write(pos);
    delay(sped_time);
  }
  delay(sped_time/2);

  for (pos = angle-1; pos >= 0; pos--){
    Serial.print(pos);
    Serial.print(",");
    Serial.println(ultrasonic.distanceRead());

    myServo.write(pos);
    delay(sped_time);
  }
  delay(sped_time/2);
}




