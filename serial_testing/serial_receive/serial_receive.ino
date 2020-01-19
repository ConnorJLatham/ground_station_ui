void setup() {
  Serial.begin(115200);
}

void loop() {
  float arr[10] = {1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10};
  for (int i = 0; i < 10; i++)
  {
    Serial.print(arr[i]);
  }
  Serial.print('\n');
  delay(10);
}
