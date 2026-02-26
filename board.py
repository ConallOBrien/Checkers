from constants import PLAYER_1, PLAYER_2, BOARD_WIDTH, BOARD_HEIGHT
from piece import Piece

class Board:
    def __init__(self):
        self.grid: list[list[Piece | None]] = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.setup_board()

    def setup_board(self):
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                if i < 3:
                    if not ((i+j) % 2):
                        self.grid[i][j] = Piece(PLAYER_1)
                if i > 4:
                    if not ((i + j) % 2):
                        self.grid[i][j] = Piece(PLAYER_2)

    def get_piece(self, row, col):
        return self.grid[row][col]


    def move_piece(self, original, destination):
        piece = self.get_piece(*original)
        self.grid[destination[0]][destination[1]] = piece
        self.remove_piece(*original)

        if abs(original[0]-destination[0]) == 2: # Capture handling (moved 2 squares)
            capture_row = (original[0] + destination[0]) // 2
            capture_col = (original[1] + destination[1]) // 2
            self.remove_piece(capture_row, capture_col)

        piece.promote_if_needed(destination[0])

    def remove_piece(self, row, col):
        self.grid[row][col] = None


    @staticmethod
    def in_bounds(row, col):
        return (0 <= row < BOARD_WIDTH) and (0 <= col < BOARD_HEIGHT)

    def get_all_pieces(self, colour):
        pieces = []
        for i in range(0, 8):
            for j in range(0, 8):
                piece_at_location = self.grid[i][j]
                if piece_at_location is not None and piece_at_location.colour == colour:
                    pieces.append((i,j, piece_at_location))

        return pieces

    def get_piece_colour(self, row, col):
        if self.get_piece(row, col) is not None:
            return self.get_piece(row, col).colour
        else:
            return None