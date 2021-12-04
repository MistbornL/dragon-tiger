async def misagebi(gameplayer, round_id, game_round):
    all = await gameplayer.find_all().to_list()
    for player in all:
        if player.game_round_id == round_id:
            if player.dragon_bet > 0 and game_round.winner == "dragon":
                player.deposit += player.dragon_bet * 2
                return await player.save()
            elif player.tiger_bet > 0 and game_round.winner == "tiger":
                player.deposit += player.tiger_bet * 2
                return await player.save()
            elif player.tie_bet > 0 and game_round.winner == "tie":
                player.deposit += player.tie_bet * 2
                return await player.save()
