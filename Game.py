import Player
import Resource

class Game:
    def __init__(self, id: int, players: list[Player], resources: list[Resource]):
        self.__id = id
        self.__winner = 1
        self.__time = 0
        self.__players = players
        self.__resources = resources

        # Accessors (Getters)
        # Accessors (Getters)

    def get_id(self) -> int:
        return self.__id

    def get_winner(self) -> int:
        return self.__winner

    def get_time(self) -> int:
        return self.__time

    def get_players(self) -> list:
        return self.__players

    def get_resources(self) -> list:
        return self.__resources

        # Modifiers (Setters)

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

    def increment_time(self):
        self.__time += 1

