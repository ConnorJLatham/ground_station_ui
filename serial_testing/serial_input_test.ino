String incoming;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
//  incoming = Serial.readString();
  
  if (Serial.available() == 0)
  {
    Serial.print("I hear ya! This is what I heard: ");
    Serial.println(Serial.readStringUntil("\n"));
  }
}
