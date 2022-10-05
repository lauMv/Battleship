

class Board:
    board = []
    ships = 5
    aircraft_carrier = 1
    battleship = 1
    cruise = 1
    submarine = 1
    destructor = 1

    def create_board(self):
        for x in range(10):
            self.board.append([" "]*10)

    def print_board(self):
        col = 1
        file_names = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for elem in file_names:
            print(" " + elem + " ", end=" ")
        print("\n")
        for file in self.board:
            if col != 10:
                print(str(col) + "  | ", end="")
            else:
                print(str(col) + " | ", end="")
            for elem in file:
                print(elem + " |", end=" ")
            print('\n')
            col = col+1

    def save_positions( self, initial_position,  final_position):
        file = ['a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        pos_init, pos_final = 0, 0
        if initial_position[0] in file:
            pos_init = file.index(initial_position[0])
        if final_position[0] in file:
            pos_final = file.index(final_position[0])
        if pos_init == pos_final:
            for elem in range(int(initial_position[1:])-1, int(final_position[1:])):
                print("pos= ", self.board[elem][pos_init])
                if self.board[elem][pos_init] == " ":
                    self.board[elem][pos_init] = 'X'
                else:
                    print("La posicion del barco choca con otra")
        if initial_position[1:] == final_position[1:]:
            for elem in range(pos_init, pos_final+1):
                if self.board[int(initial_position[1:])-1][elem] == " ":
                    self.board[int(initial_position[1:])-1][elem] = 'X'
                else:
                    print("La posicion del barco choca con otra")

    def set_ships(self):
        print("Seleccionar posicion inicial para el porta aviones (5 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7)")
        print("Seleccionar posicion final")
        final_position = input("Posicion final")
        self.save_positions(initial_position, final_position)
        self.print_board()

        print("Seleccionar posicion inicial para el acorazado (4 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7)")
        print("Seleccionar posicion final")
        final_position = input("Posicion final")
        self.save_positions(initial_position, final_position)
        self.print_board()

        print("Seleccionar posicion inicial para el crucero (3 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7)")
        print("Seleccionar posicion final")
        final_position = input("Posicion final")
        self.save_positions(initial_position, final_position)
        self.print_board()

        print("Seleccionar posicion inicial para el submarino (3 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7)")
        print("Seleccionar posicion final")
        final_position = input("Posicion final")
        self.save_positions(initial_position, final_position)
        self.print_board()

        print("Seleccionar posicion inicial para el destructor (2 casillas): ")
        initial_position = input("Posicion inicial (Ej: A7)")
        print("Seleccionar posicion final")
        final_position = input("Posicion final")
        self.save_positions(initial_position, final_position)
        self.print_board()


if __name__ == '__main__':
    board = Board()
    board.create_board()
    board.print_board()
    board.set_ships()
