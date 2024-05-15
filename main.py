import asio
from sensor_reader import DataReader
from network_sender import ConnectionManager, SocketManager


async def main():
    connection_manager = ConnectionManager()
    socket_manager = SocketManager(connection_manager)
    monitor_task = asyncio.create_task(connection_manager.monitor_connections())
    sender_task = asyncio.create_task(socket_manager.send_data())
    await asyncio.gather(monitor_task)


asyncio.run(main())
