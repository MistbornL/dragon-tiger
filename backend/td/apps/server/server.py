import socketio
from urllib.parse import parse_qs
from td.apps.documents.document import Game
from beanie import PydanticObjectId
from .quieries import get_or_create_game_round


static_files = {
    '/': './public',
}
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=[])
s_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    print(environ)
    game_id = parse_qs(environ['QUERY_STRING']).get("game_id")[0]
    print(game_id)
    game = await Game.get(PydanticObjectId(game_id))
    game_round = await get_or_create_game_round(game_id)
    send_data = {
        "min_bet": game.minBet,
        "max_bet": game.maxBet,
        "name": game.name,
        "game_round_id": str(game_round.id)
    }
    sio.enter_room(sid, game_id)
    await sio.emit("on_connect_data", send_data, to=sid)
    print("aq var")


@sio.event
async def scan_card(sid, data):
    card = data.get('card')
    print(data)


@sio.event
async def disconnect(sid):
    print("I'm disconnected!")