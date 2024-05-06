class Spell:
    def __init__(self, m):
        self.mana = m


class ElementalMagic(Spell):
    def __init__(self, m, b, f):
        Spell.__init__(self, m)
        self.burning = b
        self.frostbite = f


class Firemagic(ElementalMagic):
    def __init__(self, m, fd):
        ElementalMagic.__init__(self, m, 7, 0)
        self.fire_damage = fd


class Frostmagic(ElementalMagic):
    def __init__(self, m, frd):
        ElementalMagic.__init__(self, m, 0, 6)
        self.frost_damage = frd


Frost_Spear = Frostmagic(12, 8)
Fireball = Firemagic(10, 5)
