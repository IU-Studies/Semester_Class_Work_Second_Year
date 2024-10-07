void setup() {
  Serial.begin(9600);
  pinMode(8, INPUT);
}

void loop() {
  long duration = pulseInLong(8, LOW);

  Serial.print("Duration of LOW pulse on pin 8: ");
  Serial.print(duration);
  Serial.println(" microseconds");

  delay(1000);
}
