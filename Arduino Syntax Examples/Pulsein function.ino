void setup() {
  Serial.begin(9600);
  pinMode(7, INPUT);
}

void loop() {
  long duration = pulseIn(7, HIGH);

  Serial.print("Duration of HIGH pulse on pin 7: ");
  Serial.print(duration);
  Serial.println(" microseconds");

  delay(1000); 
}
