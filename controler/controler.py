import pygame
import os
from models.player import Player
from models.mob import Mob
from models.button import Button

from views.menu import Menu
from views.player import PlayerViews
from views.naration import Naration
from views.combat import combat

from controler import cfgperser


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
        # init pygame
        pygame.init()

        # define screen size
        screen_width = 1080
        screen_height = 720

        # define colors
        BG = (47, 47, 47)
        TEXT_COL = (246, 247, 246)

        # create game window
        flags = pygame.RESIZABLE
        screen = pygame.display.set_mode((screen_width, screen_height), flags)
        pygame.display.set_caption("JDR PROJECT")

        # load button image
        start_bt_menu = pygame.image.load('data/img/button/start_new_game.png').convert_alpha()
        exit_bt_menu = pygame.image.load('data/img/button/exit_game.png').convert_alpha()


        start_bt = Button(int(screen.get_width()/2), int(screen.get_height()/2)-50, start_bt_menu, 1)
        ext_bt = Button(int(screen.get_width()/2), int(screen.get_height()/2)+50, exit_bt_menu, 1)

        print(ext_bt.rect.center)
        print(start_bt.rect.center)

        running = True
        while running:

            # update background
            screen.fill(BG)

            if start_bt.draw(screen):
                self.new_game()
            if ext_bt.draw(screen):
                running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()

        pygame.quit()

    def new_game(self):

        self.menu.presentation()
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
                if choice == 1:
                    Naration.communication(self.player)
                if choice == 2:
                    Naration.combat(self.player)
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
            stats = [12, 4, 20, 3, 3, 3, 10]
        # Elfe
        elif race == 'Elfe':
            stats = [9, 3, 15, 4, 4, 4, 15]
        # Nain
        elif race == 'Nain':
            stats = [15, 6, 25, 2, 3, 2, 5]
        return stats
