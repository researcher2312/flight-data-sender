from adafruit_bus_device.i2c_device import I2CDevice

class LM75:
    ADDRESS = 0x48
    def __init__(self, i2c):
        self._device = I2CDevice(i2c,address)
        
    def _twos_comp(self, val, bits):
        if (val & (1 << (bits - 1))):
            val = val - (1 << bits)
        return val

    def _get_temp_bytes(self):
        buf = bytearray(2)
        with self._device:
            self._device.readinto(buf)
        return buf

    def temperature(self):
        [t_high,t_low] = self._get_temp_bytes()
        fraction = 0.5*(t_low >> 7)
        return self._twos_comp(t_high,8) + fraction