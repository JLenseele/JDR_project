from models.player import Player
from models.mob import Mob

from views.menu import Menu
from views.player import PlayerViews
from views.naration import Naration
from views.combat import combat

from . import cfgperser


class MainController(object):
    """docstring for MainController"""

    def __init__(self):
        self.player = None
        self.menu = Menu()
        self.com = False
        self.fight = False
        self.trade = False
        self.loot = False
        self.mob = None

    def run(self):
        menu_choice = self.menu.main_menu()

        # Choix creation player
        if menu_choice == 1:
            self.create_player()

            mob = None
            place = None
            pnj = None


            #test combat pnj
            tavernier = "data/pnj/tavernier.ini"

            s = cfgperser.stats_pnj(tavernier)
            print(s[0])
            self.mob = Mob(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10], s[11])

            fight = combat(self.player, self.mob)
            fight.run_fight()

            #test dialogue
            cfgperser.dialogue(tavernier)

            # Démarrage de l'aventure
            # Prologue
            Naration.elnarator(Naration.begin())



            while True:
                choice = Naration.choice(self.player)
                if choice == 1: Naration.communication(self.player)
                if choice == 2: Naration.combat(self.player)
                Naration.situation(self.player)

    def taverne(self):
        print("Vous êtes dans la taverne:")

    def create_player(self):
        name = PlayerViews.player_name()
        race = PlayerViews.player_race()
        stats = self.define_player_stats(race)
        self.player = Player(name,
                             race,
                             stats[0],
                             stats[1],
                             stats[2],
                             stats[3],
                             stats[4],
                             stats[5],
                             stats[6], )
        self.player.__str__()

    @staticmethod
    def define_player_stats(race):
        # Humain
        if race == 'Humain':
            stats = [12, 4, 4, 3, 3, 3, 10]
        # Elfe
        elif race == 'Elfe':
            stats = [9, 3, 2, 4, 4, 4, 15]
        # Nain
        elif race == 'Nain':
            stats = [15, 6, 4, 2, 3, 2, 5]
        return stats
