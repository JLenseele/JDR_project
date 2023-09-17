class Mob:

    def __init__(self, id, name, race, life, att, defense, dex, intel, cha, mana, lvl, hostility):
        self.id = id
        self.name = name
        self.race = race
        self.life_max = life
        self.life_point = life
        self.att = att
        self.defense = defense
        self.dex = dex
        self.intel = intel
        self.cha = cha
        self.mana = mana
        self.lvl = lvl
        self.weapon = None
        self.spell = []
        self.inventory = []
        self.hostility = hostility

# https://pynative.com/python-weighted-random-choices-with-probability/
    def __str__(self):
        return print(
            'Nom: {}\n'
            'Vie: {}\n'
            'Att: {}\n'
            'Def: {}'
            .format(
                self.name,
                self.life,
                self.att,
                self.defense))
