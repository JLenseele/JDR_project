from models.player import Player

from views.menu import Menu
from views.player import PlayerViews
from views.naration import Naration


class MainController(object):
    """docstring for MainController"""

    def __init__(self):
        self.player = None
        self.menu = Menu()
        self.com = False
        self.fight = False
        self.trade = False
        self.loot = False

    def run(self):
        menu_choice = self.menu.main_menu()

        # Choix creation player
        if menu_choice == 1:
            self.create_player()

            mob = None
            place = None
            pnj = None

            # Démarrage de l'aventure
            # Prologue
            Naration.elnarator(Naration.begin())

            # test create mob
            mob=open
            models.mob()

            while True:
                choice = Naration.choice(self.player)
                if choice == 1: Naration.communication(self.player)
                if choice == 2: Naration.combat(self.player)
                Naration.situation(self.player)

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
