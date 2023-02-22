from player import Player
import random
class Game:
        
    def __init__(self):
        
        self.choices = ["rock", "paper", "scissors", "lizard", "spock"]
        self.rules = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["paper", "spock"],
            "spock": ["rock", "scissors"]
        }

    def play(self, player_choice):
        player_choice = player_choice.lower()
        computer_choice = random.choice(self.choices)
        result = self.compare(player_choice, computer_choice)
        return (computer_choice, result)

    def compare(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        elif computer_choice in self.rules[player_choice]:
            return "win"
        else:
            return "lose"

game = Game()

while True:
    player_choice = input("Choose rock, paper, scissors, lizard, or spock: ")
    computer_choice, result = game.play(player_choice)
    print(f"Computer chose {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "n":
        break


