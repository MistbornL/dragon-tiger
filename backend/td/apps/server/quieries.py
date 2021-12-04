from td.apps.documents.document import Round, GamePlayer


async def get_or_create_game_round(game_id: str):
    # game_round = await Round.find_one(Round.game_id == game_id)
    # if game_round:
    #     return game_round
    game_round = Round(game_id=game_id)
    return await game_round.save()


async def get_or_create_game_player(game_id):
    game_player = await GamePlayer.find_one(GamePlayer.game_round_id == game_id)
    if game_player:
        return game_player
    game_player = GamePlayer(game_round_id=game_id)
    return await game_player.save()
