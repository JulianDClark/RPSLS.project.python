
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        


    def choose(self):
        pass

class HumanPlayer(Player):
    def choose(self):
        while True:
            self.choice = input("Enter your choice: ")
            if self.choice.capitalize() in choices:
                break
            print("Invalid input, please try again.")

class ComputerPlayer(Player):
    def choose(self):
        self.choice = random.choice(choices)

class RPSLS:
    def __init__(self):
        self.human = HumanPlayer("You")
        self.computer = ComputerPlayer("Computer")
    def play(self):
        print("Rock, Paper, Scissors, Lizard, Spock!")
        self.human.choose()
        self.computer.choose()
        print(f"{self.human.name} chose {self.human.choice}")
        print(f"{self.computer.name} chose {self.computer.choice}")
        print(self.who_wins())

    def who_wins(self):
        if self.human.choice == self.computer.choice:
            return "It's a tie!"
        elif (self.human.choice == "Rock" and self.computer.choice == "Scissors") or \
             (self.human.choice == "Scissors" and self.computer.choice == "Paper") or \
             (self.human.choice == "Paper" and self.computer.choice == "Rock") or \
             (self.human.choice == "Rock" and self.computer.choice == "Lizard") or \
             (self.human.choice == "Lizard" and self.computer.choice == "Spock") or \
             (self.human.choice == "Spock" and self.computer.choice == "Scissors") or \
             (self.human.choice == "Scissors" and self.computer.choice == "Lizard") or \
             (self.human.choice == "Lizard" and self.computer.choice == "Paper") or \
             (self.human.choice == "Paper" and self.computer.choice == "Spock") or \
             (self.human.choice == "Spock" and self.computer.choice == "Rock"):
            return f"{self.human.name} wins!"
        else:
            return f"{self.computer.name} wins!"

choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# Main game loop
while True:
    game = RPSLS()
    game.play()

    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "n":
      break









