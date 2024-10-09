const int ledPin = 13;  

void setup() {
  pinMode(ledPin, OUTPUT);  

  for (int i = 0; i < 10; i++) {
    if (i == 5) {
      continue;  
    }
    digitalWrite(ledPin, HIGH);  
    delay(500);                   
    digitalWrite(ledPin, LOW);   
    delay(500);                   
  }
}

void loop() {}
