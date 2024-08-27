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
        self.acceleration = [1.2, 3.4, 5.6]
        self.rotation = [7.8, 9.0, 12.3]
        self.magnetic = [4.56, 7.89, 0.12]

    def read_temperature(self):
        try:
            self.temperature = self.thermometer.get_temperature()
        except OSError:
            print("read error")

    async def reading_task(self):
        while True:
            self.read_temperature()
            await asyncio.sleep(1)
