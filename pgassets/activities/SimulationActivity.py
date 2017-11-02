import pygame

from backpropagation.Backpropagation import Backpropagation
from pgassets.activities.Activity import Activity
from pgassets.common.pgCheckbox import pgCheckbox
from pgassets.common.pgGraph import pgGraph
from pgassets.common.pgImageButton import pgImageButton
from pgassets.common.pgSlider import pgSlider
from pgassets.common.pgTextPanel import pgTextPanel
from pgassets.common.pgToggleButton import pgToggleButton
from pgassets.neuralnetwork.pgNeuronInfo import pgNeuronInfo

COLOR_PANEL = (255, 100, 100)


class SimulationActivity(Activity):
    def __init__(self, width: int, height: int):
        Activity.__init__(self, width, height)
        self.running: bool = False
        self.slider_drag: bool = False
        self.neuron_to_display = (0, 0)

        # initialize RUNNING/PAUSE state
        # initialize left side panel

        side_panel_width: int = 250

        self.assets["fps_display"] = pgTextPanel((0, 0), (side_panel_width, 25), "0 FPS", color=COLOR_PANEL,
                                                 fontsize=15)
        self.assets["cycles_display"] = pgTextPanel((0, 25), (side_panel_width, 25), "Cycles: 0", color=COLOR_PANEL,
                                                    fontsize=15)
        self.assets["error_display"] = pgTextPanel((0, 50), (side_panel_width, 25), "Average error: 0.00%",
                                                   color=COLOR_PANEL, fontsize=15)
        self.assets["error_graph"] = pgGraph((0, 75), (side_panel_width, 150))
        self.assets["neuron_info"] = pgNeuronInfo((0, 225), (side_panel_width, 325))
        self.assets["threshold_slider"] = pgSlider((0, 550), (side_panel_width * 0.8, 50))
        self.assets["threshold_checkbox"] = pgCheckbox((0.8 * side_panel_width, 550), (side_panel_width / 5, 50),
                                                       COLOR_PANEL)
        self.assets["export_button"] = pgImageButton((0, 600), (side_panel_width / 3, 60), "save_icon_32.png",
                                                     COLOR_PANEL)
        self.assets["restart_button"] = pgImageButton((side_panel_width / 3, 600), (side_panel_width / 3 + 1, 60),
                                                      "restart_icon_32.png", COLOR_PANEL)
        self.assets["new_button"] = pgImageButton((1 + 2 * side_panel_width / 3, 600), (side_panel_width / 3, 60),
                                                  "new_icon_32.png", COLOR_PANEL)
        self.assets["pause_button"] = pgToggleButton((side_panel_width / 2, 660), (side_panel_width / 2, 59),
                                                     "play_icon_32.png", "pause_icon_32.png", transparent=True)

    def run(self):
        counter = 1
        error_history = []

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.assets["export_button"].collidepoint(mouse_pos):
                print("Neural network saved in file: 'neural_network.npz'")
                # TODO

            elif self.assets["pause_button"].collidepoint(mouse_pos):
                if not self.running:
                    self.running = True
                elif self.running:
                    self.running = False

            elif self.assets["new_button"].collidepoint(mouse_pos):
                pass
                # TODO

            elif self.assets["restart_button"].collidepoint(mouse_pos):
                counter = 0
                error_history = []
                # TODO

            elif self.assets["threshold_checkbox"].collidepoint(mouse_pos):
                # TODO
                threshold_checkbox.update_status()

            elif self.assets["threshold_slider"].collidepoint(mouse_pos):
                self.slider_drag = True

            self.neuron_to_display = (self.assets["nn_simulation"].collidepoint(mouse_pos))

        elif event.type == pygame.MOUSEBUTTONUP:
            self.slider_drag = False

        elif event.type == pygame.MOUSEMOTION:
            if self.slider_drag:
                mouse_pos = pygame.mouse.get_pos()
                # TODO
                threshold_slider.update_slider(mouse_pos[0])