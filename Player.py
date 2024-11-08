
import math
from abc import ABC, abstractmethod

from pygame.mouse import get_pos





class Player(ABC):

    def __init__(self,id,name,position,direction):
        self.id = id
        self.name = name
        self.position = position
        self.possession = []
        self.points = 0
        self.direction = direction
        self.arme = False
        self.vivant = True

    def get_points(self):
        """Return the current points of the agent."""
        return self.points

    @abstractmethod
    def set_points(self):
        pass

    def add_points(self, points):
        """Add points to the agent's total."""
        self.points += points

    def setArme(self):
        self.arme = True

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

    def get_arme(self):
        return self.arme

    def update_arme(self,state):
        self.arme = state

    def get_vivant(self):
        return self.vivant

    def update_vivant(self,etat):
        self.vivant = etat

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
             if r.get_isFree() and self.choice_formula(r)>maxi[1]:
                 maxi=(r,self.choice_formula(r))
        return maxi[0]


    def collect_resource(self, resource):
        """Collect the resource if the player moves to its position."""
        if resource.get_isFree() and self.get_pos() == resource.get_position():
            resource.set_isFree()
            self.add_possession(resource)
            self.set_points()
        if resource.get_type == "Arme":
            self.arme=True




    def move_up(self):
        if self.position[1] < 6:
            self.position = (self.position[0], self.position[1] + 1)

    def move_down(self):
        if self.position[1] > 0 :
            self.position = (self.position[0], self.position[1] - 1)

    def move_left(self):
        if self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])
            self.direction="left"

    def move_right(self):
        if self.position[0] < 6:
            self.position = (self.position[0] + 1, self.position[1])
            self.direction="right"


