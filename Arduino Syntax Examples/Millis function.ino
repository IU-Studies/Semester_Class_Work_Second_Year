void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  unsigned long startTime = millis(); 

  digitalWrite(LED_BUILTIN, HIGH);

  while (millis() - startTime < 1000) {}

  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000); 
}
