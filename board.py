from piece import Piece, RED, BLUE

class Board():
    def __init__(self):
        self.grid = [[None for square in range(8)] for column in range(8)]
        self.setup_board()

    def setup_board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if i < 3:
                    if not ((i+j) % 2):
                        self.grid[i][j] = Piece(RED)
                if i > 4:
                    if not ((i + j) % 2):
                        self.grid[i][j] = Piece(BLUE)

    def get_piece(self, row, col):
        return self.grid[row][col]


    def move_piece(self, original, destination, piece):
        self.grid[destination[0]][destination[1]] = piece
        self.remove_piece(*original)

        if abs(original[0]-destination[0]) == 2: # Capture handling (moved 2 squares)
            capture_row = (original[0] + destination[0]) // 2
            capture_col = (original[1] + destination[1]) // 2
            self.remove_piece(capture_row, capture_col)

        piece.promote_if_needed(*destination)

    def remove_piece(self, row, col):
        self.grid[row][col] = None


    def in_bounds(self, row, col):
        return (0 <= row < 8) and (0 <= col < 8)

    def get_all_pieces(self, colour):
        pieces = []
        for i in range(0, 8):
            for j in range(0, 8):
                piece_at_location = self.grid[i][j]
                if piece_at_location is not None and piece_at_location.colour == colour:
                    pieces.append((i,j, piece_at_location))

        return pieces