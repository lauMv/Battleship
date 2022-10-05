

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
            print(" " + elem + "", end=" ")
        print("\n")
        for file in self.board:
            if col != 10:
                print(str(col) + "  | ", end="")
            else:
                print(str(col) + " | ", end="")
            for elem in file:
                print("" + elem + "|", end=" ")
            print('\n')
            col = col+1



if __name__ == '__main__':
    board = Board()
    board.create_board()
    board.print_board()