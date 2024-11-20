import math
from Player import Player


class Player2(Player):
    def __init__(self,id,name,position, direction):
        super().__init__(id,name,position, direction)

    def set_points(self):
        sum=0
        for r in self.possession:
            sum+=r.get_value()
        self.points = sum*2

    def move_player_to_resource(self, resource, res):
        p = self.get_pos()
        r = resource.get_position()
        if p[0] < r[0]:
            self.move_right()
        elif p[0] > r[0]:
            self.move_left()
        else:
            if p[1] < r[1]:
                self.move_up()
            elif p[1] > r[1]:
                self.move_down()
        print(res)
        self.check_for_resource(res)

    def move_player_to_player(self, player2):
        p = self.get_pos()
        pp = player2.get_pos()

        if (p[0] == pp[0]) and p[1] == pp[1]: return 404

        if p[0] < pp[0]:
            self.move_right()
        elif p[0] > pp[0]:
            self.move_left()
        else:
            if p[1] < pp[1]:
                self.move_up()
            elif p[1] > pp[1]:
                self.move_down()
        return 0

    def avoirArme(self):
        return False