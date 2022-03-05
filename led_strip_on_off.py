from machine import reset, Pin
from time import sleep, sleep_ms
import neopixel, led_on_off


def leds(loops=2):
    n = 300
    np = neopixel.NeoPixel(Pin(2), n)
    color = {'red': (255,0,0), 'green': (0,255,0), 'blue':(0,0,255)}
    
    for i in range(loops):
        for ind, col in enumerate(color):
            for pix in range(0,160,5):
                np[pix] = color[col]
                np.write()
            for pix in range(0,160,5):
                np[pix] = (0,0,0)
                np.write()
    sleep_ms(1000)