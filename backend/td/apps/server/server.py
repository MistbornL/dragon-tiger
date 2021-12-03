import socketio
from urllib.parse import parse_qs
from td.apps.documents.document import Game, Round, GamePlayer
from beanie import PydanticObjectId
from .quieries import get_or_create_game_round
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
    game_player = await GamePlayer.get(game_round_id)
    print(game_player)
    card = data['card']

    if game_round.dragon_card == None:
        game_round.dragon_card = card
        game_round.card_count += 1
        await game_round.save()
        await sio.emit("send_dragon_card", {"card": card}, room=game_round.round_id)
    else:
        game_round.tiger_card = card
        game_round.card_count += 1
        await game_round.save()
        await sio.emit("send_tiger_card", {"card": card}, room=game_round.round_id)

    dragon = game_round.dragon_card
    tiger = game_round.tiger_card

    game_round.winner = await winer(dragon, tiger, game_round)
    await game_round.save()
    await sio.emit('winner', {'winner': game_round.winner}, room=game_round.round_id)
    print(game_round)

    # if game_round.finished == True:
    #     if game_round.winner == game_player


@sio.event
async def place_bet(sid, data):
    amount = int(data.get('amount'))
    type = data.get('type')
    game_round_id = data.get('game_round_id')
    game_round = await Round.get(PydanticObjectId(game_round_id))
    game_player = GamePlayer(id=game_round_id)
    await game_player.save()

    if type == "tiger":
        game_player.tiger_bet += amount
        await game_player.save()
    elif type == "dragon":
        game_player.dragon_bet = amount
        await game_player.save()
    else:
        game_player.tie_bet = amount

    # if game_round.winner == type:
    #     game_player.deposit += amount * 2
    #     await game_player.save()
    # elif game_round.winner != type:
    #     game_player.deposit -= amount
    #     await game_player.save()


@sio.event
async def disconnect(sid):
    print("I'm disconnected!")
