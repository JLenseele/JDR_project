import random
from . import naration


class combat(object):

    def __init__(self, player, mob):
        self.player = player
        self.mob = mob

    def run_fight(self):

        print(f"Vous engagez le combat contre {self.mob.name}")
        while True:
            self.hero_att()
            if self.mob.life_point <= 0:
                break
            self.mob_att()
            if self.player.life_point <= 0:
                break
        if self.player.life_point <= 0:
            print("Vous êtes mort ... L'aventure s'arrête ici pour vous")
        if self.mob.life_point <= 0:
            texte = "{} est mort\n".format(self.mob.name)
            naration.Naration.elnarator(texte)

    def hero_att(self):
        fight_options = {
            1: 'Attaquer',
            2: 'Lancer un sortilège',
            3: 'Utiliser un objet'
        }
        for key in fight_options.keys():
            print(' ', key, '- ', fight_options[key])
        choice = int(input(''))

        if choice == 1:
            crit = self.roll_dice(self.player.att)
            dammage = int(round((self.player.att * crit) - (self.mob.defense/100*self.player.att)))
            print(f"Attaque physique contre l'ennemi : {dammage} dégats infligés")
            print(f"détail : att/{self.player.att} crit/{crit} def_mob/{self.mob.defense}")
            print(f"calcul : (att * crit) - (def_mob / 100 x att)")
            self.mob.life_point -= dammage
            if self.mob.life_point > 0:
                print(f"Il reste {self.mob.life_point}/{self.mob.life_max} pv")
        elif choice == 2:
            crit = self.roll_dice(self.player.intel)
        elif choice == 3:
            pass

    @staticmethod
    def mob_att():
        pass

    @staticmethod
    def roll_dice(modificateur):
        dice = random.randrange(1,20)
        print(f'Dé : {dice}/20 + {modificateur}')
        dice += modificateur
        if dice < 3:
            crit = 0
        elif 2 < dice < 10:
            crit = 0.8
        elif 9 < dice < 18:
            crit = 1.3
        elif 18 < dice:
            crit = 2
        else:
            crit = 1
        return crit
