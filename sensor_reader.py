import board
import busio
import asyncio
from bmo055 import BMO055 as bmo
from lm75 import LM75

        
class DataReader:
    def __init__(self):
        self.i2c = busio.I2C(board.GP27, board.GP26)
        self.thermometer = LM75(self.i2c)
        self.imu = bmo(self.i2c)
        
    def read_data(self):
        print(self.thermometer.temperature())
    
    async def run_reading(self):
        while True:
            self.read_data()
            await asyncio.sleep(1)