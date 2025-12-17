import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)

        self.surface = None
        self.rect = None

    def update(self) -> None:
        pass
