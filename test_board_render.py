#from battleship_fun import *
from bship_game_controller import *
from bship_board_render import *

###
###
###

board_size = {"lines": 10, "columns": 10}

players = {1 : "player 01", 2 : "player 02"}

am = (
    {"class" : "aircraft carrier", "tag" : "ac", "size" : 4, "quantity" : 1},
    {"class" : "cruiser", "tag" : "cr", "size" : 3, "quantity" : 2},
    {"class" : "destroyer", "tag" : "dt", "size" : 2, "quantity" : 2},
    {"class" : "submarine", "tag" : "sb", "size" : 2, "quantity" : 1},
    {"class" : "assault boat", "tag" : "ab", "size" : 1, "quantity" : 4},
    )


bg = {
    1 : {1 : False,2 : "targeted",3 : "targeted",4 : False,5 : False,6 : "cruiser",7 : "cruiser",8 : False,9 : False,10 : False},
    2 : {1 : "assault boat",2 : False,3 : "water",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    3 : {1 : False,2 : False,3 : "water",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : "targeted",10 : False},
    4 : {1 : False,2 : "assault boat",3 : False,4 : False,5 : False,6 : "water",7 : False,8 : False,9 : False,10 : False},
    5 : {1 : False,2 : False,3 : False,4 : False,5 : False,6 : "assault boat",7 : False,8 : False,9 : False,10 : False},
    6 : {1 : False,2 : False,3 : False,4 : "water",5 : False,6 : False,7 : "cruiser",8 : "cruiser",9 : "cruiser",10 : False},
    7 : {1 : "targeted",2 : False,3 : "cruiser",4 : "targeted",5 : False,6 : False,7 : False,8 : False,9 : False,10 : False},
    8 : {1 : False,2 : False,3 : "cruiser",4 : False,5 : False,6 : "targeted",7 : "water",8 : False,9 : "targeted",10 : "targeted"},
    9 : {1 : False,2 : "water",3 : "cruiser",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    10 : {1 : "water",2 : "water",3 : False,4 : "assault boat",5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    }

bg1 = {
    "player1" : {
    1 : {1 : False,2 : False,3 : False,4 : False,5 : False,6 : False,7 : False,8 : False,9 : False,10 : False},
    2 : {1 : "assault boat",2 : False,3 : "water",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    3 : {1 : False,2 : False,3 : "water",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : "targeted",10 : False},
    4 : {1 : False,2 : "assault boat",3 : False,4 : False,5 : False,6 : "water",7 : False,8 : False,9 : False,10 : False},
    5 : {1 : False,2 : False,3 : False,4 : False,5 : False,6 : "assault boat",7 : False,8 : False,9 : False,10 : False},
    6 : {1 : False,2 : False,3 : False,4 : "water",5 : False,6 : False,7 : "cruiser",8 : "cruiser",9 : "cruiser",10 : False},
    7 : {1 : "targeted",2 : False,3 : "cruiser",4 : "targeted",5 : False,6 : False,7 : False,8 : False,9 : False,10 : False},
    8 : {1 : False,2 : False,3 : "cruiser",4 : False,5 : False,6 : "targeted",7 : "water",8 : False,9 : "targeted",10 : "targeted"},
    9 : {1 : False,2 : "water",3 : "cruiser",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    10 : {1 : "water",2 : "water",3 : False,4 : "assault boat",5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    },
    "player2":  {
    1 : {1 : False,2 : "targeted",3 : "targeted",4 : False,5 : False,6 : "cruiser",7 : "cruiser",8 : False,9 : False,10 : False},
    2 : {1 : "assault boat",2 : False,3 : "water",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    3 : {1 : False,2 : False,3 : "water",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : "targeted",10 : False},
    4 : {1 : False,2 : "assault boat",3 : False,4 : False,5 : False,6 : "water",7 : False,8 : False,9 : False,10 : False},
    5 : {1 : False,2 : False,3 : False,4 : False,5 : False,6 : "assault boat",7 : False,8 : False,9 : False,10 : False},
    6 : {1 : False,2 : False,3 : False,4 : "water",5 : False,6 : False,7 : "cruiser",8 : "cruiser",9 : "cruiser",10 : False},
    7 : {1 : "targeted",2 : False,3 : "cruiser",4 : "targeted",5 : False,6 : False,7 : False,8 : False,9 : False,10 : False},
    8 : {1 : False,2 : False,3 : "cruiser",4 : False,5 : False,6 : "targeted",7 : "water",8 : False,9 : "targeted",10 : "targeted"},
    9 : {1 : False,2 : "water",3 : "cruiser",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    10 : {1 : "water",2 : "water",3 : False,4 : "assault boat",5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    }}

bg2 = {
    "player1" : {
    1 : {1 : False,2 : False,3 : False,4 : False,5 : "targeted",6 : False,7 : False,8 : False,9 : False,10 : False},
    2 : {1 : False,2 : False,3 : False,4 : False,5 : "targeted",6 : False,7 : False,8 : False,9 : False,10 : False},
    3 : {1 : False,2 : "targeted",3 : False,4 : False,5 : False,6 : False,7 : False,8 : False,9 : False,10 : False},
    4 : {1 : False,2 : "targeted",3 : False,4 : False,5 : False,6 : False,7 : "water",8 : False,9 : False,10 : False},
    5 : {1 : False,2 : "targeted",3 : False,4 : False,5 : False,6 : False,7 : False,8 : False,9 : False,10 : False},
    6 : {1 : False,2 : False,3 : "water",4 : "water",5 : False,6 : False,7 : False,8 : False,9 : False,10 : False},
    7 : {1 : False,2 : False,3 : False,4 : False,5 : "targeted",6 : "targeted",7 : "targeted",8 : "targeted",9 : False,10 : False},
    8 : {1 : False,2 : False,3 : False,4 : False,5 : False,6 : False,7 : False,8 : False,9 : False,10 : False},
    9 : {1 : False,2 : False,3 : "water",4 : False,5 : "targeted",6 : False,7 : False,8 : False,9 : False,10 : False},
    10 : {1 : False,2 : False,3 : False,4 : False,5 : "targeted",6 : False,7 : False,8 : False,9 : False,10 : False},
    },
    "player2":  {
    1 : {1 : False,2 : "targeted",3 : "targeted",4 : False,5 : False,6 : "cruiser",7 : "cruiser",8 : False,9 : False,10 : False},
    2 : {1 : "assault boat",2 : False,3 : "water",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    3 : {1 : False,2 : False,3 : "water",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : "targeted",10 : False},
    4 : {1 : False,2 : "assault boat",3 : False,4 : False,5 : False,6 : "water",7 : False,8 : False,9 : False,10 : False},
    5 : {1 : False,2 : False,3 : False,4 : False,5 : False,6 : "assault boat",7 : False,8 : False,9 : False,10 : False},
    6 : {1 : False,2 : False,3 : False,4 : "water",5 : False,6 : False,7 : "cruiser",8 : "cruiser",9 : "cruiser",10 : False},
    7 : {1 : "targeted",2 : False,3 : "cruiser",4 : "targeted",5 : False,6 : False,7 : False,8 : False,9 : False,10 : False},
    8 : {1 : False,2 : False,3 : "cruiser",4 : False,5 : False,6 : "targeted",7 : "water",8 : False,9 : "targeted",10 : "targeted"},
    9 : {1 : False,2 : "water",3 : "cruiser",4 : False,5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    10 : {1 : "water",2 : "water",3 : False,4 : "assault boat",5 : False,6 : "targeted",7 : False,8 : False,9 : False,10 : False},
    }}





###
### Tests - bship_board_render
###

# OK
# display_frame("Isso é um teste", "Digite algo e tecle enter para parar", ">>>", 5, True)

# OK
# display_board(am, bg, True)

# OK
# display_instruction("Isso é um teste")

# OK
# clear()

###
### Tests - bship_game_controller import
###




# OK
# print(enemy_board("player2", bg1))

print(ask_for_coordinate(am, board_size, bg, "sua vez de atacar", "entre coordenada"))



