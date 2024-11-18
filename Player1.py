from Player import Player


class Player1(Player):
    def __init__(self,id,name,position,direction):
        super().__init__(id,name,position, direction)

    def set_points(self):
        sum=0
        for r in self.possession:
            sum+=r.get_value()
        self.points = sum

    def move_player_to_resource(self, resource, res):
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
        self.check_for_resource(res)

    def move_player_to_player(self, player2):
        p = self.get_pos()
        pp = player2.get_pos()
        if (p[0] == pp[0]) and p[1] == pp[1]: return self.tuer(player2)

        if p[0] < pp[0]:
            self.move_right()
        elif p[0] > pp[0]:
            self.move_left()
        if p[1] < pp[1]:
            self.move_up()
        elif p[1] > pp[1]:
                self.move_down()

        return 0






