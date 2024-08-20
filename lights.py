import asyncio
import board
import neopixel

WHITE = 0xffffff
BLACK = 0x000000
RED = 0xff0000
GREEN = 0x00ff00
BLUE = 0x0000ff

class Lights:
    def __init__(self):
        self.pixel = neopixel.NeoPixel(board.GP10, 3, brightness=0.2, pixel_order=neopixel.RGB)
        
    def light_up(self):
        self.pixel.fill(WHITE)
        
    def light_down(self):
        self.pixel.fill(BLACK)
        
    def light_rgb(self):
        self.pixel[0] = RED
        self.pixel[1] = GREEN
        self.pixel[2] = BLUE

    async def blink(self):
        while True:
            self.light_up()
            await asyncio.sleep(2)
            self.light_rgb()
            await asyncio.sleep(2)
            self.light_down()
            await asyncio.sleep(2)
