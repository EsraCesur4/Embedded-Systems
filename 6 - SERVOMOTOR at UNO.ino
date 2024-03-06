#include <LiquidCrystal.h>
#include <Servo.h>

int PIR_PIN = 8;
int SERVO_PIN = 9;
int POT_PIN = A0;
int RED = 10;
int GREEN = 11;
int BLUE = 12;
int BUTTON_PIN = 13;
int BUZZER_PIN = 16;
int LED_PIN = 15;

Servo myServo;
LiquidCrystal lcd(2, 3, 4, 5, 6, 7);

void setup() {
  // put your setup code here, to run once:
  pinMode(PIR_PIN, INPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);

  myServo.attach(SERVO_PIN);
  lcd.begin(16,2);
}

void motorActivate(int sleeptime) {
  myServo.write(0);
  delay(sleeptime);
  myServo.write(90);
  delay(sleeptime);
  myServo.write(180);
  delay(sleeptime);
  myServo.write(90);
  delay(sleeptime);
}

int counter = 0;
void loop() {
  // put your main code here, to run repeatedly:
  
  int pir_state = digitalRead(PIR_PIN);

  if (pir_state) {
    counter++;
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, HIGH);
    delay(500);
    digitalWrite(LED_PIN, LOW);
    digitalWrite(BUZZER_PIN, LOW);
  }

  if (counter > 0) {
    int pot = analogRead(POT_PIN);
    float pot_val = map(pot, 0, 1023, 0, 1000);

    if (pot_val < 330) {
      digitalWrite(RED, HIGH);
      digitalWrite(GREEN, LOW);
      digitalWrite(BLUE, LOW);
      motorActivate(200);
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("MOTOR is ON");
      lcd.setCursor(0,1);
      lcd.print("MOTOR MODE: FAST");
      
    } else if (pot_val >= 330 && pot_val < 660) {
      digitalWrite(RED, LOW);
      digitalWrite(GREEN, HIGH);
      digitalWrite(BLUE, LOW);
      motorActivate(400);
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("MOTOR is ON");
      lcd.setCursor(0,1);
      lcd.print("MOTOR MODE: MID");
      
    } else if (pot_val >= 660) {
      digitalWrite(RED, LOW);
      digitalWrite(GREEN, LOW);
      digitalWrite(BLUE, HIGH);
      motorActivate(800);
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("MOTOR is ON");
      lcd.setCursor(0,1);
      lcd.print("MOTOR MODE: SLOW");
    }
  }

  int button_state = digitalRead(BUTTON_PIN);
  if (button_state == LOW) {
    counter = 0;
    digitalWrite(RED, LOW);
    digitalWrite(GREEN, LOW);
    digitalWrite(BLUE, LOW);
    myServo.write(0);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("MOTOR is OFF");
  }
}
