from piece import RED, BLUE
from board import Board

class Game:
    def __init__(self, starting_player = RED):
        self.board = Board()
        self.current_player = starting_player

    def generate_moves(self):
        moves = []
        player_pieces = self.board.get_all_pieces(self.current_player)
        for piece in player_pieces:
            location = (piece[0], piece[1])
            current_piece = piece[2]
            current_moves = current_piece.get_valid_moves(self.board, location)
            if len(current_moves[1]):
                moves.append(current_moves)


        if any(move[0] for move in moves):  # Only allow captures if capture possible
            moves = [move for move in moves if move[0]]
        return moves