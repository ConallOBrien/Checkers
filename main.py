from game import Game
from ui import UserInterface


def main():
    for i in range(1):
        game = Game()
        ui = UserInterface(game)
        ui.single_player_run()


if __name__ == "__main__":
    main()