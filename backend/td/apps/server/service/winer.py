async def winer(dragon, tiger, game_round):
    try:
        if dragon[:-1] > tiger[:-1]:
            game_round.finished = True
            return "dragon"
        elif dragon[:-1] < tiger[:-1]:
            game_round.finished = True
            return "tiger"
    except TypeError:
        print("waiting for cards...")
