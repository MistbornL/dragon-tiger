from typing import Optional, List

from beanie import Document


class Game(Document):
    name: str
    deck: Optional[List]
    minBet: Optional[int] = 5
    maxBet: Optional[int] = 10000


class Round(Document):
    end_time: int
    dragon_card: str
    tiger_card: str
    winner: str
    card_counted: int
    finished: bool


class GamePlayer(Document):
    game_round: int
    total_bet: int
    dragon_bet: int
    tiger_bet: int
    tie_bet: int
    deposit: int


class User(Document):
    email: str
    password: str
