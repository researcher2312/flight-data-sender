import board
import busio
import asyncio
from bno_055 import BNO055
from lm75 import LM75


class DataReader:
    def __init__(self):
        self.i2c = busio.I2C(board.GP27, board.GP26)
        self.thermometer = LM75(self.i2c)
        self.imu = BNO055(self.i2c)
        self.temperature = 0

    def read_data(self):
        try:
            self.temperature = self.thermometer.get_temperature()
        except OSError:
            print("read error")

    async def run_reading(self):
        while True:
            self.read_data()
            print(self.temperature)
            await asyncio.sleep(1)
