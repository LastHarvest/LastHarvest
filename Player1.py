
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