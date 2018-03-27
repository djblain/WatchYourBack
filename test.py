### Exists for testing purposes

from board import Board
from team import Team

game_board = Board()

team_white = Team("White", game_board, True)
team_black = Team("Black", game_board, False)

print(game_board.size)

print('\n')
game_board.print_board()
print('\n')

game_board.add_piece("black", 2, 5)
game_board.add_piece("white", 3, 4)
game_board.add_piece("black", 3, 4)
game_board.add_piece("white", 0, 8)

print('\n')
game_board.print_board()
print('\n')

game_board.remove_piece(3, 4)

print('\n')
game_board.print_board()
print('\n')

print('White pieces: ' + str(team_white.pieces_count()))
print('Black pieces: ' + str(team_black.pieces_count()))
