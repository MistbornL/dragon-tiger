import socketio

static_files = {
    '/': './public',
}
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=[])
s_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    print('connect ', sid)
    await sio.emit("message", {"message": "asd"})


@sio.event
async def connect_error(sid, data):
    print("The connection failed!", data)


@sio.event
async def disconnect(sid):
    print("I'm disconnected!")


@sio.event
async def send_message(sid, data):
    print("movida")
