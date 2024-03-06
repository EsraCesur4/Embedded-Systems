import RPi.GPIO as GPIO
import time

segments = [17, 27, 19, 13, 6, 10, 22, 26]
button1 = 9
button2 = 11

GPIO.setmode(GPIO.BCM)

for pin in segments:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

digits = {
    0:[1,1,1,1,1,1,0,0],
    1:[0,1,1,0,0,0,0,0],
    2:[1,1,0,1,1,0,1,0],
    3:[1,1,1,1,0,0,1,0],
    4:[0,1,1,0,0,1,1,0],
    5:[1,0,1,1,0,1,1,0],
    6:[0,0,1,1,1,1,1,0],
    7:[1,1,1,0,0,0,0,0],
    8:[1,1,1,1,1,1,1,0],
    9:[1,1,1,1,0,1,1,0]
}

def digit_display(digit):
    for i in range(len(segments)):
        GPIO.output(segments[i], digits[digit][i])
        print(digit)
        
while True:
    if GPIO.input(button1) == GPIO.LOW:
        count = 9
        digit_display(count)
        while GPIO.input(button1) == GPIO.LOW:
            time.sleep(1)
            count -= 1
            if count < 0:
                count = 9
            digit_display(count)
            
    elif GPIO.input(button2) == GPIO.LOW:
        count = 0
        digit_display(count)
        while GPIO.input(button2) == GPIO.LOW:
            time.sleep(1)
            count += 1
            if count > 9:
                count = 0
            digit_display(count)
