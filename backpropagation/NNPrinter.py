import random
import sys

import numpy as np
import pygame

from backpropagation.Backpropagation import Backpropagation
from backpropagation.NNExporter import export_nn
from backpropagation.pgNNSimulation import pgNNSimulation
from pgassets.common.pgButton import pgButton
from pgassets.common.pgCheckbox import pgCheckbox
from pgassets.common.pgGraph import pgGraph
from pgassets.common.pgGrid import pgGrid
from pgassets.common.pgImageButton import pgImageButton
from pgassets.common.pgImagePanel import pgImagePanel
from pgassets.common.pgNumInput import pgNumInput
from pgassets.common.pgObject import pgObject
from pgassets.common.pgSlider import pgSlider
from pgassets.common.pgTextPanel import pgTextPanel
from pgassets.neuralnetwork.pgNeuronInfo import pgNeuronInfo
from pgassets.neuralnetwork.pgStructureInput import pgStructureInput

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR_PANEL = (255, 100, 100)
COLOR_BG = (230, 230, 230)

tr_sets = [
    [np.matrix("1; 0; 0; 0; 0; 0; 0; 0"), np.matrix("1; 0; 0; 0; 0; 0; 0; 0")],
    [np.matrix("0; 1; 0; 0; 0; 0; 0; 0"), np.matrix("0; 1; 0; 0; 0; 0; 0; 0")],
    [np.matrix("0; 0; 1; 0; 0; 0; 0; 0"), np.matrix("0; 0; 1; 0; 0; 0; 0; 0")],
    [np.matrix("0; 0; 0; 1; 0; 0; 0; 0"), np.matrix("0; 0; 0; 1; 0; 0; 0; 0")],
    [np.matrix("0; 0; 0; 0; 1; 0; 0; 0"), np.matrix("0; 0; 0; 0; 1; 0; 0; 0")],
    [np.matrix("0; 0; 0; 0; 0; 1; 0; 0"), np.matrix("0; 0; 0; 0; 0; 1; 0; 0")],
    [np.matrix("0; 0; 0; 0; 0; 0; 1; 0"), np.matrix("0; 0; 0; 0; 0; 0; 1; 0")],
    [np.matrix("0; 0; 0; 0; 0; 0; 0; 1"), np.matrix("0; 0; 0; 0; 0; 0; 0; 1")]]

