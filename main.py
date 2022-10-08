from game_parts.board import Board
from time import sleep
import os
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    board.print_board()
    board.set_ships()

    board.recive_shot
    sleep(4)
    os.system("cls")

    # board2 = Board()
    # board2.print_board()
    # board2.set_ships()
    #
    # sleep(4)
    # os.system("cls")
    print(board.get_ships_positions())
    print(board.get_cant_ships)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
