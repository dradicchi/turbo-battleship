####
#### Module: Control game rounds in the command line battleship game
####

#
# 2023 - Daniel Radicchi - Licensed as CC BY
#
# This module is part of my first-steps in python studying and intends to 
# adopt a functional inspired approach.
#

# Imports the module to render the board.
from bship_board_render import *


##
## Game board controlling
##


def build_game_board(players, player_board):
    """Generate a complete empty board with players x (lines x columns)"""

    game_board = {player : player_board for player in players}

    return game_board


def build_player_board(lines, columns):
    """Generate a empty player board with lines x columns dimension"""

    player_board = {lin : {col : False for col in range(1, columns + 1)}
            for lin in range(1, lines + 1)}  

    return player_board

def build_player_ships(ship_inventory):
    """Generate a list of ships available to arrange in a player board"""

    player_ships = [ship["tag"] for ship in ship_inventory 
            for n in range(1, ship["qty"] + 1)]

    return player_ships

def arrange_game_board(player_ships, game_board):
    """Arrange the navies on the game board"""

    for player_board in game_board:

        for ship in player_ships:

            is_ship_fit = False

            while not is_ship_fit:

                lin, col = input().split(",")

                if check_ship_fit(ship, lin, col, player_board):

                    game_board[player][lin][col] = ship
                    is_ship_fit = True

                else:

                    print("")



    return game_board











ship_inventory = (
    {"class" : "aircraft carrier", "tag" : "ac", "size" : 4, "qty" : 1},
    {"class" : "cruiser", "tag" : "cr", "size" : 3, "qty" : 2},
    {"class" : "destroyer", "tag" : "dt", "size" : 2, "qty" : 2},
    {"class" : "submarine", "tag" : "sb", "size" : 2, "qty" : 1},
    {"class" : "assault boat", "tag" : "ab", "size" : 1, "qty" : 4},
    )

for ship in ship_inventory:

    
    print(ship["asas"])











def arrange_ships(board_size, players, arsenal_model):
    """Arrange the two navies on the naval battle game board"""

    # Note: A player board is a matrix of X horizontal lines, each them with 
    # Y columns. In a starting game board, a slot matrix can holds info about a
    # ship portion or empty space. As the game develops, the requested slots
    # will hold info about the shots. Below, a model of an arranged board:
    #
    #   arranged_board = {
    #       "player 1" :  {
    #           ln1 : { col1 : "ship_a", col2 : "ship_b", col3 : ...},
    #           2 : { 1 : "ship_a", 2 : "ship_a", 3 : ...},
    #           3 : { 1 : "False", 2 : "ship_b", 3 : ...},
    #           4 : { 1 : "ship_a", 2 : "False", 3 : ...},
    #           ...
    #           }
    #       "player 2" :  {
    #           1 : { 1 : "ship_a", 2 : "ship_b", 3 : ...},
    #           2 : { 1 : "ship_a", 2 : "ship_a", 3 : ...},
    #           3 : { 1 : "False", 2 : "ship_b", 3 : ...},
    #           4 : { 1 : "ship_a", 2 : "False", 3 : ...},
    #           ...
    #           }
    #       }
    #
    # Slots with "False" value mean empty water spaces in at the beginning of
    # the game.

    # Builds an empty board.
    empty_board = build_board(board_size, players)

    # Builds ships defined in the arsenal model.
    ship_list = build_ships(arsenal_model)

    display_instruction("First, we need to arrange the board game!")

    # Arranges their respective ships for each player. 
    for player in players:

        # Copies a new empty board to a player.
        initial_board[player] = empty_board[:]

        for ship in ship_list:

            does_ship_fit = False

            # Asks for a coordinate and checks if ship fits in the board.
            while not does_ship_fit:

                print("Arranging the " + player.upper() + "board... \n\n")

                print("Please, choose a initial coordinate to a " + 
                        ship["class"].upper() + ".")
                print("This ship class needs " + str(ship["size"]) + 
                        " linear slots in the board.\n\n")

                chosen_coordinate = ask_for_coordinate(board_size)

                ship_orientation = ""

                while not ship_orientation in ["n", "s", "w", "e"]:
                    ship_orientation = input("Define a cardinal orientation: " + 
                        " (n = north, s = south, w = west or e = east) ")

                does_ship_fit = does_fit(initial_board[player], ship["size"], 
                    chosen_coordinate, ship_orientation)

            # Updates the initial player board.
            initial_board[player] = put_ship(initial_board[player], 
                    ship["class"], ship["size"], chosen_coordinate,
                    ship_orientation)

            display_instruction("Ship was arranged! " + 
                    "Verifying if there are more ships to arrange...")

        display_instruction("All the " + player.upper() + 
                " ships was arranged!")

    return initial_board


def build_board(board_size, players):
    """Build a empty bi-dimentional board"""

    empty_board = {}

    #Lists of vertical and horizontal coordinates
    ln_coordinates = [num for num in range(1, board_size["horizontal"] + 1)]
    col_coordinates = [num for num in range(1, board_size["vertical"] + 1)]

    # Combines each column coordinate with each line coordinate and returns an
    # empty board for each player.
    empty_board = {player : {ln : {col : False for col in col_coordinates} 
            for ln in ln_coordinates} for player in players.values()}
   
    return empty_board


