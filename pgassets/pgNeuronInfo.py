import pygame

from pgassets.pgObject import pgObject


class pgNeuronInfo(pgObject):
    def __init__(self, pos, size=(200, 300)):
        pgObject.__init__(self, pos, size, (255, 100, 100))
        self.neuron = None
        self.font_big = pygame.font.SysFont("arial", 16)
        self.font_big.set_bold(True)
        self.font = pygame.font.SysFont("monospace", 12)
        self.weights = []

        # create textlabels
        self.label = self.font_big.render("Show info for neuron (., .)", 1, (0, 0, 0))
        self.label_in = self.font.render("in:", 1, (0, 0, 0))
        self.label_out = self.font.render("out:", 1, (0, 0, 0))

        # calculate text positions
        self.label_rect = self.label.get_rect()
        self.label_rect.center = (self.rect.left + self.rect.width / 2, self.rect.top + 20)
        self.label_in_rect = self.label_in.get_rect()
        self.label_in_rect.center = (self.rect.left + self.rect.width / 4, self.label_rect.bottom + 25)
        self.label_out_rect = self.label_out.get_rect()
        self.label_out_rect.center = (self.rect.left + 3 * self.rect.width / 4, self.label_rect.bottom + 25)

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
        screen.blit(self.label_in, self.label_in_rect)
        screen.blit(self.label_out, self.label_out_rect)

        # print incoming weights for neurons, not for input neurons
        if self.neuron[0] > 0:
            for i in range(self.weights[self.neuron[0] - 1].shape[1]):
                label = self.font.render("%.2f" % self.weights[self.neuron[0] - 1].item(self.neuron[1], i), 1, (0, 0, 0))
                label_rect = label.get_rect()
                label_rect.right = self.rect.left + 0.35 * self.rect.width
                label_rect.top = self.rect.top + 70 + 18 * i
                screen.blit(label, label_rect)

        # print outgoing weights for neurons, not for output neurons
        try:
            for i in range(self.weights[self.neuron[0]].shape[0]):
                label = self.font.render("%.2f" % self.weights[self.neuron[0]].item(i, self.neuron[1]), 1, (0, 0, 0))
                label_rect = label.get_rect()
                label_rect.right = self.rect.left + 0.85 * self.rect.width
                label_rect.top = self.rect.top + 70 + 18 * i
                screen.blit(label, label_rect)
        except IndexError:
            pass
