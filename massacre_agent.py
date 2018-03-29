# functions which perform the massacre action

from board import Board
from team import Team
from piece import Piece

state_previous = Board()

def board_assess_minimax(g_board,t_attack,t_defend,depth):
    # assess by performing minimax
    # better if can kill, worse if gets killed
    dir_check = [[0,1],[-1,0],[0,-1],[1,0]]
    ally_begin = t_attack.pieces_count()
    enemy_begin = t_defend.pieces_count()
    if depth > 0 and enemy_begin > 0:
        s_max = -1000
        for d in dir_check:
            for p in t_attack.get_my_pieces():
                new_pos = [-1,-1]
                p_pos = p.get_position()
                if g_board.piece_can_move(p,d[0],d[1]):
                    new_pos = [p_pos[0]+d[0],p_pos[1]+d[1]]
                elif g_board.piece_can_move(p,d[0]*2,d[1]*2):
                    new_pos = [p_pos[0]+d[0]*2,p_pos[1]+d[1]*2]
                if not g_board.position_out_of_bounds(new_pos[0],new_pos[1]):
                    n_board = Board()
                    n_attack = Team(t_attack.colour,n_board,False)
                    n_defend = Team(t_defend.colour,n_board,False)
                    for c in g_board.pieces:
                        if c != p:
                            n_board.add_piece(c.colour,c.row,c.column)
                        else:
                            n_board.add_piece(p.colour,new_pos[0],new_pos[1])
                    n_board.pieces_eliminate(t_attack.colour)
                    ally_end = n_attack.pieces_count()
                    enemy_end = n_defend.pieces_count()
                    n_score = ally_end - ally_begin
                    n_score += enemy_begin - enemy_end
                    n_score += board_assess_minimax(n_board,n_attack,
                                                   n_defend,depth-1)
                    s_max = max(n_score,s_max)
        return s_max
    else:
        return 0


def massacre(g_board,t_attack,t_defend):
    # TODO: massacre function
    # directions to check for adjacent pieces, movement, etc.
    dir_check = [[0,1],[-1,0],[0,-1],[1,0]]
    # try to find positions to move to which surround an enemy
    s_max = -1000
    p_move = 0
    d_move = [0,0]
    ally_begin = t_attack.pieces_count()
    enemy_begin = t_defend.pieces_count()
    depth_limit = 2
    ally_pieces = t_attack.get_my_pieces()
    enemy_pieces = t_defend.get_my_pieces()
    full_break = False
    for d in dir_check:
        if full_break:
            break
        print(d)
        for p in t_attack.get_my_pieces():
            new_pos = [-1,-1]
            p_pos = p.get_position()
            if g_board.piece_can_move(p,d[0],d[1]):
                new_pos = [p_pos[0]+d[0],p_pos[1]+d[1]]
            elif g_board.piece_can_move(p,d[0]*2,d[1]*2):
                new_pos = [p_pos[0]+d[0]*2,p_pos[1]+d[1]*2]
            if not g_board.position_out_of_bounds(new_pos[0],new_pos[1]):
                n_board = Board()
                n_attack = Team(t_attack.colour,n_board,False)
                n_defend = Team(t_defend.colour,n_board,False)
                for c in g_board.pieces:
                    if c != p:
                        n_board.add_piece(c.colour,c.row,c.column)
                    else:
                        n_board.add_piece(c.colour,new_pos[0],new_pos[1])
                n_board.pieces_eliminate(t_attack.colour)
                ally_end = n_attack.pieces_count()
                enemy_end = n_defend.pieces_count()
                n_score = ally_end - ally_begin
                n_score += enemy_begin - enemy_end
                n_score += board_assess_minimax(n_board,n_attack,
                                                n_defend,depth_limit)
                if n_score > s_max:
                    s_max = n_score
                    p_move = p
                    d_move = d
                if enemy_end == 0 or n_score > 0:
                    full_break = True
                    break
    print(s_max)
    if s_max < 0:
        dist = 1000
        for p in ally_pieces:
            e = p.find_nearest(enemy_pieces)
            if e != None:
                for d in dir_check:
                    e_pos = e.get_position()
                    new_pos = [-1,-1]
                    p_pos = p.get_position()
                    if g_board.piece_can_move(p,d[0],d[1]):
                        new_pos = [p_pos[0]+d[0],p_pos[1]+d[1]]
                    elif g_board.piece_can_move(p,d[0]*2,d[1]*2):
                        new_pos = [p_pos[0]+d[0]*2,p_pos[1]+d[1]*2]
                    if not g_board.position_out_of_bounds(
                        new_pos[0],
                        new_pos[1]):
                        d_current = abs(e_pos[0]-p_pos[0])
                        d_current += abs(e_pos[1]-p_pos[1])
                        d_new = abs(e_pos[0]-new_pos[0])
                        d_new += abs(e_pos[1]-new_pos[1])
                        if d_new < dist and d_current > 1:
                            p_move = p
                            d_move = d
                            dist = d_new
    if p_move != 0:
        str_out = '(' + str(p_move.row) + ' ,' + str(p_move.column) + ')'
        pos = p_move.get_position()
        if g_board.piece_can_move(p_move,d_move[0],d_move[1]):
            p_move.set_position(pos[0]+d_move[0],pos[1]+d_move[1])
        elif g_board.piece_can_move(p_move,d_move[0]*2,d_move[1]*2):
            p_move.set_position(pos[0]+d_move[0]*2,pos[1]+d_move[1]*2)
        g_board.pieces_eliminate(t_attack.colour)
        str_out += ' -> '
        str_out += '(' + str(p_move.row) + ' ,' + str(p_move.column) + ')'
        print(str_out)
