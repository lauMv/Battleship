from colorclass import Color


def get_row(position):
    file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    pos = file.index(position[0])
    return int(pos)


class Board:
    board = []
    ships = 5
    aircraft_carrier = 1
    battleship = 1
    cruise = 1
    submarine = 1
    destructor = 1

    def __init__(self):
        pass

    def create_board(self):
        self.board = []
        for x in range(10):
            row = []
            for y in range(10):
                row.append([" ", False])
            self.board.append(row)

    def print_board(self):
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
                if elem[1]:
                    print(Color('{autored}'+elem[0]+'{/red}') + " |", end=" ")
                else:
                    print(elem[0] + " |", end=" ")
            print('\n')
            col = col+1

    def save_ship_positions(self, initial_position,  final_position):
        pos_init_y, pos_final_y = get_row(initial_position), get_row(final_position)
        pos_init_x, pos_final_x = int(initial_position[1:]) - 1, int(final_position[1:]) - 1

        if pos_init_y == pos_final_y:
            index = pos_init_x
            for elem in range(pos_init_x, pos_final_x+1):
                if self.board[index][pos_init_y][0] == " ":
                    self.board[index][pos_init_y][0] = "X"
                    index = index + 1
                else:
                    print("La posicion del barco choca con otra")

        if pos_init_x == pos_final_x:
            index = pos_init_y
            for elem in range(pos_init_y, pos_final_y+1):
                if self.board[pos_init_x][index][0] == " ":
                    self.board[pos_init_x][index][0] = 'X'
                    index = index + 1
                else:
                    print("La posicion del barco choca con otra")

    def set_ships(self):
        print("Seleccionar posicion inicial para el porta aviones (5 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7)")
        print("Seleccionar posicion final")
        final_position = input("Posicion final")
        self.save_ship_positions(initial_position, final_position)
        self.print_board()

        # print("Seleccionar posicion inicial para el acorazado (4 casillas): ")
        # initial_position = input("Posicion inicial (Ej: A7)")
        # print("Seleccionar posicion final")
        # final_position = input("Posicion final")
        # self.save_ship_positions(initial_position, final_position)
        # self.print_board()
        #
        # print("Seleccionar posicion inicial para el crucero (3 casillas): ")
        # initial_position = input("Posicion inicial (Ej: A7)")
        # print("Seleccionar posicion final")
        # final_position = input("Posicion final")
        # self.save_ship_positions(initial_position, final_position)
        # self.print_board()

        # print("Seleccionar posicion inicial para el submarino (3 casillas): ")
        # initial_position = input("Posicion inicial (Ej: A7)")
        # print("Seleccionar posicion final")
        # final_position = input("Posicion final")
        # self.save_ship_positions(initial_position, final_position)
        # self.print_board()
        #
        # print("Seleccionar posicion inicial para el destructor (2 casillas): ")
        # initial_position = input("Posicion inicial (Ej: A7)")
        # print("Seleccionar posicion final")
        # final_position = input("Posicion final")
        # self.save_ship_positions(initial_position, final_position)
        # self.print_board()

    def mark_bullet(self, pos):
        pos_y = get_row(pos)
        pos_x = int(pos[1:])
        if self.board[pos_x][pos_y][0] == " ":
            self.board[pos_x][pos_y][0] = "."
            self.board[pos_x][pos_y][1] = True
        else:
            self.board[pos_x][pos_y][1] = True


if __name__ == '__main__':
    board = Board()
    board.create_board()
    board.print_board()
    board.set_ships()
    board.mark_bullet("a1")
    board.print_board()
    board.mark_bullet("b1")
    board.print_board()
    print(board.board)
