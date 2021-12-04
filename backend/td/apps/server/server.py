import socketio
from urllib.parse import parse_qs
from td.apps.documents.document import Game, Round, GamePlayer
from beanie import PydanticObjectId
from .quieries import get_or_create_game_round, get_or_create_game_player
from .service.place_bets import place_bets
from .service.winer import winer

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
    game_round_id = data.get('game_round_id')
    game_round = await Round.get(PydanticObjectId(game_round_id))
    game_player = await get_or_create_game_player(game_round_id)

    card = data['card']

    if game_round.card_count == 0:
        game_round.dragon_card = card
        game_round.card_count += 1
        await game_round.save()
        await sio.emit("send_dragon_card", {"card": card}, room=game_round.round_id)
    else:
        game_round.tiger_card = card
        game_round.card_count += 1
        await game_round.save()
        await sio.emit("send_tiger_card", {"card": card}, room=game_round.round_id)

    game_round.winner = await winer(game_round.dragon_card, game_round.tiger_card, game_round)
    await game_round.save()
    await sio.emit('winner', {'winner': game_round.winner}, room=game_round.round_id)
    print(game_round)
    print(game_player)

    all_game_player = await GamePlayer.find_all(game_round_id=game_round_id).to_list()
    print(f"all: {all_game_player}")


@sio.event
async def place_bet(sid, data):
    amount = int(data.get('amount'))
    type = data.get('type')
    round_id = data.get('game_round_id')

    game_player = await get_or_create_game_player(round_id)
    await place_bets(game_player, type, amount)
    print(game_player)


@sio.event
async def disconnect(sid):
    print("I'm disconnected!")
