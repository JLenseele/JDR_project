class Mob:

    def __init__(self, id, name, race, life, att, defense, agility, hostility):
        self.id = id
        self.name = name
        self.race = race
        self.life = life
        self.att = att
        self.defense = defense
        self.agility = agility
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
