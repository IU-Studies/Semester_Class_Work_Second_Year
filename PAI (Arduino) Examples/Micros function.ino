void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  unsigned long startTime = micros();

  digitalWrite(LED_BUILTIN, HIGH);

  while (micros() - startTime < 1000) {}

  digitalWrite(LED_BUILTIN, LOW);

  delayMicroseconds(1000);
}
