import socketio
from urllib.parse import parse_qs
from td.apps.documents.document import Game, Round
from beanie import PydanticObjectId
from .quieries import get_or_create_game_round

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=[])
s_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    game_id = parse_qs(environ['QUERY_STRING']).get("game_id")[0]
    game = await Game.get(PydanticObjectId(game_id))
    game_round = await get_or_create_game_round(game_id)
    send_data = {
        "min_bet": game.minBet,
        "max_bet": game.maxBet,
        "name": game.name,
        "game_round_id": str(game_round.id),
        "start_timestamp": 15
    }
    sio.enter_room(sid, game_id)
    await sio.emit("on_connect_data", send_data, to=sid)
    print("im connected")


@sio.event
async def scan_card(sid, data):
    print(data)
    game_round = await Round.get(PydanticObjectId(data['game_round_id']))
    card = data['card']
    if game_round.card_count:
        game_round.dragon_card = card
        game_round.card_count += 1
        await game_round.save()
        await sio.emit("send_dragon_card", {"card": card}, room=game_round.game_id)
    else:
        game_round.tiger_card = card
        game_round.card_count += 1
        await game_round.save()
        await sio.emit("send_tiger_card", {"card": card}, room=game_round.game_id)
    print(game_round)


@sio.event
async def receive_bet(sid, data):
    bet = data.get('bet')
    await sio.emit("sdasd", data)


@sio.event
async def receive_target(sid, data):
    target = data.get('target')
    await sio.emit("sdasd", data)


@sio.event
async def disconnect(sid):
    print("I'm disconnected!")
