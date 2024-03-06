import RPi.GPIO as GPIO
from gpiozero import RGBLED, MCP3008, Button, LED, Buzzer
import time
from RPLCD import CharLCD

servo_pin = 17
pwm_freq = 50
pir_pin = 22

rgbled = RGBLED(red=5, green=6, blue=13)
pot = MCP3008(channel=0)
button = Button(27)
yellow_led = LED(26)
buzzer = Buzzer(19)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(pir_pin, GPIO.IN)

servo_pwm = GPIO.PWM(servo_pin, pwm_freq)
lcd = CharLCD(cols=16, rows=2, pin_rs=25, pin_e=24, pins_data=[23,18,15,14], numbering_mode=GPIO.BCM)

def set_angle(angle, sleep_time):
    duty_cycle = (angle / 180.0) * 10 + 2
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(sleep_time)

def motor_activate(sleep_time):
    set_angle(0, sleep_time)
    set_angle(90, sleep_time)
    set_angle(180, sleep_time)
    set_angle(90, sleep_time)

counter = 0
try:
    while True:
        servo_pwm.start(0)
        pir_state = GPIO.input(pir_pin)
        if pir_state:
            counter += 1
            yellow_led.on()
            buzzer.on()
            time.sleep(0.5)
            yellow_led.off()
            buzzer.off()
            
        if counter > 0:
            pot_val = pot.value
            if pot_val < 0.33:
                rgbled.color = (1, 0, 0)
                motor_activate(0.2)
                lcd.clear()
                lcd.cursor_pos = (0,0)
                lcd.write_string("MOTOR is ON")
                lcd.cursor_pos = (1,0)
                lcd.write_string("MOTOR MODE: FAST")
            
            elif 0.33 <= pot_val <= 0.66:
                rgbled.color = (0, 1, 0)
                motor_activate(0.4)
                lcd.clear()
                lcd.cursor_pos = (0,0)
                lcd.write_string("MOTOR is ON")
                lcd.cursor_pos = (1,0)
                lcd.write_string("MOTOR MODE: MID")
                
            elif pot_val > 0.66:
                rgbled.color = (0, 0, 1)
                motor_activate(0.8)
                lcd.clear()
                lcd.cursor_pos = (0,0)
                lcd.write_string("MOTOR is ON")
                lcd.cursor_pos = (1,0)
                lcd.write_string("MOTOR MODE: SLOW")
            
        if button.is_pressed:
            rgbled.color = (0,0,0)
            counter = 0
            servo_pwm.ChangeDutyCycle(0)
            lcd.clear()
            lcd.cursor_pos = (0,0)
            lcd.write_string("MOTOR is OFF")
            
except KeyboardInterrupt:
    rgbled.color = (0, 0, 0)
    servo_pwm.stop()
    lcd.clear()
    GPIO.cleanup()
