import socketio
from urllib.parse import parse_qs
from td.apps.documents.document import Game, Round
from beanie import PydanticObjectId
from .quieries import get_or_create_game_round

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=[])
s_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    print(environ)
    game_id = parse_qs(environ['QUERY_STRING']).get("game_id")[0]
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
    print("im connected")


@sio.event
async def scan_card(sid, environ, data):
    card = data.get('card')
    await sio.emit("sdasd", data)

    game_id = parse_qs(environ['QUERY_STRING']).get("game_id")[0]
    round = await Round.get(PydanticObjectId(game_id))
    dragon_card = round.dragon_card
    tiger_card = round.tiger_card
    cc = round.card_count
    if cc == 0:
        tiger_card == card
        cc += 1
    else:
        dragon_card = card
    await round.save()
    if dragon_card[1:] > tiger_card[1:]:
        round.winner == dragon_card
    elif dragon_card[1:] < tiger_card[1:]:
        round.winner == tiger_card
    else:
        round.winner = "tie"
    await round.save()


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
