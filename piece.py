class Piece:
    def __init__(self, colour):
        self.colour = colour        # PLAYER_1 or PLAYER_2
        self.is_king = False    # True if piece is a king


    def get_valid_moves(self, board, position):
        capture = False
        valid = []
        direction = (1, -1)[self.colour]
        x, y = (position[0], position[1])

        destinations = ((x+2 * direction, y+2),(x+2 * direction, y-2),(x-2 * direction, y+2),(x-2 * direction, y-2), # for first 4, captured piece in i+4
                        (x+1 * direction, y+1),(x+1 * direction, y-1),(x-1 * direction, y+1),(x-1 * direction, y-1)) # first 2 go forward, next 2 are corresponding reverse for kings

        for i in range(2):
            if board.in_bounds(*destinations[i]):
                if board.get_piece(*destinations[i]) is None:
                    if board.get_piece(*destinations[i+4]) is not None and board.get_piece(*destinations[i+4]).colour != self.colour:
                        capture = True
                        valid.append(destinations[i])

            if self.is_king:
                if board.in_bounds(*destinations[i+2]):
                    if board.get_piece(*destinations[i + 2]) is None:
                        if board.get_piece(*destinations[i + 6]) is not None and board.get_piece(
                                *destinations[i + 6]).colour != self.colour:
                            capture = True
                            valid.append(destinations[i+2])

        if not capture:
            for i in range(4, 6):
                if board.in_bounds(*destinations[i]):
                    if board.get_piece(*destinations[i]) is None:
                        valid.append(destinations[i])

                if self.is_king:
                    if board.in_bounds(*destinations[i+2]):
                        if board.get_piece(*destinations[i + 2]) is None:
                            valid.append(destinations[i+2])

        return capture, valid

    def promote_if_needed(self, row):
        if row == 7 - (7*self.colour):
            self.is_king = True
        return