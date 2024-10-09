int sensorState = 0;
int buzzer = 12;
int sensorPin = 2; 
int led = 13; 

void setup() {
  pinMode(sensorPin, INPUT);
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  sensorState = digitalRead(sensorPin);

  if (sensorState == HIGH) {
    digitalWrite(led, HIGH);
    digitalWrite(buzzer, HIGH);

  } else {
    digitalWrite(led, LOW);
    digitalWrite(buzzer, LOW);
  }
  delay(10); 
}
