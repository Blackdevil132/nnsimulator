import pygame

from pgassets.pgObject import pgObject


class pgTextPanel(pgObject):
    def __init__(self, pos, size, text, transparent=False, borderwidth=0, color=(255, 255, 255), textcolor=(0, 0, 0), bordercolor=(0, 0, 0), fontsize=20, bold=False):
        pgObject.__init__(self, pos, size, color, borderwidth, transparent, bordercolor)
        self.font = pygame.font.SysFont("arial", fontsize)
        self.font.set_bold(bold)
        self.textcolor = textcolor

        self.label = self.font.render(text, 1, self.textcolor)
        self.label_rect = self.label.get_rect()
        self.label_rect.center = self.rect.center

    def set_text(self, text: str):
        self.label = self.font.render(text, 1, self.textcolor)
        self.label_rect = self.label.get_rect()
        self.label_rect.center = self.rect.center

    def draw(self, screen):
        pgObject.draw(self, screen)
        screen.blit(self.label, self.label_rect)