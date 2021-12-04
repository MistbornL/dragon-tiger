async def place_bets(game_player, type, amount):
    if type == "tiger":
        game_player.tiger_bet += amount
        game_player.deposit -= amount
    elif type == "dragon":
        game_player.dragon_bet += amount
        game_player.deposit -= amount
    else:
        game_player.tie_bet += amount
        game_player.deposit -= amount

    game_player.total_bet += amount
    return await game_player.save()
