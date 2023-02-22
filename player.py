import random 
from player import Player 

class action(Player):
    Rock = 0
Paper = 1
scissors = 2
Lizard = 3
Spock = 4

victories = {action.scissors: [action.lizard, action.paper],
action.paper: [action.spock, action.rock],
action.rock: [action.lizard, action.paper],
action.lizard: [action.spock, action.paper],
action.spock: [action.scissors, action.rock]}

def get_user_selection():
    choices =[f"{action.name}[{action.value}]"for action in action]
    choices_str ='', ''. join(choices)
    selection = int(input(f'enter a choice({choices_str}):'))
    action = action(selection)
    return action
def get_computer_selection():
    selection = random.randint(0,len(action)- 1)
    action = action(selection)
    return action 
def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action: 
        print(f'both players selected {user_action.name} its a tie')
    elif computer_action in defeats:
        print(f'{user_action.name} beats {computer_action.name} you win')
    else: 
        print(f'{computer_action.name} beats {user_action.name} you lose')

