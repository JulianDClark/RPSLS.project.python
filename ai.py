from player import Player
import random
from time import sleep
class AI(Player):
    
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.score = 0
        self.wins = 0
        
    def choose_gesture(self):
        self.gesture = str(random.randint(0, 4))
        gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        sleep(1)
        print(f"{self.name} has picked {gesture_list[int(self.choose_gesture)]}")

        return self.gesture