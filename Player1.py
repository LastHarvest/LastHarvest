import math

from Player import Player
from pygame.mouse import get_pos

class Player1(Player):
    def __init__(self,id,name,position):
        super().__init__(id,name,position)

    def set_points(self):
        sum=0
        for r in self.possession:
            sum+=r.get_value()
        self.points += sum

    def move_player_to_resource(self, resource):
        p = self.get_pos()
        r = resource.get_position()
        if p[0] < r[0]:
            self.move_right()
        elif p[0] > r[0]:
            self.move_left()
        if p[1] < r[1]:
            self.move_up()
        elif p[1] > r[1]:
            self.move_down()


