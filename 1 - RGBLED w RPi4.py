from gpiozero import RGBLED,MCP3008
import time

led = RGBLED(red=17, green=27, blue=22)
pot = MCP3008(channel=0)

while True:
    pot_val = pot.value
    print(pot_val)
    if pot_val < 0.33:
        led.color = (1,0,0)
    if 0.33 <= pot_val <= 0.66:
        led.color = (0,1,0)
    if pot_val > 0.66:
        led.color = (0,0,1)
    
    time.sleep(0.1)
