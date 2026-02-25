from constants import RED, BLUE, BOARDWIDTH, BOARDHEIGHT

PLAYER_1_PIECE = "🔴"
PLAYER_2_PIECE = "🔵"
EMPTY_SQUARE = "⚫"

class UserInterface():
    def __init__(self, game):
        self.game = game

    def show_board(self):
        board = self.game.board
        side = self.game.current_player
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


    def run(self):
        self.show_board()
        while self.game.check_win_condition() is None:
            try:
                inputMove = input("Enter your move: ")
                location1 = (int(inputMove[1]) - 1, ord(inputMove[0]) - ord('a'))
                location2 = (int(inputMove[5]) - 1, ord(inputMove[4]) - ord('a'))

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

