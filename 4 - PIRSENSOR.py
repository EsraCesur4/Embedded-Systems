from gpiozero import MotionSensor, Buzzer, LED
import time

pir = MotionSensor(17)
buzzer = Buzzer(27)
red_led = LED(22)
green_led = LED(10)

while True:
    if pir.motion_detected:
        buzzer.on()
        green_led.on()
        red_led.off()
        time.sleep(1)
        
    else:
        buzzer.off()
        green_led.off()
        red_led.on()
        time.sleep(1)
