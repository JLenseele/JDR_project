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
TEXT_FONT = pygame.font.Font(None, 25)


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

        # main menu bk
        screen_bk = pygame.image.load('data/img/background/1.png').convert_alpha()
        screen_rect = screen_bk.get_rect(center=(self.screen_width / 2, self.screen_height / 2))

        # logo
        logo_main = pygame.image.load('data/img/logo/logo.png').convert_alpha()
        logo_main = pygame.transform.scale(logo_main, (489, 534))
        logo_rect = logo_main.get_rect(center=(self.screen_width / 2, self.screen_height / 2))

        self.screen.fill('black')

        # background menu principal
        self.screen.blit(screen_bk, screen_rect)

        # Logo menu principal
        #self.screen.blit(logo_main, logo_rect)

        # Titre
        title_text = TITLE_FONT.render('Une histoire à dormir debout',
                                       False, 'black')
        title_rect = title_text.get_rect(center=(self.screen_width / 2, self.screen_height / 3))
        #self.screen.blit(title_text, title_rect)

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
        # affiche le CMD display_text
        self.display_surf = pygame.Surface((self.screen_width / 6 * 4, self.screen_height / 5 * 2))
        self.display_rect = self.display_surf.get_rect(midtop=(self.screen_width / 2, 0))
        # affiche input text
        self.input_surf = pygame.Surface((self.screen_width/6*4, 35))
        self.input_rect = self.display_surf.get_rect(midtop=(self.screen_width / 2, self.display_rect.bottom + 20))
        # main dashboard
        self.main_dashboard_surf = pygame.Surface((self.screen_width, self.screen_height/2))
        self.main_dashboard_rect = self.main_dashboard_surf.get_rect(midbottom=(self.screen_width/2, self.screen_height))
        # ajout stats au dashboard
        self.stats_surf = pygame.Surface((self.main_dashboard_rect.width/7, self.main_dashboard_rect.height))
        self.stats_rect = self.stats_surf.get_rect(midleft=(0, self.main_dashboard_rect.height/2))
        # ajout item menu au dashboard
        self.item_surf = pygame.Surface((self.main_dashboard_rect.width/7*3, self.main_dashboard_rect.height))
        self.item_rect = self.item_surf.get_rect(midleft=self.stats_rect.midright)
        # ajout jauge (vie/mana) menu au dashboard
        self.jauge_surf = pygame.Surface((self.main_dashboard_rect.width / 7*2, self.main_dashboard_rect.height))
        self.jauge_rect = self.jauge_surf.get_rect(midleft=self.item_rect.midright)
        # ajout spell menu au dashboard
        self.spell_surf = pygame.Surface((self.main_dashboard_rect.width / 7, self.main_dashboard_rect.height))
        self.spell_rect = self.spell_surf.get_rect(midleft=self.jauge_rect.midright)
        # texte dans le cmd
        self.text_wr = TEXT_FONT.render('', True, 'White')
        self.text_wr_rect = self.text_wr.get_rect(bottomleft=(self.display_rect.left + 10, self.display_rect.bottom - 10))
        self.text_rd = self.text_wr
        self.text_rd_rect = self.display_rect

        self.list_pnjdialogue = []
        self.list_playerdialogue = []

    def load_objects(self):

        file_name = 'data/prologue/prologue1'
        db = TinyDB(file_name + '.json')
        dial_table = db.table('dialogue')
        ser_dial = dial_table.all()

        for dial in ser_dial:
            d_id = dial['id']
            d_content = dial['content']
            d_next = dial['next']
            d_descr = dial['descr']
            d_end = dial['end']
            if dial['quest']:
                d_quest = dial['quest']
                obj = Playerdialogue(d_id, d_content, d_next, d_descr, d_end, d_quest)
                self.list_playerdialogue.append(obj)
            else:
                obj = Pnjdialogue(d_id, d_content, d_next, d_descr, d_end)
                self.list_pnjdialogue.append(obj)

    def load_text(self):
        return 'texte de test lorem ipsum mon cul sur la commode'

    def show_text(self, text):
        chars = ''
        for i in range(len(text)):
            chars += text[i]
            self.text_wr = TEXT_FONT.render(chars, False, 'White')
            self.screen.blit(self.text_wr, self.text_wr_rect)
            pygame.display.update()
            pygame.time.wait(25)

    def on_start(self):

        self.load_objects()
        pygame.mixer.music.load("data/music/in_game/first.mp3")
        pygame.mixer.music.play(-1)

        self.screen.fill('Green')

        self.display_surf.set_alpha(100)
        self.input_surf.set_alpha(200)
        self.main_dashboard_surf.set_alpha(200)

        self.stats_surf.fill('orange')
        self.item_surf.fill('yellow')
        self.jauge_surf.fill('red')
        self.spell_surf.fill('orchid')

        # affiche console text
        self.screen.blit(self.display_surf, self.display_rect)
        self.screen.blit(self.text_wr, self.text_wr_rect)
        self.screen.blit(self.text_rd, self.text_rd_rect)
        # affiche barre input
        self.screen.blit(self.input_surf, self.input_rect)
        # affiche les stats dans le dashboard
        self.main_dashboard_surf.blit(self.stats_surf, self.stats_rect)
        # affiche item menu dans le DB
        self.main_dashboard_surf.blit(self.item_surf, self.item_rect)
        # affiche jauge (vie/mana) menu dans le DB
        self.main_dashboard_surf.blit(self.jauge_surf, self.jauge_rect)
        # affiche spell menu dans le DB
        self.main_dashboard_surf.blit(self.spell_surf, self.spell_rect)
        # affiche le dashboard principal
        self.screen.blit(self.main_dashboard_surf, self.main_dashboard_rect)

        # dessine barre hor. central
        pygame.draw.line(self.screen, (0, 0, 0, 150),
                         (0, self.screen_height / 2), (self.screen_width, self.screen_height / 2),
                         5)

        # maj la fenetre
        pygame.display.flip()

    def update(self, events):
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
            scene.on_exit()
            scene = new_scene
            scene.on_start()

        if new_scene == scenes['game']:
            text = scene.load_text()
            scene.show_text(text)

            #choix = scene.input(events)
            #text = scene.load_text(choix)
            #scene.show_text(text)

        clock.tick(60)
        pygame.display.update()

