#include <string.h>

char buff[64];
char key[] = "nice";
void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0)
  {
    Serial.readStringUntil('\n').toCharArray(buff, 64);
    Serial.println(buff);
    if (strcmp(key, buff) ==0)
    {
      Serial.println("abaababababababab");
    }
  }
}
