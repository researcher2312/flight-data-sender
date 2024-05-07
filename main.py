from network_sender import connection_manager, socket_manager
import asio


async def main():
    connection_manager = ConnectionManager()
    socket_manager = SocketManager(connection_manager)
    monitor_task = asyncio.create_task(connection_manager.monitor_connections())
    sender_task = asyncio.create_task(socket_manager.send_data())
    await asyncio.gather(monitor_task)


asyncio.run(main())
