import board
import neopixel

WHITE = 0xffffff
BLACK = 0x000000

class Lights:
    def __init__(self):
        self.pixel = neopixel.NeoPixel(board.GP10, 3, pixel_order=neopixel.RGB)
        
    def light_up(self):
        self.pixel.fill(WHITE)
        
    def light_down(self):
        self.pixel.fill(BLACK)
    