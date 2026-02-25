from game import Game
from ui import UserInterface


def main():
    game = Game()
    UI = UserInterface()
    print(game.generate_moves())
    UI.show_board(game.board, 1)


if __name__ == "__main__":
    main()