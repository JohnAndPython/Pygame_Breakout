import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.surface = None
        self.rect = None

    def update(self):
        pass
        #return super().update(*args, **kwargs)
    
    def draw(self, surface: pygame.Surface) -> None:
        pass