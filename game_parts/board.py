from colorclass import Color
from box import Box
import os


def get_row(position):
    file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    pos = file.index(position[0])
    return int(pos)


class Board:
    board = []
    ships = 5
    ships_sunks = 0
    aircraft_carrier = 1
    ships_positions = []

    def __init__(self):
        for x in range(10):
            row = []
            for y in range(10):
                box = Box()
                row.append(box)
            self.board.append(row)

    def get_ships_positions(self):
        return self.ships_positions

    def get_cant_ships(self):
        return self.ships

    def print_board(self):
        self.send_sunk_message()
        col = 1
        file_names = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for elem in file_names:
            print(" " + elem + " ", end=" ")
        print("\n")

        for row in self.board:

            if col != 10:
                print(str(col) + "  | ", end="")
            else:
                print(str(col) + " | ", end="")

            for elem in row:
                if elem.get_state():
                    print(Color('{autored}'+elem.get_cont()+'{/red}') + " |", end=" ")
                else:
                    print(elem.get_cont() + " |", end=" ")
            print('\n')
            col = col+1

    def save_ship_positions(self, initial_position,  final_position):
        pos_init_y, pos_final_y = get_row(initial_position), get_row(final_position)
        pos_init_x, pos_final_x = int(initial_position[1:]) - 1, int(final_position[1:]) - 1
        coordinates = []
        if pos_init_y == pos_final_y:
            index = pos_init_x
            for elem in range(pos_init_x, pos_final_x+1):
                if self.board[index][pos_init_y].get_cont() == " ":
                    self.board[index][pos_init_y].set_cont("X")
                    self.board[index][pos_init_y].set_pos(index, pos_final_y)
                    elem = [index, pos_final_y]
                    index += 1
                else:
                    print("La posicion del barco choca con otra")
                coordinates.append(elem)

        if pos_init_x == pos_final_x:
            index = pos_init_y
            for elem in range(pos_init_y, pos_final_y+1):
                if self.board[pos_init_x][index].get_cont() == " ":
                    self.board[pos_init_x][index].set_cont("X")
                    self.board[pos_init_x][index].set_pos(pos_init_x, index)
                    elem = [pos_init_x, index]
                    index = index + 1
                else:
                    print("La posicion del barco choca con otra")
                coordinates.append(elem)
        self.ships_positions.append(coordinates)

    def set_ships(self):
        print("Seleccionar posicion inicial para el porta aviones (5 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7): ")
        print("Seleccionar posicion final: ")
        final_position = input("Posicion final: ")
        if self.validate_ship_size(initial_position, final_position, 5):
            self.save_ship_positions(initial_position, final_position)
            self.print_board()

        print("Seleccionar posicion inicial para el acorazado (4 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7): ")
        print("Seleccionar posicion final: ")
        final_position = input("Posicion final: ")
        if self.validate_ship_size(initial_position, final_position, 4):
            self.save_ship_positions(initial_position, final_position)
            self.print_board()

        print("Seleccionar posicion inicial para el crucero (3 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7): ")
        print("Seleccionar posicion final: ")
        final_position = input("Posicion final: ")
        if self.validate_ship_size(initial_position, final_position, 3):
            self.save_ship_positions(initial_position, final_position)
            self.print_board()

        print("Seleccionar posicion inicial para el submarino (3 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7): ")
        print("Seleccionar posicion final: ")
        final_position = input("Posicion final: ")
        if self.validate_ship_size(initial_position, final_position, 3):
            self.save_ship_positions(initial_position, final_position)
            self.print_board()

        print("Seleccionar posicion inicial para el destructor (2 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7): ")
        print("Seleccionar posicion final: ")
        final_position = input("Posicion final: ")
        if self.validate_ship_size(initial_position, final_position, 2):
            self.save_ship_positions(initial_position, final_position)
            self.print_board()

    def mark_bullet(self, pos):
        pos_y = get_row(pos)
        pos_x = int(pos[1:])-1
        if self.board[pos_x][pos_y].get_cont() == " ":
            self.board[pos_x][pos_y].set_cont(".")
            self.board[pos_x][pos_y].change_state()
        else:
            self.board[pos_x][pos_y].change_state()

    def send_sunk_message(self):
        if self.check_sunk_ship() > self.ships_sunks:
            os.system("cls")
            print(Color('{autored}' + "Barco Hundido!!" + '{/red}'))
            self.ships_sunks += 1

    def check_sunk_ship(self):
        ships_sunk = 0
        for ship in self.ships_positions:
            is_sunk = 0
            for pos in ship:
                if self.board[pos[0]][pos[1]].get_state():
                    is_sunk += 1
            if is_sunk == len(ship):
                self.ships -= 1
                ships_sunk += 1
        return ships_sunk

    def validate_ship_size(self, initial_position, final_position, len):
        pos_x_init, pos_x_final = int(initial_position[1:]) - 1, int(final_position[1:]) - 1
        pos_y_init, pos_y_final = get_row(initial_position), get_row(final_position)
        if pos_x_init == pos_x_final:
            if pos_y_final - pos_y_init == len-1:
                return True
        elif pos_y_init == pos_y_final:
            if pos_x_final - pos_x_init == len-1:
                return True
        return False
