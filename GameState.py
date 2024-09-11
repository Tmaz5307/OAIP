class GameState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        self.location = 'Неизвестно'
        self.units = 0
        self.nanites = 0
        self.hydrargyrum = 0
        self.time_left = 0

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = ''
        print("Локация: ", value)

    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self, value):
        self.__units = value
        print("Юниты: ", value)

    @property
    def nanites(self):
        return self.__nanites

    @nanites.setter
    def nanites(self, value):
        self.__nanites = value
        print("Наниты: ", value)

    @property
    def time_left(self):
        return self.__time_left

    @time_left.setter
    def time_left(self, value):
        self.__time_left = value
        print("Время в игре: ", value)

    @property
    def hydrargyrum(self):
        return self.__hydrargyrum

    @hydrargyrum.setter
    def hydrargyrum(self, value):
        self.__hydrargyrum = value
        print("Ртуть: ", value)


def main():
    game_state = GameState()
    print('---------------------------')
    game_state.location = input('Введите новое название локации: ')
    game_state.units += int(input("Введите новое значение для 'Юниты': "))
    game_state.nanites += int(input("Введите новое значение для 'Наниты': "))
    game_state.hydrargyrum += int(input("Введите новое значение для 'Ртуть': "))
    game_state.time_left += int(input("Введите новое значение для 'Время в игре'(в часах): "))


if __name__ == "__main__":
    main()
