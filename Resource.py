class Resource:
    def __init__(self, id: int, value: int, position: tuple, type: str, item: int, isFree: bool):
        self.__id = id
        self.__value = value
        self.__position = position
        self.__type = type
        self.__isFree = isFree
        self.__item = item

    def get_id(self) -> int:
        return self.__id

    def get_value(self) -> int:
        return self.__value

    def get_position(self) -> tuple:
        return self.__position

    def get_type(self) -> str:
        return self.__type

    def get_isFree(self) -> bool:
        return self.__isFree

    def set_id(self, id: int):
        self.__id = id

    def set_value(self, value: int):
        self.__value = value

    def set_position(self, position: tuple):
        self.__position = position

    def set_type(self, type: str):
        self.__type = type

    def set_isFree(self ):
        self.__isFree = False

    def get_item(self):
        return self.__item