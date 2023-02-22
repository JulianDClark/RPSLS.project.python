from player import Player
from game import Game
# if __name__ == "__main__":
#     game = Game()
#     game.run_game()
class Game:
    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = AI()
        self.choices = ["rock", "paper", "scissors", "lizard", "spock"]
        self.rules = {"rock": ["scissors", "lizard"],
                      "paper": ["rock", "spock"],
                      "scissors": ["paper", "lizard"],
                      "lizard": ["paper", "spock"],
                      "spock": ["rock", "scissors"]}
    def display_greeting(self,greeting):
        self.display_greeting = greeting
        print("Welcome to RPSLS")
        print('')
        print("Each match will be best 2 out of 3")
        print('\nRules\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n ')
        print("player one please choose one of the chooses")
        print('rock','paper','scissors','lizard','spock')


    def determine_winner(self, move1, move2):
        if move1 == move2:
            print("It's a tie!")
        elif move2 in self.rules[move1]:
            self.player1.add_point()
            print(f"{self.player1.get_name()} wins!")
        else:
            self.player2.add_point()
            print(f"{self.player2.get_name()} wins!")

    def play_game(self):
        for i in range(3):
            print(f"Round {i+1}:")
            self.player1.set_move(input("Player 1, enter your move: ").lower())
            self.player2.set_move()
            print(f"{self.player2.get_name()} chooses {self.player2.get_move()}.")
            self.determine_winner(self.player1.get_move(), self.player2.get_move())

        if self.player1.get_score() > self.player2.get_score():
            print(f"{self.player1.get_name()} wins the game!")
        elif self.player2.get_score() > self.player1.get_score():
            print(f"{self.player2.get_name()} wins the game!")
        else:
            print("The game is tied!")

game = Game() 
game.display_greeting()
game.play_game()
