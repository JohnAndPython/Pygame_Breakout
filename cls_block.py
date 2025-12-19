import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, left: int, top: int, width: int, height: int, color: tuple[int]) -> None:
        super().__init__()

        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.left = left
        self.rect.top = top

    def update(self) -> None:
        pass
