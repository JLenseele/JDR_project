import pygame


class Surface:

    def __init__(self, w, h, x, y, bk_color, text, font, image=None):
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.bk = bk_color
        self.text = font.render(text, True, 'White')
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def draw(self, screen):
        action = False

        # get mouse pos
        pos = pygame.mouse.get_pos()

        # check mouse over and click pos
        if self.rect.collidepoint(pos):
            pygame.draw.rect(screen, 'orangered', self.rect, 0, 10)
            print('on')
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            pygame.draw.rect(screen, self.bk, self.rect, 0, 10)
            print('off')

        # draw button on screen
        self.surface.set_alpha(0)

        screen.blit(self.surface, self.rect)
        screen.blit(self.text, self.text_rect)

        return action
