
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
        
    
