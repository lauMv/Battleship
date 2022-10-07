from board import Board
from time import sleep
import os


class Player:
    board = Board()

    def __init__(self):
        pass

    def set_board(self):
        self.board.set_ships()
        sleep(4)
        os.system("cls")

    def recive_bullet(self, bullet):
        self.board.mark_bullet(bullet)
        sleep(4)
        os.system("cls")

    def shoot(self):
        bullet = input("Disparar: ")
        return bullet
        os.system("cls")

    def show_board(self):
        self.board.print_board()
        sleep(4)
        os.system("cls")


if __name__ == '__main__':

    player1 = Player()
    player2 = Player()

    player1.set_board()
    player2.set_board()
