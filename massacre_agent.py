# functions which perform the massacre action

from board import Board
from team import Team
from piece import Piece

def massacre(g_board,t_attack,t_defend):
    # TODO: massacre function
    # directions to check for adjacent pieces, movement, etc.
    dir_check = [[0,1],[-1,0],[0,-1],[1,0]]
    pieces_enemy = t_defend.get_other_pieces()      # enemy pieces
    pieces_ally = t_attack.get_my_pieces()          # my pieces
    corners = g_board.get_corners()                 # corners
    p_adjacent = 0      # a piece adjacent to an enemy (if one exists)
    p_surround = 0      # a piece to surround
    p_move = 0          # a piece chosen to move (nearest)
    dist_nearest = -1   # dist of p_move to surround enemy
    for e in pieces_enemy:
        for a in pieces_ally:
            if e.is_adjacent(a):
                p_adjacent = a
                p_surround = e
    #if type(p_adjacent) == Piece:
        #
    g_board.pieces_eliminate(t_attack.colour)
    print("Not done yet!")
