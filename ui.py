from constants import *
import pygame

""" 
PLAYER_1 = 0
PLAYER_2 = 1

BOARD_WIDTH = 8
BOARD_HEIGHT = 8

SQUARE_SIZE = 70

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
"""

PLAYER_1_PIECE = "🔴"
PLAYER_2_PIECE = "🔵"
EMPTY_SQUARE = "⚫"

class UserInterface:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.load_surfaces()
        self.calculate_borders()
        self.current_selection = None
        self.running = True
        self.show_board()

    def show_board(self):
        board = self.game.board
        side = self.game.current_player
        if side == PLAYER_1:
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
        elif board.get_piece_colour(row, col) == PLAYER_1:
            print(PLAYER_1_PIECE, end=" ")
        elif board.get_piece_colour(row, col) == PLAYER_2:
            print(PLAYER_2_PIECE, end=" ")

    def draw_board(self):
        self.screen.fill((20, 80, 10))
        self.screen.blit(self.blank_board_surface, (self.x_offset, self.y_offset))
        if self.current_selection is not None:
            self.screen.blit(self.selected_square_surface, (self.x_offset + (SQUARE_SIZE * self.current_selection[1]), self.y_offset + (SQUARE_SIZE * (BOARD_HEIGHT - 1 - self.current_selection[0]))))

        for piece_details in self.game.find_all_piece_details():
            if piece_details[0] == PLAYER_1:
                self.screen.blit(self.p1_piece_surface,
                                 (self.x_offset + (SQUARE_SIZE * piece_details[2][1]),
                                  self.y_offset + (SQUARE_SIZE * (BOARD_HEIGHT - 1 - piece_details[2][0]))))
            else:
                self.screen.blit(self.p2_piece_surface,
                                 (self.x_offset + (SQUARE_SIZE * piece_details[2][1]),
                                  self.y_offset + (SQUARE_SIZE * (BOARD_HEIGHT - 1 - piece_details[2][0]))))

            if piece_details[1]:
                self.screen.blit(self.king_surface,
                                 (self.x_offset + (SQUARE_SIZE * piece_details[2][1]),
                                  self.y_offset + (SQUARE_SIZE * (BOARD_HEIGHT - 1 - piece_details[2][0]))))



    def run(self):
        """
        self.show_board()
        while self.game.check_win_condition() is None:
            try:
                input_move = input("Enter your move: ")
                location1 = (int(input_move[1]) - 1, ord(input_move[0]) - ord('a'))
                location2 = (int(input_move[5]) - 1, ord(input_move[4]) - ord('a'))

                if not self.game.valid_position(*location1) or not self.game.valid_position(*location2):
                    raise Exception


                outcome = self.game.handle_move(location1, location2)
                if not outcome:
                    raise Exception


                self.show_board()

            except:
                print("Invalid move")
        """

        while self.game.check_win_condition() is None and self.running == True:
            self.event_handler()
            self.draw_board()
            pygame.display.flip()
            self.clock.tick(30)

    def load_surfaces(self):
        self.p1_piece_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.p1_piece_surface, (255, 0, 0), (SQUARE_SIZE // 2, SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
        self.p2_piece_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.p2_piece_surface, (0, 0, 255), (SQUARE_SIZE // 2, SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
        self.king_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.king_surface, (220, 170, 0), (SQUARE_SIZE // 2, SQUARE_SIZE // 2), 5)
        self.load_blank_board()
        self.selected_square_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
        self.selected_square_surface.fill((255, 255, 255))


    def load_blank_board(self):
        self.blank_board_surface = pygame.Surface((SQUARE_SIZE*8, SQUARE_SIZE*8), pygame.SRCALPHA)
        self.blank_board_surface.fill((190, 135, 75))

        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                if (i+j) % 2:
                    pygame.draw.rect(self.blank_board_surface, (100, 70, 35), (pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)))


    def calculate_borders(self):
        self.x_offset = (WINDOW_WIDTH - (SQUARE_SIZE * BOARD_WIDTH)) // 2
        self.y_offset = (WINDOW_HEIGHT - (SQUARE_SIZE * BOARD_HEIGHT)) // 2

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.on_board(pos):
                    square = self.get_clicked_square(pos)
                    if self.current_selection is None:
                        if self.valid_piece_location(square):
                            self.current_selection = square
                    else:
                        if square == self.current_selection:
                            self.current_selection = None
                        else:
                            self.game.handle_move(self.current_selection, square)
                            self.current_selection = None


    def on_board(self, position):
        if self.x_offset <= position[0] <= WINDOW_WIDTH - self.x_offset:
            if self.y_offset <= position[1] <= WINDOW_HEIGHT - self.y_offset:
                return True
        return False

    def get_clicked_square(self, position):
        x_position = (position[0] - self.x_offset) // SQUARE_SIZE
        y_position = (position[1] - self.y_offset) // SQUARE_SIZE
        y_position = BOARD_HEIGHT - 1 - y_position
        print(y_position, x_position )
        return y_position, x_position

    def valid_piece_location(self, square):
        return self.game.player_piece_at(*square)
