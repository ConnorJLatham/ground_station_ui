int incoming_byte = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
    incoming_byte = Serial.read();
    Serial.print("Here we go: I like focex and trains and planes arnd cars too");
    Serial.println(incoming_byte);
    delay(75);
  }