def show_neural_network():
    # initialize pygame window
    size = width, height = 1280, 720
    icon = pygame.image.load("images/brain_icon_32.png")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("NNNS Neural Network Simulator")

    # initialize OPTIONS state
    grid_imgs = []
    for i in range(12):
        grid_imgs.append(pgImagePanel((0, 0), (250, 150), "brain_icon_48.png", color=COLOR_PANEL,
                                      borderwidth=2, id=i+1))
    options_grid = pgGrid((0, 80), (width, height - 160), (3, 4), grid_imgs)
    options_header = pgTextPanel((0, 0), (width, 80), "Choose a function to learn", color=COLOR_PANEL, bold=True,
                                 fontsize=28)

    # initialize STRUCTURE state
    structure_back = pgImageButton((width * 0.5 - 250, height - 65), (200, 50), "play_icon_32.png", COLOR_BG)
    structure_back.image = pygame.transform.rotate(structure_back.image, 180)
    structure_start = pgButton((width * 0.5 + 50, height - 65), (200, 50), "Start", COLOR_BG)
    structure_num_layer_input = pgNumInput((0.15 * width, 0.5 * height), (50, 100), 1)
    structure_input = pgStructureInput((0.4 * width, 200), (0.5 * width, height - 400), (8, 8), 1, COLOR_PANEL)
    structure_num_layer_box = pgObject((0, 200), (250, height - 400), COLOR_PANEL, 2)
    structure_num_layer_box.rect.centerx = structure_num_layer_input.rect.centerx

    # initialize static assets / collect assets in list
    structure_assets = [
        structure_num_layer_box,
        pgTextPanel((0, 0), (width, 80), "Configure neural network", color=COLOR_PANEL, bold=True,
                    fontsize=28),
        pgTextPanel((0.15 * width, 210), (50, 50), "number of",
                    transparent=True, fontsize=28, bold=True),
        pgTextPanel((0.15 * width, 260), (50, 50), "hidden layers",
                    transparent=True, fontsize=28, bold=True),
        structure_back,
        structure_start,
        structure_num_layer_input,
        structure_input
    ]

    # initialize some variables
    clock = pygame.time.Clock()
    done = False
    RUNNING, PAUSE, OPTIONS, STRUCTURE = 0, 1, 2, 3
    state = OPTIONS

    while not done:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if state == OPTIONS:
                    if options_grid.collidepoint(mouse_pos):
                        state = STRUCTURE

                elif state == STRUCTURE:
                    if structure_back.collidepoint(mouse_pos):
                        state = OPTIONS

                    elif structure_start.collidepoint(mouse_pos):
                        struct = structure_input.get_value()
                        nn = Backpropagation(struct)
                        # initialize network simulator
                        nn_simulation = pgNNSimulation((side_panel_width, 0), (width - side_panel_width, 720), struct)
                        state = PAUSE

                    elif structure_input.collidepoint(mouse_pos):
                        pass

                    elif structure_num_layer_input.collidepoint(mouse_pos):
                        structure_input.set_num_hidden(structure_num_layer_input.get_value())

        else:
            if state == RUNNING:
                # train network with random sample
                x, y = random.choice(tr_sets)
                nn.learn([x], [y])

                screen.fill(COLOR_BG)

                # get threshold for weight display
                threshold = threshold_slider.get_value()
                nn_simulation.set_threshold(threshold, threshold_checkbox.get_status())

                # update nn
                nn_simulation.update(nn.W, nn.b)

                # calculate and update error and graph
                total_error = nn.get_error(tr_sets)
                error_history.append(total_error)
                error_graph.set_data(error_history)
                error_panel.set_text("Average error: %.2f%%" % (100.0 * total_error))

                # update cycles and fps
                cycles_panel.set_text("Cycles: %i" % counter)
                fps_panel.set_text("FPS: %i" % clock.get_fps())

                # update weights for neuron info panel
                neuron_info.set_weights(nn.W)

                # draw assets
                for asset in assets:
                    asset.draw(screen)

                nn_simulation.draw(screen)

                # draw left side panel border
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, side_panel_width, 75), 2)
                pygame.draw.line(screen, (0, 0, 0), (side_panel_width, 0), (side_panel_width, height), 4)

                # cycles++
                counter += 1

            elif state == PAUSE:
                screen.fill(COLOR_BG)

                # draw assets
                for asset in assets:
                    asset.draw(screen)

                nn_simulation.draw(screen)

                # draw left side panel border
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, side_panel_width, 75), 2)
                pygame.draw.line(screen, (0, 0, 0), (side_panel_width, 0), (side_panel_width, height), 4)

            elif state == OPTIONS:
                screen.fill(COLOR_BG)
                options_header.draw(screen)
                pygame.draw.line(screen, (0, 0, 0), (0, 80), (width, 80), 3)
                pygame.draw.rect(screen, COLOR_PANEL, pygame.Rect(0, height - 80, width, 80))
                pygame.draw.line(screen, (0, 0, 0), (0, height - 80), (width, height - 80), 3)
                options_grid.draw(screen)

            elif state == STRUCTURE:
                screen.fill(COLOR_BG)
                pygame.draw.line(screen, (0, 0, 0), (0, 80), (width, 80), 3)
                pygame.draw.rect(screen, COLOR_PANEL, pygame.Rect(0, height - 80, width, 80))
                pygame.draw.line(screen, (0, 0, 0), (0, height - 80), (width, height - 80), 3)

                for o in structure_assets:
                    o.draw(screen)

            # update display
            pygame.display.flip()
            clock.tick(1000)

    pygame.quit()
    sys.exit()