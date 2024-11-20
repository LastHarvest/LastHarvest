import math
from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self,id,name,position,direction):
        self.id = id
        self.name = name
        self.position = position
        self.possession = []
        self.points = 0
        self.direction = direction
        self.arme = False

    def get_points(self):
        """Return the current points of the agent."""
        return self.points

    @abstractmethod
    def set_points(self):
        pass

    @abstractmethod
    def move_player_to_player(self, player2):
        pass



    def check_for_resource(self, resources):
        for r in resources:
            self.collect_resource(r)


    def add_points(self, points):
        """Add points to the agent's total."""
        self.points += points


    def add_possession(self, resource):
        """Add a resource to the agent's possession."""
        if resource not in self.possession:
            self.possession.append(resource)

    def get_points(self):
        return self.points

    def get_pos(self):
        """Return the current position of the agent."""
        return self.position

    def update_pos(self, new_position):
        """Update the agent's position."""
        self.position = new_position

    def has_arme(self):
        return self.arme

    def get_vivant(self):
        return self.vivant

    def get_possession(self):
        """Return the list of resources in possession."""
        return self.possession

    def get_direction(self):
        return self.direction

    def get_pos_of_resource(self, resource):
        """Return the position coordinates of the given resource."""
        return resource.get_position()  # Assuming 'resource' has a 'position' attribute

    def get_amount_food(self):
        """Return the amount of food in possession (percentage)"""
        food=0
        for r in self.get_possession():
            if r.get_type()=="food": food+=1
        return food/(len(self.get_possession())+1)

    def get_amount_hydration(self):
        return 1-self.get_amount_food()

    def get_distance_resource(self, resource):
        pos_player = self.get_pos()
        pos_resource = resource.get_position()

        return math.sqrt((pos_resource[0] - pos_player[0])**2 + (pos_resource[1] - pos_player[1])**2)

    def get_id(self):
        return self.id

    def choice_formula(self, resource):
        """Applies the choice formula to the given resource"""
        if resource.get_type()=="food":
            return (resource.get_value()*self.get_amount_food())/(self.get_distance_resource(resource)+1)
        else:
            return (resource.get_value()*self.get_amount_hydration())/(self.get_distance_resource(resource)+1)


    def get_best_resource(self, resources):
        """Return the best resource based on the choice formula"""
        maxi=(0,0)
        for r in resources:
            if (r.is_notTaken() == True) and self.choice_formula(r)>maxi[1]:
                maxi=(r,self.choice_formula(r))
        return maxi[0] #r[0] resource, r[1] formula value


    def collect_resource(self, resource):
        """Collect the resource if the player moves to its position.
        If the resource is a weapon then it sets weapon has true to be able to kill the other player
        """
        val = resource.is_notTaken() and self.get_pos() == resource.get_position()
        if val and resource.get_type() == "Arme":
            resource.set_Appeared()
            self.arme = True

        elif val:
            resource.set_Taken()
            self.add_possession(resource)
            self.set_points()


    def get_arme(self):
        return self.arme


    def move_up(self):
            self.position = (self.position[0], self.position[1] + 1)

    def move_down(self):
        self.position = (self.position[0], self.position[1] - 1)

    def move_left(self):
        self.position = (self.position[0] - 1, self.position[1])
        self.direction="left"

    def move_right(self):
        self.position = (self.position[0] + 1, self.position[1])
        self.direction="right"

    def accelerate_up(self):
        self.move_up()
        self.move_up()
        self.move_up()


    def accelerate_down(self):
        self.move_down()
        self.move_down()
        self.move_down()


    def accelerate_right(self):
        self.move_right()
        self.move_right()
        self.move_right()


    def accelerate_left(self):
        self.move_left()
        self.move_left()
        self.move_left()

    def is_Next(self, pp):
        return (self.get_pos()[0] == pp.get_pos()[0]) or (self.get_pos()[1] == pp.get_pos()[1]) or (self.get_pos()[0] == pp.get_pos()[0]+1) or (self.get_pos()[1] == pp.get_pos()[1]+1)

    # def tuer(self, player2):
    #     if (player2.get_vivant()): player2.vivant = False
    #     return 404
