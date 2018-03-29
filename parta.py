# runs the program for Assignment Part A

from board import Board
from team import Team
from piece import Piece
import massacre_agent

# set up board and teams
game_board = Board()
team_white = Team("White", game_board, True)
team_black = Team("Black", game_board, False)
size = game_board.size

def calculate_moves(t):
    # calculates the total no. possible moves for a given time
    dir_check = [[0,1],[-1,0],[0,-1],[1,0]]     # directions to check
    pieces = t.get_my_pieces()
    moves = 0
    for p in pieces:
        # check for each piece in each direction
        for d in dir_check:
            # check if can move
            if t.game_board.piece_can_move(p, d[0], d[1]):
                moves += 1
            # if can't move, check if can jump instead
            elif t.game_board.piece_can_move(p, d[0]*2, d[1]*2):
                moves += 1
    return moves

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
    moves_count = 0
    while (team_black.pieces_count() > 0 and moves_count < 16):
        massacre_agent.massacre(game_board,team_white,team_black)
        moves_count += 1
    if (moves_count == 16):
        print("Too many moves! Aborted")
    game_board.print_board() # get rid of this later
