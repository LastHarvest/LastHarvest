from Player import Player


class Player1(Player):
    def __init__(self,id,name,position,direction):
        super().__init__(id,name,position, direction)

    def set_points(self):
        sum=0
        for r in self.possession:
            sum+=r.get_value()
        self.points += sum