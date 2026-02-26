from constants import RED, BLUE, BOARD_WIDTH, BOARD_HEIGHT

PLAYER_1_PIECE = "🔴"
PLAYER_2_PIECE = "🔵"
EMPTY_SQUARE = "⚫"

class UserInterface:
    def __init__(self, game):
        self.game = game

    def show_board(self):
        board = self.game.board
        side = self.game.current_player
        if side == RED:
            direction = -1
        else:
            direction = 1
        for i in range(BOARD_HEIGHT)[::direction]:
            for j in range(BOARD_WIDTH)[::-direction]:
                self.show_square(board, i, j)
            print()

        print(("a   b  c  d  e   f  g  h", "h   g  f  e  d   c  b  a")[side])


    @staticmethod
    def show_square(board, row, col):
        if board.get_piece_colour(row, col) is None:
            print(EMPTY_SQUARE, end=" ")
        elif board.get_piece_colour(row, col) == RED:
            print(PLAYER_1_PIECE, end=" ")
        elif board.get_piece_colour(row, col) == BLUE:
            print(PLAYER_2_PIECE, end=" ")


    def run(self):
        self.show_board()
        while self.game.check_win_condition() is None:
            try:
                input_move = input("Enter your move: ")
                location1 = (int(input_move[1]) - 1, ord(input_move[0]) - ord('a'))
                location2 = (int(input_move[5]) - 1, ord(input_move[4]) - ord('a'))

                print(location1, location2)
                if not self.game.valid_position(*location1) or not self.game.valid_position(*location2):
                    print("Error 1")
                    raise Exception


                outcome = self.game.handle_move(location1, location2)
                if not outcome:
                    print("Error 2")
                    raise Exception


                self.show_board()





            except:
                print("Invalid move")

