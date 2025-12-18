import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.surface = pygame.Surface((20, 20))
        self.surface.fill((255, 100, 100))
        self.rect = self.surface.get_rect()

        self.speed_x = 0
        self.speed_y = 0
        self.direction_x = 0
        self.direction_y = 0

    def update(self, *args, **kwargs):
        pass
        #return super().update(*args, **kwargs)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.surface, self.rect)
