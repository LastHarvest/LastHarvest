import random
from time import sleep

from Resource import Resource
from Player import Player
from Disponibility import TRUE, FALSE, APPEARED
from Player1 import Player1
from Player2 import Player2

class Game:
    def __init__(self):
        self.__running = True
        self.__nbResMax = 11
        self.__nbResources = 6
        self.__winner = -1
        self.__time = 0
        self.__players = [Player1(1, "Player1", (0, 0),"right"),
                            Player2(2, "Player2", (6, 6),"left")]
        self.__resources = [
                            Resource(0, 0, (3, 3), "Arme", 0,FALSE),
                            Resource(2, 9, (3, 4), "Food", 1,TRUE),
                            Resource(3, 30, (2, 1), "Hydration",2, TRUE),
                            Resource(4, 15, (0, 4), "Food", 2,TRUE),
                            # Resource(1, 10, (6, 0), "Food",3, TRUE),
                            # Resource(6, 25, (1, 6), "Food",2, TRUE),
                            # Resource(5, 20, (4, 0), "Hydration", 2,TRUE)
                        ]




#METHODS
    def add_ressources(self):
        players = self.__players
        resources = self.__resources
        tab = []
        tab.append((3, 3))
        for r in resources:
            if r.is_notTaken():
                tab.append(r.get_position())
        x = random.randrange(0, 7)
        y = random.randrange(0, 7)
        while (x, y) in tab:
            x = random.randrange(0, 7)
            y = random.randrange(0, 7)

        image = random.randrange(1, 4)
        val = random.randrange(9, 20)
        test = random.randrange(1, 2)

        if (players[0].get_points() >= 30 or players[1].get_points() >= 30) and not (resources[0].has_Appeared()):
            print("Setting the weapon")
            resources[0].set_True()
        elif test == 1:
            res = Resource(self.get_resourcesLength(), val, (x, y), "Food", image, TRUE)
            resources.append(res)
        else:
            res = Resource(self.get_resourcesLength(), val, (x, y), "Hydration", image, TRUE)
            resources.append(res)

    def action(self):
        i = self.__time % 2
        players = self.__players
        resources = self.__resources

        if players[i].has_arme():
            end = players[i].move_player_to_player(players[abs(i - 1)])
            if players[i].get_pos() == players[abs(i - 1)].get_pos():
                players[i].tuer(players[abs(i - 1)])
                self.__winner = i
                self.__running = False

        elif players[abs(i - 1)].has_arme():
            players[i].fuite(players[abs(i - 1)])

        elif players[i].get_points() >= 50 and resources[0].is_notTaken():
            players[i].move_player_to_resource(resources[0], resources)

        else :
            players[i].move_player_to_resource(players[i].get_best_resource(resources), resources)

        if self.nb_Libre() < 8 and self.__nbResources < self.__nbResMax:
            self.add_nbResources()
            self.add_ressources()



    def nb_Libre(self):
        return sum(1 for r in self.__resources if r.is_notTaken())


#GETTER

    def get_winner(self) -> int:
        return self.__winner

    def get_time(self) -> int:
        return self.__time

    def get_players(self) -> list:
        return self.__players

    def get_resources(self) -> list:
        return self.__resources

    def get_nbResources(self) -> int:
        return self.__nbResources

    def get_nbResMax(self) -> int:
        return self.__nbResMax

    def get_resourcesLength(self) -> int:
        return len(self.__resources)

    def get_running(self):
        return self.__running


##SETTERS
    def set_id(self, id: int):
        self.__id = id

    def set_winner(self, winner: int):
        self.__winner = winner

    def set_time(self, time: int):
        self.__time = time

    def set_players(self, players: list[Player]):
        self.__players = players

    def set_resources(self, resources: list[Resource]):
        self.__resources = resources

##ADDERS
    def increment_time(self):
        self.__time += 1

    def add_nbResources(self):
        self.__nbResources += 1

    def stop_game(self):
        self.__running = False