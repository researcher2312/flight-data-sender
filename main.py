import asio
from sensor_reader import DataReader
from network_sender import ConnectionManager, SocketManager
from lights import Lights


async def main():
    connection_manager = ConnectionManager()
    socket_manager = SocketManager(connection_manager)
    lights = Lights()
    monitor_task = asyncio.create_task(connection_manager.monitor_connections())
    sender_task = asyncio.create_task(socket_manager.send_data())
    lights.light_up()
    await asyncio.gather(monitor_task)


asyncio.run(main())
