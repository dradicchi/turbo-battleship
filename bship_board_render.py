####
#### Module: Render the board in the command line battleship game
####

#
# 2023 - Daniel Radicchi - Licensed as CC BY
#
# This module is part of my first-steps in python studying and intends to 
# adopt a functional inspired approach.
#

from os import system, name


def display_frame(message, instruction, prompt, height, clear_screen=False):
    """Display a full screen message, wait for input and return inputed data"""

    ########################################################
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                 Main message here                    #
    #                                                      #
    #                Instruction here...                   #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    #                                                      #
    ########################################################


    # Assigns the values to the basic frame structure
    message_left_blank_space = (50 - len(message)) // 2
    instruction_left_blank_space = (50 - len(instruction)) // 2
    full_line_frame = "\t" +  ("#" * 56)
    blank_line_frame = "\t# " + " " * 52+ " #"

    # Clears the screen if called
    if clear_screen == True:
        clear()

    print(full_line_frame)

    for line in range (0, height):
        print(blank_line_frame)

    print("\t#", " " *  message_left_blank_space, message, 
            " " * (50 - len(message) - message_left_blank_space),"#")
    print(blank_line_frame)
    print("\t#", " " *  instruction_left_blank_space, instruction, 
            " " * (50 - len(instruction) - instruction_left_blank_space),"#")

    for line in range (0, height):
        print(blank_line_frame)

    print(full_line_frame)
    inputed_data = input("\n\t" + prompt)

    return inputed_data 


def display_board(arsenal_model, board, show_no_targeted_ships=False):
    """Display a player board"""

    # Note: A player board is a matrix of X horizontal lines, each them with 
    # Y columns. In a starting game board, a slot matrix can holds info about a
    # ship portion or empty space. As the game develops, the requested slots
    # will hold info about the shots. Below, a model of a board:
    #
    #   board = {
    #           ln1 : { col1 : "ship_a", col2 : "ship_a", col3 : ...},
    #           2 : { 1 : "ship_a", 2 : "ship_a", 3 : ...},
    #           3 : { 1 : "False", 2 : "ship_a", 3 : ...},
    #           4 : { 1 : "ship_a", 2 : "False", 3 : ...},
    #           ...
    #           }
    #
    # Slots with "False" value mean empty water spaces in at the beginning of
    # the game.

    # A rendered board example
    #
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   |    | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   | 01 |    |    |    |    |    |    |    |    |    |    |
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   | 02 |    |    |    |    |    |    |    |    |    |    |
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   | 03 |    |    | TG |    |    |    |    |    |    |    |
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   | 04 |    |    |    | WA |    |    |    |    |    |    |
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   | 05 |    |    |    | WA |    |    |    |    |    |    |
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   | 06 |    | TG |    |    |    |    |    |    |    |    |
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   | 07 |    |    |    |    |    |    |    |    |    |    |
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   | 08 |    |    |    |    |    |    |    |    |    |    |
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   | 09 |    |    |    |    |    |    |    |    |    |    |
    #   +----+----+----+----+----+----+----+----+----+----+----+
    #   | 10 |    |    |    |    |    |    |    |    |    |    |
    #   +----+----+----+----+----+----+----+----+----+----+----+

    # generates a key-value-pair collection to ships with class and tag values.
    ship_tags = {ship["class"]:ship["tag"] for ship in arsenal_model}

    horizontal_line = "\t+" + ("----+" * (len(board.values()) + 1))
    
    # Displays the header board.
    print(horizontal_line)
    print("\t|    |", end=" ")

    for col in range(1, len(board.keys()) + 1):
        print(str(col).zfill(2) + " |", end=" ") # Prints column label

    print("\n" + horizontal_line)

    # Displays game field lines.
    for line, cols in board.items():
        
        print("\t| " + str(line).zfill(2) + " |", end=" ") # Prints line label
        
        # Prints columns for a line. 
        for col, value in cols.items():
            
            if value == False:
                print("   |", end=" ")

            elif value == "water": 
                print("WA |", end=" ")

            elif value == "targeted": 
                print("TG |", end=" ")

            # The False flag masks the remaining ships.
            elif show_no_targeted_ships == False:
                print("   |", end=" ")

            else:
                print(ship_tags[value].upper() + " |", end=" ")

        print("\n" + horizontal_line)

    return False 


def display_instruction(instruction):
    """Display instructions with a wait step"""

    print("\n\t" + instruction)
    inputed_data = input("\tPress any key to continue... ")

    return inputed_data


def clear():
    """Clear the screen"""

    # Ref: https://stackoverflow.com/questions/66010549/python-clear-output

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear')

