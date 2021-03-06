from machine import Pin
from time import sleep_ms
import neopixel

def leds(loops=2):
    n = 300
    npx = neopixel.NeoPixel(Pin(2), n)
    color = {'red': (255,0,0), 'green': (0,255,0), 'blue':(0,0,255)}
    for i in range(loops):
        for ind, col in enumerate(color):
            for pix in range(0,160,5):
                npx[pix] = color[col]
                npx.write()
            for pix in range(0,160,5):
                npx[pix] = (0,0,0)
                npx.write()
    sleep_ms(1000)
leds()
