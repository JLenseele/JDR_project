import pygame
from tinydb import TinyDB, Query
from sys import exit

from models.button import Button
from models.surface import Surface
from models.dialogue import Pnjdialogue, Playerdialogue

from views.player import PlayerViews
from views.naration import Naration
from views.combat import combat

from controler import cfgperser

# init pygame
pygame.init()
# define colors
BG = (47, 47, 47)
BT_MENU_FONT = pygame.font.Font(None, 30)
TITLE_FONT = pygame.font.Font(None, 100)
TEXT_FONT = pygame.font.Font(None, 20)


class Scene:
    def on_start(self):
        pass

    def handling_event(self):
        pass

    def update(self, events):
        pass

    def display(self):
        pass

    def on_exit(self):
        pass


class Menu(Scene):
    """docstring for MainController"""

    def __init__(self, screen, scenes):
        self.screen = screen
        self.scenes = scenes
        self.is_playing = False
        # define screen size
        self.screen_width = 1080
        self.screen_height = 720
        # music
        self.channel = pygame.mixer.Channel(0)
        # bouton
        self.resume_bt = Button(250, 50,
                             self.screen_width / 2, self.screen_height / 2 + 25,
                             'Blue',
                             'Reprendre la Partie', BT_MENU_FONT)
        self.new_game_bt = Button(200, 50,
                                  self.screen_width/2, self.screen_height/2 + 100,
                                  'Blue',
                                  'Nouvelle Partie', BT_MENU_FONT)
        self.ext_bt = Button(150, 50,
                                  self.screen_width/2, self.screen_height/2 + 175,
                                  'Blue',
                                  'Quitter', BT_MENU_FONT)

    def on_start(self):
        # music menu
        pygame.mixer.music.load('data/music/menu/music_menu.mp3')
        pygame.mixer.music.play(-1)

        # logo
        logo_main = pygame.image.load('data/logo/logo.png').convert_alpha()
        logo_main = pygame.transform.scale(logo_main, (489, 534))
        logo_rect = logo_main.get_rect(center=(self.screen_width / 2, self.screen_height / 2))

        self.screen.fill('blue4')

        # Logo menu principal
        self.screen.blit(logo_main, logo_rect)

        # Titre
        title_text = TITLE_FONT.render('Une histoire à dormir debout',
                                       False, 'darkolivegreen1')
        title_rect = title_text.get_rect(center=(self.screen_width / 2, self.screen_height / 3))
        self.screen.blit(title_text, title_rect)

    def handling_event(self):
        pass

    def update(self, events):
        # bouton menu options
        if self.resume_bt.draw(self.screen):
            return self.scenes['game']
        if self.new_game_bt.draw(self.screen):
            return self.scenes['game']
        if self.ext_bt.draw(self.screen):
            pygame.quit()
            exit()

        pygame.display.flip()

        return self


class Game(Scene):

    def __init__(self, screen, scenes):
        self.screen = screen
        self.scenes = scenes
        self.is_playing = True
        # define screen size
        self.screen_width = 1080
        self.screen_height = 720
        # music
        self.music = pygame.mixer.music.load("data/music/in_game/first.mp3")
        self.channel = pygame.mixer.Channel(0)
        self.prologue = False

    def load_objects(self):
        dial_file_name = 'data/prologue/prologue1'
        db = TinyDB(dial_file_name + '.json')


    def on_start(self):
        self.load_objects()
        print('GAME')
        pygame.mixer.music.load("data/music/in_game/first.mp3")
        pygame.mixer.music.play(-1)
        self.screen.fill('Green')

        # affiche le CMD display_text
        display_surf = pygame.Surface((self.screen_width / 6 * 4, self.screen_height / 5 * 2))
        display_rect = display_surf.get_rect(midtop=(self.screen_width / 2, 0))
        display_surf.set_alpha(100)
        # affiche input text
        input_surf = pygame.Surface((self.screen_width/6*4, 35))
        input_rect = display_surf.get_rect(midtop=(self.screen_width / 2, display_rect.bottom + 20))
        input_surf.set_alpha(200)

        # main dashboard
        main_dashboard_surf = pygame.Surface((self.screen_width, self.screen_height/6*3))
        main_dashboard_rect = main_dashboard_surf.get_rect(midbottom=(self.screen_width/2, self.screen_height))
        main_dashboard_surf.set_alpha(200)
        # ajout stats au dashboard
        stats_surf = pygame.Surface((main_dashboard_rect.width/7, main_dashboard_rect.height))
        stats_rect = stats_surf.get_rect(midleft=(0, main_dashboard_rect.height/2))
        stats_surf.fill('orange')
        # ajout item menu au dashboard
        item_surf = pygame.Surface((main_dashboard_rect.width/7*3, main_dashboard_rect.height))
        item_rect = item_surf.get_rect(midleft=stats_rect.midright)
        item_surf.fill('yellow')
        # ajout jauge (vie/mana) menu au dashboard
        jauge_surf = pygame.Surface((main_dashboard_rect.width / 7*2, main_dashboard_rect.height))
        jauge_rect = jauge_surf.get_rect(midleft=item_rect.midright)
        jauge_surf.fill('red')
        # ajout spell menu au dashboard
        spell_surf = pygame.Surface((main_dashboard_rect.width / 7, main_dashboard_rect.height))
        spell_rect = spell_surf.get_rect(midleft=jauge_rect.midright)
        spell_surf.fill('orchid')

        # affiche console text
        self.screen.blit(display_surf, display_rect)
        text = TEXT_FONT.render('texte de test', True, 'White')
        text_rect = text.get_rect(bottomleft=(display_rect.left + 10, display_rect.bottom - 10))
        self.screen.blit(text, text_rect)

        # affiche barre input
        self.screen.blit(input_surf, input_rect)

        # dessine barre hor. central
        pygame.draw.line(self.screen, (0, 0, 0, 150),
                         (0, self.screen_height / 2), (self.screen_width, self.screen_height / 2),
                         5)

        # affiche les stats dans le dashboard
        main_dashboard_surf.blit(stats_surf, stats_rect)
        # affiche item menu dans le DB
        main_dashboard_surf.blit(item_surf, item_rect)
        # affiche jauge (vie/mana) menu dans le DB
        main_dashboard_surf.blit(jauge_surf, jauge_rect)
        # affiche spell menu dans le DB
        main_dashboard_surf.blit(spell_surf, spell_rect)
        # affiche le dashboard principal
        self.screen.blit(main_dashboard_surf, main_dashboard_rect)

        # maj la fenetre
        pygame.display.flip()

    def update(self, events):
        while True:
            # check if any event is quit
            events = pygame.event.get()
            print('boucle 2')
            for event in events:
                if event.type == pygame.QUIT:
                    return


            return self


def main():

    # create game window
    screen = pygame.display.set_mode((1080, 720))
    clock = pygame.time.Clock()

    # All the scene
    scenes = {}
    scenes['menu'] = Menu(screen, scenes)
    scenes['game'] = Game(screen, scenes)

    # Start on Menu
    scene = scenes['menu']
    scene.on_start()
    while True:
        # check if any event is quit
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        # switch scene
        new_scene = scene.update(events)
        if new_scene is not scene:
            print('o')
            scene.on_exit()
            scene = new_scene
            scene.on_start()

        clock.tick(60)
        pygame.display.update()

