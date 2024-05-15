class Spell:
    def __init__(self, m):
        self.mana = m


class ElementalMagic(Spell):
    def __init__(self, m, b, f):
        Spell.__init__(self, m)
        self.burning = b
        self.frostbite = f


class ForbiddenMagic(Spell):
    def __init__(self, m, d):
        Spell.__init__(self, m)
        self.desiccation = d


class Firemagic(ElementalMagic):
    def __init__(self, m, fd):
        ElementalMagic.__init__(self, m, 7, 0)
        self.fire_damage = fd


class Frostmagic(ElementalMagic):
    def __init__(self, m, frd):
        ElementalMagic.__init__(self, m, 0, 6)
        self.frost_damage = frd


class Darkmagic(ForbiddenMagic):
    def __init__(self, m, dd):
        ForbiddenMagic.__init__(self, m, 20)
        self.dark_damage = dd


Frostspear = Frostmagic(12, 8)
Fireball = Firemagic(10, 5)
Dark_fog = Darkmagic(13, 9)
