from ai import AI
from game import Game

class Game:
    def __init__(self):
        self.player_one = AI("Player One")
        self.player_two = Game("Player Two")
        self.player_one.set_opponent(self.player_two)
        self.player_two.set_opponent(self.player_one)
        self.player_one.set_game(self)
        self.player_two.set_game(self)
        self.player_one.set_gesture_list()
