####
#### A command line battleship game in Python
####

#
# This program is part of my first-steps in python studying and intends to 
# adopt a functional inspired approach.
# 

# Imports the modules to control the game flow and render the board.
from bship_game_controller import *
from bship_board_render import *


##
## Game settings
##

# Note: Despite of my intention for a functional oriented project, I decided to 
# leave this assignments out of the main function. In a future project 
# extension, is possible to implement a command line interface to set these
# parameters each new playing.

# Defines a bi-dimentional size board.
board_size = {"lines": 10, "columns": 10}

# Defines labels to each player.
players = {1 : "player 01", 2 : "player 02"}

# Defines a arsenal model. 
ship_inventory = (
    {"class" : "aircraft carrier", "tag" : "ac", "size" : 4, "qty" : 1},
    {"class" : "cruiser", "tag" : "cr", "size" : 3, "qty" : 2},
    {"class" : "destroyer", "tag" : "dt", "size" : 2, "qty" : 2},
    {"class" : "submarine", "tag" : "sb", "size" : 2, "qty" : 1},
    {"class" : "assault boat", "tag" : "ab", "size" : 1, "qty" : 4},
    )



##
## Game main functions
##

def start_game():
    """Start a new naval battle game"""

    display_frame("!! Wellcome to the BATTLESHIP GAME !!", 
            "Press any key to continue...","", 10, clear_screen=True)

    # Sets a initial board setup.
    game_board = arrange_ships(board_size, players, arsenal_model)

    # Game starts without a winner.
    there_is_winner = False

    # For each new round, in order:
    #   - Run an attack for each player and update the board;
    #   - Checks if there is a winner.
    while not there_is_winner:
        game_board = run_a_round(game_board, board_size)
        there_is_winner = if_a_winner(game_board) # Returns the winner.
        
    display_board(arsenal_model, enemy_board(there_is_winner, game_board))
    display_frame(("Congratulations!!! " + there_is_winner.upper() + 
            " is the winner!"), "Press any key to continue...","",  1)

    do_play_again()

    return False


def do_play_again():
    """Ask to play again. If yes, start a new game, otherwise quit"""

    play_again = display_frame("Do you play again?", 
            "Enter 'y' to start a new game or any key to quit:","> ",  10,
             clear_screen=True)

    if play_again.lower() == "y":
        start_game()

    else:
        display_frame("Thank you to play!!!", 
            "Press any key to quit... ","",  10, clear_screen=True)

        return False


##
## Enjoy the game!
##

start_game()
