from typing import Optional, List

from beanie import Document


class Game(Document):
    name: str
    minBet: Optional[int] = 5
    maxBet: Optional[int] = 10000


class Round(Document):
    end_time: int = 123123
    game_id: str
    dragon_card: str = None
    tiger_card: str = None
    winner: str = None
    card_count: int = 0
    finished: bool = False


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
