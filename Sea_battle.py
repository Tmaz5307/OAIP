class Ship:
    def __init__(self, length, amount):
        self.length = length
        self.amount = amount


class Battleship(Ship):
    def __init__(self):
        super().__init__(length=4, amount=1)


class Cruiser(Ship):
    def __init__(self):
        super().__init__(length=3, amount=1)


class Destroyer(Ship):
    def __init__(self):
        super().__init__(length=2, amount=2)


class Game:
    def __init__(self, width, length, ships):
        self.width = width
        self.length = length
        self.ships = ships

    def place_ship(self, ship):
        pass

    def shoot(self, position):
        pass

    def is_game_over(self):
        pass

    def print_board(self):
        pass


