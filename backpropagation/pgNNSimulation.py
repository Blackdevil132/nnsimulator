import random

import numpy as np

from backpropagation.Backpropagation import Backpropagation
from pgassets.common.pgObject import pgObject
from pgassets.neuralnetwork.pgNeuron import pgNeuron
from pgassets.neuralnetwork.pgWeight import pgWeight

COLOR_POS_WEIGHT = (70, 255, 70)
COLOR_NEG_WEIGHT = (255, 0, 0)
COLOR_ZERO_WEIGHT = (216, 216, 216)
COLOR_BIAS = (100, 100, 100)


class pgNNSimulation(pgObject):
    def __init__(self, pos, size, structure):
        pgObject.__init__(self, pos, size)
        self.structure = structure
        self.threshold = 1
        self.show_all = False
        self.bias_weights = []
        self.weights = []

        max_x_gap, max_y_gap = 250, 150

        # calculate neuron positions
        self.neuron_positions = [[0 for j in range(structure[i])] for i in range(len(structure))]
        vert_offset = [0 for i in range(len(structure))]
        gap_y = (self.rect.height - 50) / (max(structure))
        gap_y = min((gap_y, max_y_gap))
        gap_x = (self.rect.width - 120) / (len(structure) - 1)
        gap_x = min((gap_x, max_x_gap))
        hor_offset = self.rect.left + (self.rect.width - gap_x * (len(structure) - 1)) / 2
        for j in range(len(structure) - 1):
            dist_all = gap_y * (structure[j])
            vert_offset[j] = self.rect.top + (self.rect.height - dist_all) / 2
        vert_offset[-1] = self.rect.top + (self.rect.height - gap_y * (structure[-1] - 1)) / 2
        for j in range(len(self.neuron_positions)):
            for i in range(len(self.neuron_positions[j])):
                self.neuron_positions[j][i] = (int(hor_offset + j * gap_x), int(vert_offset[j] + gap_y * i))

        self.neurons = []
        for column in range(len(structure)):
            for row in range(structure[column]):
                self.neurons.append(pgNeuron(self.neuron_positions[column][row], (column, row)))

        self.bias = []
        for i in range(len(structure) - 1):
            bias_pos_x, bias_pos_y = self.neuron_positions[i][-1]
            self.bias.append(pgNeuron((bias_pos_x, bias_pos_y + gap_y), (i, structure[i]), 12, (0, 0, 0), "b"))

    def draw(self, screen):
        # draw bias weights
        for w in self.bias_weights:
            w.draw(screen)

        for w in self.weights:
            w.draw(screen)

        # draw neurons
        for neuron in self.neurons:
            neuron.draw(screen)

        for bias in self.bias:
            bias.draw(screen)

    def get_color(self, weight):
        if abs(weight) < self.threshold:
            return COLOR_ZERO_WEIGHT
        elif weight < 0:
            return COLOR_NEG_WEIGHT
        else:
            return COLOR_POS_WEIGHT

    def get_width(self, weight):
        width = abs(weight)
        if self.threshold > width:
            return self.show_all
        else:
            return max(1, int(width))

    def update(self, W, b):
        self.bias_weights = []
        self.weights = []
        # calculate weights
        for l in range(len(W)):
            for i in range(W[l].shape[0]):
                for j in range(W[l].shape[1]):
                    start = self.neuron_positions[l][j]
                    end = self.neuron_positions[l + 1][i]
                    self.weights.append(pgWeight(start, end, self.get_color(W[l].item(i, j)), self.get_width(W[l].item(i, j))))

            # calculate bias weights
            start_b = self.bias[l].rect.topleft
            for i in range(len(self.neuron_positions[l + 1])):
                end_b = self.neuron_positions[l + 1][i]
                self.bias_weights.append(pgWeight(start_b, end_b, COLOR_BIAS, self.get_width(b[l].item(i, 0))))

    def collidepoint(self, pos):
        for neuron in self.neurons:
            if neuron.collidepoint(pos):
                return neuron.id
        return None

    def set_threshold(self, t, s_a=0):
        self.threshold = t
        self.show_all = s_a
