from game import Game
from ui import UserInterface


def main():
    game = Game()
    ui = UserInterface(game)
    ui.run()



if __name__ == "__main__":
    main()