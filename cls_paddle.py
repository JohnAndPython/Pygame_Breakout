import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.surface = pygame.Surface((100, 20))
        self.surface.fill((0, 0, 0))
        self.rect = self.surface.get_rect()

        self.move_right = False
        self.move_left = False
        self.speed = 0

    def update(self, dt, border_left: int, border_right: int):
        if self.move_right:
            self.rect.move_ip(self.speed * dt, 0)
            if self.rect.right >= border_right:
                self.rect.right = border_right
        elif self.move_left:
            self.rect.move_ip(-self.speed * dt, 0)
            if self.rect.left <= border_left:
                self.rect.left = border_left
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.surface, self.rect)