def does_fit(board, ship_size, coordinate, cardinal_orientation):
    """Check if the ship fit in the position"""

    does_ship_fit = False

    if (cardinal_orientation == "n") and (ship_size <= coordinate["vertical"]):

            demanded_slots = demanded_slots(ship_size, coordinate, 
                    cardinal_orientation)

            for slot in demanded_slots:

                if board[slot] == False:

                    does_ship_fit






            does_ship_fit = True





    elif cardinal_orientation == "s":
        False
    elif cardinal_orientation == "w":
        False
    elif cardinal_orientation == "e":
        False

    return does_ship_fit


def demanded_slots(ship_size, coordinate, cardinal_orientation):
    """Return a list of demanded slots to put a ship"""

    demanded_slots = ""

    return demanded_slots



def put_ship(board, ship_class, ship_size, coordinate, cardinal_orientation):
    """Put a ship in the board game"""

    if cardinal_orientation == "n":
        False
    elif cardinal_orientation == "s":
        False
    elif cardinal_orientation == "w":
        False
    elif cardinal_orientation == "e":
        False






    update_board = ""

    return update_board











def build_ships(arsenal_model):
    """Build all ships defined in the arsenal model"""

    # Builds the correct quantity for each ship class.
    # Arsenal model: ({"class" : "str", "size" : int, "quantity" : int}, ...)
    # Output form: [{"class" : "str", "size" : int}, {"class" : ...}, ...]


    for ship_model in arsenal_model:
        for qty in range(0, ship_model["quantity"]):

            ship = {"class" : ship_model["class"], "size" : ship_model["size"]}
            ship_list.append(ship)

    return ship_list


##
## Game dynamics
##

def ask_for_coordinate(arsenal_model, board_size, board, msg, instr):
    """Show a board and ask a player to a coordinate"""

    prompt = ("Limits:\n\t- Line coordinate: choose from 1 to " + 
                str(board_size["lines"]) + 
                ";\n\t- Column coordinate: choose from 1 to " + 
                str(board_size["columns"]) + 
                ";\n\n\tType a comma between the coordinates (ex: 2,3): ")

    coordinate = ""

    # Shows a board and asks a coordinate.
    # Keeps asking until the coordinate values are correct.
    while len(coordinate) < 2:

        clear()
        display_board(arsenal_model, board)

        coordinate = [value for value in display_frame(msg, instr, prompt, 1).split(",") if value.isnumeric]

    return coordinate # returns a list as [3, 5].


# def run_a_round(arsenal_model, board_size, game_board):
#     """Run a round game of the naval battle game"""

#     for player in game_board.keys():

#         enemy_board = enemy_board(player, game_board)
        
#         message = "It's " + player.upper() + "'s turn to play!"
        
#         instr = "Enter the coordinates to your shot:"

#         # Repeats an asking to a coordinate if this coordinate has already 
#         # been called.
#         coord_already_called = True

#         while coord_already_called:

#             # Shows the enemy board and asks for the shoot coordinate.
#             # The function "ask_for_coordinate" Keeps asking until the coordinate
#             # values are valid.
#             coordinate = ask_for_coordinate(board_size, enemy_board, message,
#                     instruction)

#             for column in enemy_board[coordinate[0]].keys():

#                 if (column[coordinate[1]] == "targeted" or 
#                         column[coordinate[1]] == "water"):

#                     display_instruction("Sorry... This coordinate has" +
#                             " already been called!")

#                 else:
#                     coord_already_called = False

#         # When a valid and already non-requested coordinate is inputed, updates
#         # the enemy board.
#         for column in enemy_board[coordinate[0]].keys():

#             if column[coordinate[1]] == False:

#                 column[coordinate[1]] = "water"

#                 display_instruction("Ops... the shot was in the water.")


#             else:
                
#                 coord_already_called = False












#         # If the shot was in the water.
#         enemy_board[shot_coordinate] == False:
#             enemy_board[shot_coordinate] = "water"
#             display_instruction("Ops... the shot was in the water.")

#         # If the shot find a ship.
        
#              target = enemy_board[shot_coordinate]
#              enemy_board[shot_coordinate] = "targeted"
#              display_instruction("Wow! A " + target.upper() + " was targeted!")

#         # Saves the result of player's shot.
#         inv_updated_board[player] = enemy_board

#     # Re-swaps the player boards.
#     updated_board = swap_board(inv_updated_board)

#     return updated_board






def enemy_board(player, game_board):
    """Return the enemy board."""

    for enemy, player_board in game_board.items():
        if player != enemy:
            enemy_board = player_board

    return enemy_board


def if_a_winner(game_board):
    """Check if there is a winner in the naval battle game"""

    # Checks the winner status for each player.
    for player, board_player in game_board.items():

        player_columns_values = [value for value in columns for columns in board_player.values()]
        print(player_columns_values)
        input()

    #         # Checks if are only water (False or "water" values) in the player
    #         # board.
    #         if 2 < len(set(player_columns_values)):
    #             winner = False

    #         else:
    #             winner = player

    # return winner # Return the winner label.

