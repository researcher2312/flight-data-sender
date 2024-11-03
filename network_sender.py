import wifi
import time
import asyncio
import socketpool
from array import array


class SocketManager:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        self.pool = socketpool.SocketPool(wifi.radio)
        self.socket = None
        self.address = None

    def create_socket(self):
        self.socket = self.pool.socket(self.pool.AF_INET, self.pool.SOCK_DGRAM)
        self.address = (str(self.connection_manager.device_address), 1234)
        try:
            self.socket.connect(self.address)
        except:
            self.address = None
            print("connection error")
        self.socket.settimeout(5)

    def send_data(self, sensor):
        data = array("f", sensor.get_all_readings())
        try:
            self.socket.send(data)
        except BrokenPipeError:
            print("send error")
        else:
            print("transmission finished")

    async def send_task(self, sensor):
        while True:
            if self.connection_manager.device_connected:
                if self.address == None:
                    self.create_socket()
                else:
                    self.send_data(sensor)
                
            await asyncio.sleep(0.02)


class ConnectionManager:
    def __init__(self):
        self.device_connected = False
        self.device_address = None
        self.connection_missing_counter = 0
        wifi.radio.start_ap(ssid="Astronaut", password="12345678")

    def get_connected_ip(self):
        stations = wifi.radio.stations_ap
        if len(stations) == 1:
            self.device_connected = True
            self.device_address = stations[0].ipv4_address
            self.connection_missing_counter = 0
        elif len(stations) > 1:
            self.device_connected = False
            print("too much connections")
        else:
            self.connection_missing_counter += 1
            
        if self.connection_missing_counter > 10:
            self.device_connected = False

    async def monitor_connections_task(self):
        while True:
            self.get_connected_ip()
            print(self.device_address)
            await asyncio.sleep(2)
