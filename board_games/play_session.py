from player import Player
from game import Game

class PlaySession:
    def __init__(self, game: Game):
        self.__results : dict[Player, int, GameResult] = {}
        self.__game : Game = game