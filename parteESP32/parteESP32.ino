#include <iostream>
#include <string>

using namespace std;

#define pinPot1=15;

#define RXD2 16
#define TXD2 17

float pot1Value=0;



void recibirDato(int pot){
  
  
  }

void setup() {
  Serial.begin(115200);
  Serial.print("este es el setup");

  Serial2.begin(9600, SERIAL_8N1, RXD2, TXD2);
}



int i=0;
void loop() {
  if (Serial2.available() > 0) {
      String sms = Serial2.readStringUntil('\n');
      String label = sms.substring(0,5);
      float value= (sms.substring(5)).toFloat();
      
      if (label == "pot1"){
        
        }

      Serial.println(sms);
  }

  /*
  pot1Value = analogRead(pinPot1);
  Serial.print("pot1:");
  pot1Value=3.3*pot1Value/4095;
  Serial.println(pot1Value);
  */
  delay(500);
}
