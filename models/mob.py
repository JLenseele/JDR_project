class Mob:

    def __init__(self, name, race, life, att, defense):
        self.name = name
        self.race = race
        self.life = life
        self.att = att
        self.defense = defense

    def __str__(self):
        return print('Nom: {}\nVie: {}\nAtt: {}\nDef: {}'.format(self.name, self.life, self.att, self.defense))
