import socketio

static_files = {
    '/': './public',
}
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*", static_files=static_files)
app = socketio.ASGIApp(sio)


@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)


@sio.event
async def connect_error(sid, data):
    print("The connection failed!", data)


@sio.event
async def disconnect(sid):
    print("I'm disconnected!")


@sio.event
async def send_message(sid, data):
    print("movida")
