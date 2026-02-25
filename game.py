from constants import RED, BLUE
from board import Board

class Game:
    def __init__(self, starting_player = RED):
        self.board = Board()
        self.current_player = starting_player
        self.previous_jump = None

    def generate_moves(self, colour = None):
        if colour is None:
            colour = self.current_player
        moves = []

        if self.previous_jump is not None:
            second_jumps = self.check_for_double()
            moves.append(second_jumps)

        else:
            player_pieces = self.board.get_all_pieces(colour)
            for piece in player_pieces:
                location = (piece[0], piece[1])
                current_piece = piece[2]
                current_moves = current_piece.get_valid_moves(self.board, location)
                if len(current_moves[1]):
                    moves.append(current_moves)


            if any(move[0] for move in moves):  # Only allow captures if capture possible
                moves = [move for move in moves if move[0]]

        return moves

    def handle_move(self, start, end):
        avalable_moves = self.generate_moves()
        if any((move[1] == start and move[2] == end) for move in avalable_moves):
            self.apply_move(start, end)
            if abs(start[0]-end[0]) == 2:
                if self.check_for_double() is not None:
                    self.previous_jump = end
                    return True

            self.switch_turn() # Doesn't run if double jump available
            return True

        else:
            return False




    def apply_move(self, start, end):
        self.previous_jump = None
        self.board.move_piece(start, end)


    def switch_turn(self):
        self.previous_jump = None
        if self.current_player == RED:
            self.current_player = BLUE
        else:
            self.current_player = RED

    def valid_position(self, row, col):
        return self.board.in_bounds(row, col)


    def check_win_condition(self):
        if len(self.board.get_all_pieces(RED)) == 0 or len(self.generate_moves(RED)) == 0:
            return BLUE
        elif len(self.board.get_all_pieces(BLUE)) == 0 or len(self.generate_moves(BLUE)) == 0:
            return RED
        return None

    def check_for_double(self):
        previous_piece = self.board.get_piece(*self.previous_jump)
        possible_moves = previous_piece.get_valid_moves(self.board, self.previous_jump)
        if len(possible_moves[1]) and possible_moves[0]:  # Check for available captures from piece that jumped
            return possible_moves
        return None

