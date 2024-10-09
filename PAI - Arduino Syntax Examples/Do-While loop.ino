int counter = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  do {
    Serial.println(counter);  
    counter++;                
    delay(500);              
  } while (counter < 5);      

  while (true) {
  }
}
