import random 
from game import game

class action():
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

# is this the right section for this ? what do i put in between for and import and in the () for actions