# runs the program for Assignment Part A

from board import Board
from team import Team
from piece import Piece

# set up board and teams
game_board = Board()
team_white = Team("White", game_board, True)
team_black = Team("Black", game_board, False)
size = game_board.size

def calculate_moves(t):
    # calculates the total no. possible moves for a given time
    pieces = t.get_my_pieces()
    moves = 0
    for p in pieces:
        # check if can move or jump right
        if t.game_board.piece_can_move(p, 0, 1):
            moves = moves + 1
        elif t.game_board.piece_can_move(p, 0, 2):
            moves = moves + 1
        # check if can move or jump left
        if t.game_board.piece_can_move(p, 0, -1):
            moves = moves + 1
        elif t.game_board.piece_can_move(p, 0, -2):
            moves = moves + 1
        # check if can move or jump down
        if t.game_board.piece_can_move(p, 1, 0):
            moves = moves + 1
        elif t.game_board.piece_can_move(p, 2, 0):
            moves = moves + 1
        # check if can move or jump up
        if t.game_board.piece_can_move(p, -1, 0):
            moves = moves + 1
        elif t.game_board.piece_can_move(p, -2, 0):
            moves = moves + 1
    return moves

def massacre(t):
    # TODO: massacre function
    print("Not done yet!")

for row in range(0,size):
    # read lines from input and add pieces to the board
    line = input()
    col = 0
    for c in line.split():
        if c == 'X':
            game_board.add_piece("X", row, col)
        elif c == '@':
            game_board.add_piece("Black", row, col)
        elif c == 'O':
            game_board.add_piece("White", row, col)
        col = col + 1

# take the command as the last input
command = input()

# "Moves"
if command.capitalize() == "Moves":
    print(calculate_moves(team_white))
    print(calculate_moves(team_black))

# "Massacre"
if command.capitalize() == "Massacre":
    massacre(team_white)
    game_board.print_board() # get rid of this later


