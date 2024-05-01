import wifi
import time
import asyncio
import socketpool



class SocketManager:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        self.pool = socketpool.SocketPool(wifi.radio)
        self.socket = None
        self.socket_initialised = False

    def create_socket(self):
        self.socket = self.pool.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.device_address, 23))

    async def send_data(self):
        if self.connection_manager.device_connected:
            if not self.socket_initialised:
                pass
            else:
                pass
        await asyncio.sleep(10)

class ConnectionManager:
    def __init__(self):
        self.device_connected = False
        self.device_address = None
        wifi.radio.start_ap(ssid="Astronaut", password="12345678")
        wifi.radio.start_dhcp_ap()

    def get_connected_ip(self):
        stations = wifi.radio.stations_ap
        if len(stations) == 0:
            self.device_connected = False
        elif len(stations) == 1:
            self.device_connected = True
            self.device_address = stations[0].ipv4_address
        else:
            self.device_connected = False

    async def monitor_connections(self):
        while True:
            self.get_connected_ip()
            print(self.device_connected)
            await asyncio.sleep(1)

async def main():
    print("test")
    connection_manager = ConnectionManager()
    socket_manager = SocketManager(connection_manager)
    asyncio.create_task(connection_manager.monitor_connections())
    asyncio.create_task(socket_manager.send_data())

asyncio.run(main())
