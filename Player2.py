import math

from Player import Player


class Player2(Player):
    def __init__(self,id,name,position):
        super().__init__(id,name,position)

    def set_points(self):
        sum=0
        for r in self.possession:
            sum+=r.get_value()
        self.points += sum*2