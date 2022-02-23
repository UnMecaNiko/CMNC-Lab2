const int pinPot1=15;

int pot1Value=0;

void setup() {
  Serial.begin(115200);
  Serial.print("este es el setup");
  
}
int i=0;
void loop() {
  pot1Value = analogRead(pinPot1);
  Serial.print("pot1:");
  Serial.println(pot1Value);
  
  delay(500);
}
