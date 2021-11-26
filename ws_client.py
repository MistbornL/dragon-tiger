import asyncio
import socketio


sio = socketio.AsyncClient()
game_id = "61a0d8deb9ff41b57231fda0"


game_round_id = None


@sio.event
async def on_connect_data(data):
    global game_round_id
    game_round_id = data.get('game_round_id')
    print(data)
    print("I'm connected!")


@sio.event
async def connect():
    await sio.emit("scan_card", {'card': "2c", "game_round_id": game_round_id})
    print("qweqwe")


async def main():
    await sio.connect(f'http://localhost:8000/?game_id={game_id}',
                      socketio_path='/ws/socket.io')
    await sio.wait()

asyncio.run(main())
