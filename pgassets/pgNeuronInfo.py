import pygame

from pgassets.pgImagePanel import pgImagePanel
from pgassets.pgObject import pgObject


class pgNeuronInfo(pgObject):
    def __init__(self, pos, size=(200, 300)):
        pgObject.__init__(self, pos, size, (255, 100, 100))
        self.neuron = None
        self.font_big = pygame.font.SysFont("arial", 16)
        self.font_big.set_bold(True)
        self.font = pygame.font.SysFont("monospace", 12)
        self.weights = []

        # create textlabel
        self.label = self.font_big.render("Show info for neuron (., .)", 1, (0, 0, 0))
        self.label_rect = self.label.get_rect()
        self.label_rect.center = (self.rect.left + self.rect.width / 2, self.rect.top + 20)

        # create imagelabels
        self.img_in = pgImagePanel((self.rect.left + 40, self.label_rect.bottom + 25), (32, 32), "in_icon_32.png", transparent=True)
        self.img_out = pgImagePanel((self.rect.right - 72, self.label_rect.bottom + 25), (32, 32), "out_icon_32.png", transparent=True)

    def set_neuron(self, neuron):
        if neuron is None:
            return
        self.neuron = neuron
        self.label = self.font_big.render("Show weights for neuron (%i, %i)" % self.neuron, 1, (0, 0, 0))
        self.label_rect = self.label.get_rect()
        self.label_rect.center = (self.rect.left + self.rect.width / 2, self.rect.top + 20)

    def set_weights(self, W):
        self.weights = W

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

        # draw border with linewidth = 2
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        if self.neuron is None:
            return

        screen.blit(self.label, self.label_rect)
        self.img_in.draw(screen)
        self.img_out.draw(screen)

        # print incoming weights for neurons, not for input neurons
        if self.neuron[0] > 0:
            for i in range(self.weights[self.neuron[0] - 1].shape[1]):
                label = self.font.render("%.2f" % self.weights[self.neuron[0] - 1].item(self.neuron[1], i), 1, (0, 0, 0))
                label_rect = label.get_rect()
                label_rect.right = self.img_in.rect.right
                label_rect.top = self.img_in.rect.bottom + 18 * (i + 1)
                screen.blit(label, label_rect)

        # print outgoing weights for neurons, not for output neurons
        try:
            for i in range(self.weights[self.neuron[0]].shape[0]):
                label = self.font.render("%.2f" % self.weights[self.neuron[0]].item(i, self.neuron[1]), 1, (0, 0, 0))
                label_rect = label.get_rect()
                label_rect.right = self.img_out.rect.right
                label_rect.top = self.img_out.rect.bottom + 18 * (i + 1)
                screen.blit(label, label_rect)
        except IndexError:
            pass
