import pygame
from typing import Dict

from pgassets.common.pgObject import pgObject


class Activity:
    def __init__(self, width: int, height: int):
        self.size: (int, int) = width, height
        self.assets: Dict[pgObject] = {}

    def run(self) -> bool:
        return False

    def draw(self, screen: pygame.Surface):
        for asset in self.assets:
            asset.draw(screen)

    def handle_event(self, event: pygame.event):
        pass
