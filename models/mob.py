class Mob:

    def __init__(self, name, race, life, att, defense, agility, hostility, loot):
        self.name = name
        self.race = race
        self.life = life
        self.att = att
        self.defense = defense
        self.agility = agility
        self.hostility = hostility
        self.loot = loot

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
