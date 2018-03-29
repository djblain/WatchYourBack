from piece import Piece

class Board:
    # the Board class used in the game

    def __init__(self):
        # initialise board
        self.size = 8
        self.pieces = []

    def resize(self, new_size):
        # TODO for part B: resize the board
        self.size = new_size

    def position_out_of_bounds(self, row, column):
        # check whether a given position is off the board
        if (column < 0):
            return True
        elif (row < 0):
            return True
        elif (column >= self.size):
            return True
        elif (row >= self.size):
            return True
        else:
            return False

    def find_piece(self, row, column):
        # finds the piece located at the given position
        # returns 0 if no such piece exists
        if self.position_out_of_bounds(row, column):
            return -1
        for p in self.pieces:
            if p.get_position() == [row, column]:
                return p
        return None

    def add_piece(self, colour, row, column):
        # adds a new piece to the given location, if it can be placed there
        if (self.position_out_of_bounds(row,column)):
            print("Can't place here, not on the board!")
            return False
        else:
            if self.find_piece(row, column) == None:
                n = Piece(colour, row, column)
                self.pieces.append(n)
                return n
            else:
                print("Piece already here! Can't place!")
                return False


    def remove_piece(self, row, column):
        # removes the piece from the specified position
        p = self.find_piece(row, column)
        if type(p) == Piece:
            self.pieces.remove(p)
        else:
            print('No piece to remove!')

    def get_corners(self):
        #returns a list of the corner pieces (X)
        c = []
        for p in self.pieces:
            if p.colour.capitalize() == 'X':
                c.append(p)
        return c

    def piece_is_surrounded(self, piece):
        [r, c] = piece.get_position()
        c_self = piece.colour.capitalize()
        # check if horizontally surrounded first
        p_left = self.find_piece(r, c-1) # piece to the left
        p_right = self.find_piece(r, c+1) # piece to the right
        if type(p_left) == Piece and type(p_right) == Piece:
            c_left = p_left.colour.capitalize()
            c_right = p_right.colour.capitalize()
            if c_left!=c_self and c_right!=c_self:
                return True
        # check if vertically surrounded
        p_up = self.find_piece(r-1, c) # piece above
        p_down = self.find_piece(r+1, c) # piece below
        if type(p_up) == Piece and type(p_down) == Piece:
            c_up = p_up.colour.capitalize()
            c_down = p_down.colour.capitalize()
            if c_up!=c_self and c_down!=c_self:
                return True
        # not surrounded
        return False

    def position_safe(self, colour, row, column):
        #checks whether a position is safe for a piece of a given colour
        piece_temp = Piece(colour, row, column)
        if (piece_is_surrounded(piece_temp)):
            return False
        else:
            return True

    def piece_can_move(self, piece, r_move, c_move):
        # checks whether the indicated piece can move to a new position
        # r_move and c_move are relative to current position
        [r, c] = piece.get_position()
        if self.position_out_of_bounds(r + r_move, c + c_move):
            return False
        else:
            if self.find_piece(r + r_move, c + c_move) == None:
                return True
            else:
                return False

    def piece_move_towards(self, piece, dest_row, dest_col):
        # move a piece towards a certain position
        if self.position_out_of_bounds(dest_row, dest_col):
            return
        else:
            return

    def pieces_eliminate(self,colour_last):
        #eliminates surrounded pieces
        #remove pieces not of colour == colour_last
        for p in self.pieces:
            if self.piece_is_surrounded(p) and p.colour != colour_last:
                self.pieces.remove(p)
        #remove pieces regardless of colour
        for p in self.pieces:
            if self.piece_is_surrounded(p):
                self.pieces.remove(p)

    def print_board(self):
        # print the board row-by-row
        for x in range(self.size):
            str = "" # line string
            for y in range(self.size):
                s = self.find_piece(x, y)
                # choose appropriate symbol
                if type(s) == Piece:
                    if s.colour.capitalize() == "Black":
                        str = str + '@'
                    elif s.colour.capitalize() == "White":
                        str = str + 'O'
                    elif s.colour.capitalize() == "X":
                        str = str + 'X'
                else:
                    str = str + '-'
                # add spaces between symbols
                if y < self.size-1:
                    str = str + " "
            print(str)
