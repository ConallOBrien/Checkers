from board import Board
from piece import RED, BLUE

PLAYER_1_PIECE = "🔴"
PLAYER_2_PIECE = "🔵"
EMPTY_SQUARE = "⚫"

class UserInterface():
    def __init__(self):
        pass

    def show_board(self, board, side=RED):
        if side == RED:
            direction = -1
        else:
            direction = 1
        indexes = (0, 1, 2, 3, 4, 5, 6, 7)
        for i in indexes[::direction]:
            for j in indexes[:: -direction]:
                self.show_square(board, i, j)
            print()

        print(("a   b  c  d  e   f  g  h", "h   g  f  e  d   c  b  a")[side])


    def show_square(self, board, row, col):
        if board.get_piece_colour(row, col) is None:
            print(EMPTY_SQUARE, end=" ")
        elif (board.get_piece_colour(row, col) == RED):
            print(PLAYER_1_PIECE, end=" ")
        elif (board.get_piece_colour(row, col) == BLUE):
            print(PLAYER_2_PIECE, end=" ")
