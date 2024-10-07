void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  
  delayMicroseconds(500);           
  digitalWrite(LED_BUILTIN, LOW);   
  delayMicroseconds(500);           
}
