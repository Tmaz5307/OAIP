class Ship:
    def __init__(self, length):
        self.length = length


class Battleship(Ship):
    def __init__(self, amount):
        super().__init__(length=4)
        self.amount = amount


class Cruiser(Ship):
    def __init__(self, amount):
        super().__init__(length=3)
        self.amount = amount


class Destroyer(Ship):
    def __init__(self, amount):
        super().__init__(length=2)
        self.amount = amount


class Game:
    def __init__(self, width, length, position):
        self.width = width
        self.length = length
        self.position = position

    def place_ship(self, ship):
        pass

    def shoot(self, position):
        pass

    def is_game_over(self):
        pass

    def print_board(self):
        pass


