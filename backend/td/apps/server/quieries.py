from td.apps.documents.document import Round, GamePlayer


async def get_or_create_game_round(game_id: str):
    # game_round = await Round.find_one(Round.round_id == game_id)
    # if game_round:
    #     return game_round
    game_round = Round(round_id=game_id)
    return await game_round.save()



