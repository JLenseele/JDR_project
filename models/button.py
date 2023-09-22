import pygame


class Button:

    def __init__(self, x, y, image, scale):
        w = image.get_width()
        h = image.get_height()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, screen):
        action = False

        # get mouse pos
        pos = pygame.mouse.get_pos()

        # check mouse over and click pos
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
