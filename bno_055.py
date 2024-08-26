import time
import adafruit_bno055

IMU_ADDRESS = 0x29

CONFIG_MODE = 0x00
ACCONLY_MODE = 0x01
MAGONLY_MODE = 0x02
GYRONLY_MODE = 0x03
ACCMAG_MODE = 0x04
ACCGYRO_MODE = 0x05
MAGGYRO_MODE = 0x06
AMG_MODE = 0x07
IMUPLUS_MODE = 0x08
COMPASS_MODE = 0x09
M4G_MODE = 0x0A
NDOF_FMC_OFF_MODE = 0x0B
NDOF_MODE = 0x0C

class BNO055:
    def __init__(self, i2c):
        self.sensor = adafruit_bno055.BNO055_I2C(i2c, IMU_ADDRESS)
        self.offset_magnetometer = 0
        self.offset_accelerometer = 0
        self.offset_gyroscope = 0

    def calibrate_magnetometer(self):
        print("Magnetometer: Perform the figure-eight calibration dance.")
        while not self.sensor.calibration_status[3] == 3:
            print(f"Mag Calib Status: {100 / 3 * self.sensor.calibration_status[3]:3.0f}%")
            time.sleep(1)
        print("... CALIBRATED")
        time.sleep(1)

    def calibrate_accelerometer(self):
        print("Accelerometer: Perform the six-step calibration dance.")
        while not self.sensor.calibration_status[2] == 3:
            # Calibration Dance Step Two: Accelerometer
            #   Place sensor board into six stable positions for a few seconds each:
            #    1) x-axis right, y-axis up,    z-axis away
            #    2) x-axis up,    y-axis left,  z-axis away
            #    3) x-axis left,  y-axis down,  z-axis away
            #    4) x-axis down,  y-axis right, z-axis away
            #    5) x-axis left,  y-axis right, z-axis up
            #    6) x-axis right, y-axis left,  z-axis down
            #   Repeat the steps until calibrated
            print(f"Accel Calib Status: {100 / 3 * self.sensor.calibration_status[2]:3.0f}%")
            time.sleep(1)
        print("... CALIBRATED")
        time.sleep(1)

    def calibrate_gyroscope(self):
        print("Gyroscope: Perform the hold-in-place calibration dance.")
        while not self.sensor.calibration_status[1] == 3:
            # Calibration Dance Step Three: Gyroscope
            #  Place sensor in any stable position for a few seconds
            #  (Accelerometer calibration may also calibrate the gyro)
            print(f"Gyro Calib Status: {100 / 3 * self.sensor.calibration_status[1]:3.0f}%")
            time.sleep(1)
        print("... CALIBRATED")
        time.sleep(1)

    def calibrate(self):
        self.calibrate_magnetometer()
        self.calibrate_accelerometer()
        self.calibrate_gyroscope()
        self.offset_magnetometer = sensor.offsets_magnetometer
        self.offset_accelerometer = sensor.offsets_accelerometer
        self.offset_gyroscope = sensor.offsets_gyroscope
