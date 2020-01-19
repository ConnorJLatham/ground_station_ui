void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.print(Serial.available());
  delay(500);
  if (Serial.available() > 3)
  {
    Serial.print(Serial.readStringUntil('\n'));
  }
  Serial.println();
}
