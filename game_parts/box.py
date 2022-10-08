

class Box:
    state = False
    cont = " "
    pos_x, pos_y = 0, 0

    def set_cont(self, cont):
        self.cont = cont

    def change_state(self):
        self.state = True

    def set_pos(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_cont(self):
        return self.cont

    def get_state(self):
        return self.state