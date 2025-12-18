import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.surface = pygame.Surface((100, 20))
        self.surface.fill((0, 0, 0))
        self.rect = self.surface.get_rect()

        self.move_right = False
        self.move_left = False
        self.speed = 5

    def update(self):
        pass
        #return super().update(*args, **kwargs)
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.surface, self.rect)