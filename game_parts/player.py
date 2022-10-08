from board import Board
from time import sleep
import os


class Player:
    board = Board()
    state = False

    def __init__(self):
        state = False

    def set_board(self):
        self.board.set_ships()
        sleep(4)
        os.system("cls")

    def recive_bullet(self, bullet):
        self.board.mark_bullet(bullet)
        self.board.print_board()
        if self.board.get_cant_ships() == 0:
            self.state = True
        sleep(4)
        os.system("cls")

    def shoot(self):
        bullet = input("Disparar: ")
        return bullet
        os.system("cls")

    def get_state(self):
        return self.state
