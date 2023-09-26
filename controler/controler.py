import pygame
from sys import exit

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
        self.is_playing = False
        # define screen size
        self.screen_width = 1080
        self.screen_height = 720

    def run(self):
        # init pygame
        pygame.init()

        # define colors
        BG = (47, 47, 47)
        TEXT_COL = (246, 247, 246)

        # create game window
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("JDR PROJECT")

        # create clock obj
        clock = pygame.time.Clock()

        # create text font
        game_font = pygame.font.Font('data/font/tahoma.ttf', 20)

        # load button image
        start_bt_menu = pygame.image.load('data/img/button/start_new_game.png').convert_alpha()
        exit_bt_menu = pygame.image.load('data/img/button/exit_game.png').convert_alpha()

        # create start menu button
        start_bt = Button(int(screen.get_width()/2), int(screen.get_height()/2)-50, start_bt_menu, 1)
        ext_bt = Button(int(screen.get_width()/2), int(screen.get_height()/2)+50, exit_bt_menu, 1)

        # create surface for game
        cmd_surf = pygame.Surface((int(self.screen_width/6)*4, int(self.screen_height/2)))
        cmd_surf.fill('gray31')
        cmd_rect = cmd_surf.get_rect(topleft = (int(self.screen_width / 6), 0))

        input_surf = pygame.Surface((int(self.screen_width/6)*4, 30))
        input_surf.fill((47, 47, 200))
        input_text_surf = game_font.render('text input here', True, TEXT_COL)
        input_rect = input_surf.get_rect(topleft = (int(self.screen_width / 6), int(self.screen_height / 2) + 10))

        # create text_surface
        writting_text_surf = game_font.render('text writting here', True, TEXT_COL)


        while True:

            # check if any event is quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # fill all screen with color BG
            screen.fill(BG)

            if self.is_playing:
                screen.blit(cmd_surf, (int(self.screen_width / 6), 0))
                screen.blit(input_surf, (int(self.screen_width / 6), int(self.screen_height / 2) + 10))
                pygame.draw.rect(screen, 'Green', input_rect, 1, 20)
                pygame.draw.rect(screen, 'Green', cmd_rect, 1, 20)
                pygame.draw.line(screen,
                                 'Green',
                                 (0, int(self.screen_height/2 + 20 + input_surf.get_height())),
                                 (self.screen_width, int(self.screen_height/2 + 20 + input_surf.get_height()))
                                 )
                input_surf.blit(input_text_surf, (10,0))
                cmd_surf.blit(writting_text_surf, (10, cmd_surf.get_height()-30))

            else:
                if start_bt.draw(screen):
                    self.is_playing = True
                if ext_bt.draw(screen):
                    pygame.quit()
                    exit()

            # update entire window
            pygame.display.update()
            clock.tick(60)

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
