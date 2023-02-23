# from game import Game
# if __name__ == "__main__":
#     game = Game()
#     game.run_game()
import random

# define the valid choices and their abbreviations
choices = {"rock": "r", "paper": "p", "scissors": "s", "lizard": "l", "spock": "sp"}

# define the rules of the game: each choice beats the preceding two in the list
rules = {"rock": ["scissors", "lizard"],
         "paper": ["rock", "spock"],
         "scissors": ["paper", "lizard"],
         "lizard": ["paper", "spock"],
         "spock": ["rock", "scissors"]}

# function to print the rules of the game
def print_rules():
    print("Welcome to RPSLS (Rock, Paper, Scissors, Lizard, Spock)!")
    print("Here are the rules:")
    print("- Rock crushes Scissors and crushes Lizard")
    print("- Paper covers Rock and disproves Spock")
    print("- Scissors cuts Paper and decapitates Lizard")
    print("- Lizard eats Paper and poisons Spock")
    print("- Spock vaporizes Rock and smashes Scissors")
    print("The first player to win three rounds is the winner.")
    print()

# function to get the player's choice
def get_player_choice():
    while True:
        choice = input("Enter your choice (r/p/s/l/sp): ").lower()
        if choice in choices.values():
            # convert the abbreviation back to the full choice name
            for c, a in choices.items():
                if choice == a:
                    return c
        else:
            print("Invalid choice. Please try again.")

# function to get the computer's choice
def get_computer_choice():
    return random.choice(list(choices.keys()))

# function to determine the winner of the game
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie!"
    elif computer_choice in rules[player_choice]:
        return "You win!"
    else:
        return "Computer wins!"

# main game loop
print_rules()
player_score = 0
computer_score = 0
while player_score < 3 and computer_score < 3:
    print("Score: Player {} - {} Computer".format(player_score, computer_score))
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {player_choice}, and the computer chose {computer_choice}.")
    winner = get_winner(player_choice, computer_choice)
    print(winner)
    if winner == "You win!":
        player_score += 1
    elif winner == "Computer wins!":
        computer_score += 1
print("Final score: Player {} - {} Computer".format(player_score, computer_score))
if player_score > computer_score:
    print("You win the game!")
else:
    print("Computer wins the game.")


# game = Game() 
# game.display_greeting()
# game.play_game()
