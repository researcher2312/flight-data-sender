import board
import busio
import asyncio

class Sensor:
    def __init__(self, scl, sda):
        self.i2c = busio.I2C(pin_data.scl, pin_data.sda)
        
class DataReader:
    def __init__(self):
        self.thermometer = Sensor(x, x)
        
    async def read_data(self):
        pass
    
    async def run_reading(self):
        while True:
            self.read_data()
            await asyncio.sleep(1)