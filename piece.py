
class Piece:
    # the Piece class used in the game

    def __init__(self, colour, row, column):
        # initialise a piece with given values
        self.colour = colour
        self.row = row
        self.column = column

    def get_position(self):
        # returns the position of the piece
        return [self.row, self.column]

    def set_position(self, new_row, new_column):
        # puts the piece in a new position
        self.row = new_row
        self.column = new_column

    def is_adjacent(self, other_piece):
        # checks whether another piece is adjacent to this piece
        my_pos = self.get_position()
        other_pos = other_piece.get_position()
        row_diff = abs(my_pos[0] - other_pos[0])    #row difference
        col_diff = abs(my_pos[1] - other_pos[1])    #column difference
        #two pieces are adjacent iff the positional difference is exactly 1
        if row_diff + col_diff == 1:
            return True
        return False

    def position_distance(self, row, column):
        #returns this piece's distance to an indicated position
        [my_row, my_column] = self.get_position()
        return abs(my_row - row) + abs(my_column - column)

    def distance_nearest(self, pieces_check):
        #returns the distance to the nearest piece in pieces_check
        dist = -1
        for p in pieces_check:
            if p != self:
                [r,c] = p.get_position()
                dist = min(dist, self.position_distance(r,c))
        return dist
