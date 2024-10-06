int buttonState = 2;  

void setup() {
  Serial.begin(9600);
}

void loop() {
  switch (buttonState) {
    case 0:
      Serial.println("Button is not pressed");
      break;
    case 1:
      Serial.println("Button is pressed");
      break;
    case 2:
      Serial.println("Button is in an unknown state");
      break;
    default:
      Serial.println("Invalid state");
      break;
  }

  buttonState = (buttonState + 1) % 4; 
  delay(1000);  
}
