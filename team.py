from board import Board
from piece import Piece

class Team:
    # the Team class for the game

    def __init__(self, colour, board, human):
        # initialises the team with the given values
        self.colour = colour            # Team colour
        self.to_place = 12              # Pieces left to place
        self.game_board = board         # Board which the game is played on
        self.human = human              # Whether this team is human controlled

    def get_my_pieces(self):
        # returns a list of pieces of the same colour
        pieces = []
        for p in self.game_board.pieces:
            if p.colour.capitalize() == self.colour.capitalize():
                pieces.append(p)
        return pieces

    def get_other_pieces(self):
        # returns a list of pieces not of the same colour
        pieces = []
        for p in self.game_board.pieces:
            if p.colour.capitalize() != self.colour.capitalize():
                pieces.append(p)
        return pieces

    def pieces_count(self):
        # returns the number of pieces
        return len(self.get_my_pieces())

    def take_turn(self):
        # Return True if turn valid, False otherwise
        # Do nothing for now, implement for part B
        return True
