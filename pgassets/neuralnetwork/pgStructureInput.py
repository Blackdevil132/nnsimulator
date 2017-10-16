import pygame

from pgassets.common.pgNumInput import pgNumInput
from pgassets.common.pgObject import pgObject
from pgassets.common.pgTextPanel import pgTextPanel


class pgStructureInput(pgObject):
    def __init__(self, pos, size, io_layers, n_h_layers=1, color=(255, 255, 255), transparent=False):
        pgObject.__init__(self, pos, size, color=color, transparent=transparent, borderwidth=2)
        self.n_in, self.n_out = io_layers
        self.n_h_layers = n_h_layers

        self.h_offset = 0.08 * self.rect.width
        self.width_inner = self.rect.width - 4 * self.h_offset

        # create all static texts to display
        self.textlabels = [
            pgTextPanel(self.rect.topleft,
                        (self.rect.width, 50), "Structure", transparent=True,
                        fontsize=28, bold=True),
            pgTextPanel((self.h_offset + self.rect.left, self.rect.top + 0.5 * self.rect.height),
                        (50, 100), str(self.n_in), transparent=True, fontsize=30),
            pgTextPanel((self.rect.right - self.h_offset - 50, self.rect.top + 0.5 * self.rect.height),
                        (50, 100), str(self.n_out), transparent=True, fontsize=30),
            pgTextPanel((self.h_offset + self.rect.left, self.rect.top + 0.2 * self.rect.height),
                        (50, 100), "Input layer", transparent=True),
            pgTextPanel((self.rect.right - self.h_offset - 50, self.rect.top + 0.2 * self.rect.height),
                        (50, 100), "Output layer", transparent=True),
            pgTextPanel((self.rect.left + 2 * self.h_offset, self.rect.top + 0.2 * self.rect.height),
                        (self.width_inner, 100), "Hidden layers", transparent=True)
        ]

        self.layers = []
        for i in range(self.n_h_layers):
            self.layers.append(
                pgNumInput((2 * self.h_offset - 25 + self.rect.left + (i+1) * (self.width_inner/(self.n_h_layers + 1)),
                            self.rect.top + 0.5 * self.rect.height), (50, 100)))

    def set_num_hidden(self, value):
        if value < 0:
            raise ValueError("cant have negative hidden layers")
        self.n_h_layers = value
        self.layers = []
        for i in range(self.n_h_layers):
            self.layers.append(
                pgNumInput((2 * self.h_offset - 25 + self.rect.left + (i + 1) * (self.width_inner / (self.n_h_layers + 1)),
                            self.rect.top + 0.5 * self.rect.height), (50, 100)))

    def collidepoint(self, pos: tuple):
        if not pgObject.collidepoint(self, pos):
            return 0
        else:
            for o in self.layers:
                if o.collidepoint(pos):
                    return 1

    def draw(self, screen: pygame.Surface):
        pgObject.draw(self, screen)

        for o in self.layers:
            o.draw(screen)

        for l in self.textlabels:
            l.draw(screen)

    def get_value(self):
        return tuple([self.n_in] + [l.get_value() for l in self.layers] +  [self.n_out])
