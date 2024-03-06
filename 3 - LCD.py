from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

rs = 17
e = 27
d_pins = [22, 23, 24, 25]

led_pin = 16
GPIO.setup(led_pin, GPIO.OUT)

lcd = CharLCD(cols=16, rows=2, pin_rs=rs, pin_e=e, pins_data=d_pins, numbering_mode=GPIO.BCM)
lcd.clear()

while True:
    lcd.cursor_pos = (0,0)
    lcd.write_string("Esra Cesur")
        
    GPIO.output(led_pin, GPIO.LOW)
    lcd.cursor_pos = (1,0)
    lcd.write_string("LED is OFF")
        
    time.sleep(5)
    lcd.clear()
        
    lcd.cursor_pos = (0,0)
    lcd.write_string("Esra Cesur")

    GPIO.output(led_pin, GPIO.HIGH)
    lcd.cursor_pos = (1,0)
    lcd.write_string("LED is ON")
        
    time.sleep(5)
    lcd.clear()
    