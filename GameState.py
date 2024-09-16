import json


class GameState:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filename="game_data.json"):
        self.filename = filename
        self.location = 'Неизвестно'
        self.units = 0
        self.nanites = 0
        self.hydrargyrum = 0
        self.time_left = 0

        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.location = data["location"]
                self.units = data["units"]
                self.nanites = data["nanites"]
                self.hydrargyrum = data["hydrargyrum"]
                self.time_left = data["time_left"]
        except FileNotFoundError:
            pass

    def save(self):
        data = {
            "location": self.location,
            "units": self.units,
            "nanites": self.nanites,
            "hydrargyrum": self.hydrargyrum,
            "time_left": self.time_left
        }

        with open(self.filename, "w") as f:
            json.dump(data, f)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.location = data["location"]
                self.units = data["units"]
                self.nanites = data["nanites"]
                self.hydrargyrum = data["hydrargyrum"]
                self.time_left = data["time_left"]
        except FileNotFoundError:
            pass


def main():
    game_state = GameState()
    print("Локация: ", game_state.location)
    print("Юниты: ", game_state.units)
    print("Наниты: ", game_state.nanites)
    print("Ртуть: ", game_state.hydrargyrum)
    print("Время в игре: ", game_state.time_left)
    print('---------------------------')
    game_state.location = input('Введите новое название локации: ')
    game_state.units = int(input("Введите новое значение для 'Юниты': "))
    game_state.nanites = int(input("Введите новое значение для 'Наниты': "))
    game_state.hydrargyrum = int(input("Введите новое значение для 'Ртуть': "))
    game_state.time_left = int(input("Введите новое значение для 'Время в игре'(в часах): "))
    game_state.save()


if __name__ == "__main__":
    main()
