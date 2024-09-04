import board
import busio
import asyncio
import adafruit_icm20x
#from bno_055 import BNO055
from lm75 import LM75


class DataReader:
    def __init__(self):
        self.i2c = busio.I2C(board.GP27, board.GP26)
        self.thermometer = LM75(self.i2c)
        #self.imu = BNO055(self.i2c)
        self.imu = adafruit_icm20x.ICM20948(self.i2c)
        self.temperature = 0.0
        self.acceleration = []
        self.rotation = []
        self.magnetic = []

    def read_temperature(self):
        try:
            self.temperature = self.thermometer.get_temperature()
        except OSError:
            print("temperature read error")

    def read_imu(self):
        try:
            self.acceleration = self.imu.acceleration
            self.rotation = self.imu.gyro
            self.magnetic = self.imu.magnetic
        except OSError:
            print("imu read error")

    def get_all_readings(self):
        return [self.temperature, *self.acceleration, *self.rotation, *self.magnetic]

    async def reading_task(self):
        while True:
            self.read_temperature()
            self.read_imu()
            await asyncio.sleep(1)
