from .player import Player


class Game:
    player1 = Player()
    player2 = Player()

    def __init__(self):
        self.player1.set_board()
        self.player2.set_board()

    def play(self):
        loser = None
        winner = None
        while loser is None:
            if self.player1.get_state():
                loser = "player_1"
                winner = "player_2"
            else:
                p1_shoot = self.player1.shoot()
                self.player2.recive_bullet(p1_shoot)
            if self.player2.get_state():
                loser = "player_2"
                winner = "player_1"
            else:
                p2_shoot = self.player2.shoot()
                self.player1.recive_shoot(p2_shoot)
        print("Juego terminado")
        print(winner + "Gano!!")
        print(loser + "Perdio!!")
