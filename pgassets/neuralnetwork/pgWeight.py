import pygame


class pgWeight:
    def __init__(self, start, end, color, width):
        self.start = start
        self.end = end
        self.color = color
        self.width = width

    def draw(self, screen: pygame.Surface):
        if self.width == 1:
            pygame.draw.aaline(screen, self.color, self.start, self.end, self.width)
        else:
            pygame.draw.line(screen, self.color, self.start, self.end, self.width)
