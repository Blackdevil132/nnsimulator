import sys

import pygame

from backpropagation.NNExporter import export_nn
from backpropagation.pgNNSimulation import pgNNSimulation
from pgassets.pgButton import pgButton
from pgassets.pgCheckbox import pgCheckbox
from pgassets.pgGraph import pgGraph
from pgassets.pgImageButton import pgImageButton
from pgassets.pgNeuronInfo import pgNeuronInfo
from pgassets.pgSlider import pgSlider
from pgassets.pgTextPanel import pgTextPanel

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR_PANEL = (255, 100, 100)
COLOR_BG = (240, 240, 240)


def show_neural_network():
    # initialize pygame window
    size = width, height = 1280, 720
    icon = pygame.image.load("images/brain_icon_32.png")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Simulate Neural network with structure (., ., .)")

    side_panel_width = 250

    # initialize left side panel
    fps_panel = pgTextPanel((0, 0), (side_panel_width, 30), "0 FPS", color=COLOR_PANEL, fontsize=15)
    cycles_panel = pgTextPanel((0, 30), (side_panel_width, 30), "Cycles: 0", color=COLOR_PANEL, fontsize=15)
    error_panel = pgTextPanel((0, 60), (side_panel_width, 30), "Average error: 0.00%", color=COLOR_PANEL, fontsize=15)
    error_graph = pgGraph((0, 90), (side_panel_width, 150))
    neuron_info = pgNeuronInfo((0, 240), (side_panel_width, 310))
    threshold_slider = pgSlider((0, 550), (side_panel_width*0.8, 50))
    threshold_checkbox = pgCheckbox((0.8*side_panel_width, 550), (side_panel_width/5, 50), COLOR_PANEL)
    export_button = pgImageButton((0, 600), (side_panel_width / 3, 60), "save_icon_32.png", COLOR_PANEL)
    restart_button = pgImageButton((side_panel_width / 3, 600), (side_panel_width / 3 + 1, 60), "restart_icon_32.png", COLOR_PANEL)
    new_button = pgImageButton((1 + 2*side_panel_width/3, 600), (side_panel_width/3, 60), "new_icon_32.png", COLOR_PANEL)
    pause_button = pgImageButton((side_panel_width/2, 660), (side_panel_width/2, 59), "play_icon_32.png", transparent=True)
    empty_button = pgButton((0, 660), (side_panel_width/2, 59), "", transparent=True)
    # initialize network simulator
    nn_simulation = pgNNSimulation((side_panel_width, 0), (width - side_panel_width, 720))

    # initialize some variables
    clock = pygame.time.Clock()
    counter = 1
    error_history = []
    done = False
    RUNNING, PAUSE = 0, 1
    state = PAUSE
    slider_drag = False

    while not done:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if export_button.collidepoint(mouse_pos):
                    print("Neural network saved in file: 'neural_network.npz'")
                    export_nn(nn_simulation.nn, "neural_network")

                elif pause_button.collidepoint(mouse_pos):
                    if state == PAUSE:
                        state = RUNNING
                        pause_button.set_image("pause_icon_32.png")
                    elif state == RUNNING:
                        state = PAUSE
                        pause_button.set_image("play_icon_32.png")

                elif restart_button.collidepoint(mouse_pos):
                    counter = 0
                    error_history = []
                    nn_simulation.reset()

                elif threshold_checkbox.collidepoint(mouse_pos):
                    threshold_checkbox.update_status()

                elif threshold_slider.collidepoint(mouse_pos):
                    slider_drag = True

                neuron_info.set_neuron(nn_simulation.collidepoint(mouse_pos))

            elif event.type == pygame.MOUSEBUTTONUP:
                slider_drag = False

            elif event.type == pygame.MOUSEMOTION:
                if slider_drag:
                    mouse_pos = pygame.mouse.get_pos()
                    threshold_slider.update_slider(mouse_pos[0])

        else:
            if state == RUNNING:
                screen.fill(COLOR_BG)

                # get threshold for weight display
                threshold = threshold_slider.get_value()
                show_low_weights = threshold_checkbox.get_status()
                nn_simulation.set_threshold(threshold, show_low_weights)

                # update nn
                nn_simulation.update()

                # calculate and update error and graph
                total_error = nn_simulation.get_error()
                error_history.append(total_error)
                error_graph.set_data(error_history)
                error_panel.set_text("Average error: %.2f%%" % (100.0 * total_error))

                # update cycles and fps
                cycles_panel.set_text("Cycles: %i" % counter)
                fps_panel.set_text("FPS: %i" % clock.get_fps())

                # update weights for neuron info panel
                neuron_info.set_weights(nn_simulation.get_weights())

                # draw left side panel
                fps_panel.draw(screen)
                cycles_panel.draw(screen)
                error_panel.draw(screen)
                error_graph.draw(screen)
                neuron_info.draw(screen)
                threshold_checkbox.draw(screen)
                threshold_slider.draw(screen)
                export_button.draw(screen)
                pause_button.draw(screen)
                restart_button.draw(screen)
                new_button.draw(screen)
                empty_button.draw(screen)
                # draw simulation
                nn_simulation.draw(screen)

                # draw left side panel border
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, side_panel_width, 90), 2)
                pygame.draw.line(screen, (0, 0, 0), (side_panel_width, 0), (side_panel_width, height), 4)

                # cycles++
                counter += 1

            elif state == PAUSE:
                screen.fill(COLOR_BG)
                # draw left side panel
                fps_panel.draw(screen)
                cycles_panel.draw(screen)
                error_panel.draw(screen)
                error_graph.draw(screen)
                neuron_info.draw(screen)
                threshold_checkbox.draw(screen)
                threshold_slider.draw(screen)
                export_button.draw(screen)
                pause_button.draw(screen)
                restart_button.draw(screen)
                new_button.draw(screen)
                empty_button.draw(screen)
                # draw simulation
                nn_simulation.draw(screen)

                # draw left side panel border
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, side_panel_width, 90), 2)
                pygame.draw.line(screen, (0, 0, 0), (side_panel_width, 0), (side_panel_width, height), 4)

            # update display
            pygame.display.flip()
            clock.tick(1000)

    pygame.quit()
    sys.exit()