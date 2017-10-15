import numpy as np
import pygame

from pgassets.pgObject import pgObject


class pgNeuron(pgObject):
    def __init__(self, pos: tuple, id: tuple, radius: int=16, color=(0, 128, 255), label=""):
        pgObject.__init__(self, pos, (radius*2, radius*2), color)
        self.id = id
        self.radius = radius

        font = pygame.font.SysFont("arial", self.radius)
        self.label = font.render(label, 1, (255, 255, 255))
        self.label_rect = self.label.get_rect()
        self.label_rect.center = self.rect.topleft

    def collidepoint(self, pos) -> bool:
        distance = np.hypot(pos[0]-self.rect.left, pos[1]-self.rect.top)

        if distance <= self.radius:
            return True

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.topleft, self.radius, 0)
        pygame.draw.circle(screen, (0, 0, 0), self.rect.topleft, self.radius, 1)
        screen.blit(self.label, self.label_rect)
