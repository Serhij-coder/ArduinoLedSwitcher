int inChar;
boll conection_test = 1;
#define LED_PIN 52

void setup() {
  pinMode(LED_PIN, OUTPUT); // Инициализация светодиода
  Serial.begin(9600); // Инициализация Serial - порта
}

void loop() {
  static bool flag;
  if (Serial.available() > 0)
  {
    inChar = Serial.read();
    if (inChar == 't')Serial.println(conection_test);
    if (inChar == 'e') // e - Enable - включить
    {
      digitalWrite(LED_PIN, HIGH);
    }
  }

  else if (inChar == 'd') // d - Disable - выключить
  {
    digitalWrite(LED_PIN, LOW);
  }
  else if (inChar == 'b') // b - Blink - выключить режим мигания
  {
    flag += 1;
    while (flag == 1) {
      digitalWrite(LED_PIN, HIGH);
      delay(100);
      digitalWrite(LED_PIN, LOW);
      delay(100);
      inChar = Serial.read();
      if (Serial.available() > 0)
      {
        if (inChar != 'b') // b - Blink - выключить режим мигания
        {
          flag -= 1;
        }
      }
    }
  }
}
