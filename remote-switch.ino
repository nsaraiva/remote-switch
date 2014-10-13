/*
Analysing the data from serial connection

created 2014-07-15
autor Nelson Saraiva
version 0.1

This code is in the public domain.
*/
 
char command;
void setup() {
  // Open serial communications:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  Serial.println("ready");
}

void loop() {
  // if data present, blink
  if (Serial.available() > 0) {
    command = Serial.read();
    if (isDigit(command)){
      digitalWrite(13,HIGH);
    }else{
      digitalWrite(13,LOW);
    }
    Serial.println(command);
    if (command.substring(0,2) == "on") {
      Serial.println("ligado");
      digitalWrite(13, HIGH);
    }else{
      Serial.println("desligado");      
      digitalWrite(13, LOW);
    }
    */
  }
}

