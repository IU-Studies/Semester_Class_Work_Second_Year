int temperaturePin = 0; 
int fanPin = 12;

void setup() 
{ 
Serial.begin(9600); 
pinMode(fanPin, OUTPUT);
} 

void loop() 
{ 
float voltage, degreesC, degreesF; 
voltage = getVoltage(temperaturePin); 
degreesC = (voltage - 0.5) * 100.0; 
degreesF = degreesC * (9.0/5.0) + 32.0; 
  
Serial.print("voltage: "); 
Serial.print(voltage); 
Serial.print("  deg C: "); 
Serial.print(degreesC); 
Serial.print("  deg F: "); 
Serial.println(degreesF);
  
  if (degreesC>40){
    digitalWrite(fanPin, HIGH);
  }
  else{
    digitalWrite(fanPin, LOW);
  }
  
  
delay(1000); 
} 
float getVoltage(int pin) 
{ 
return (analogRead(pin) * 0.004882814); 
}
