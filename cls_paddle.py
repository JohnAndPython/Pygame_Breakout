import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.surface = pygame.Surface((100, 20))
        self.surface.fill((0, 0, 0))
        self.rect = self.surface.get_rect()

        # small rects for collision
        self.small_rect_left = pygame.Rect()
        self.small_rect_left.height = self.rect.height // 2
        self.small_rect_left.width = int(self.rect.width * 0.15)

        self.small_rect_rigth = pygame.Rect()
        self.small_rect_rigth.height = self.small_rect_left.height
        self.small_rect_rigth.width = int(self.rect.width * 0.15)

        self.small_rect_middle = pygame.Rect()
        self.small_rect_middle.height = self.small_rect_left.height
        self.small_rect_middle.width = int(self.rect.width * 0.25) #self.rect.width - self.small_rect_left.width - self.small_rect_rigth.width


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

        self.small_rect_left.topleft = self.rect.topleft
        self.small_rect_rigth.topright = self.rect.topright
        self.small_rect_middle.midtop = self.rect.midtop
        
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.surface, self.rect)

        # pygame.draw.rect(surface, (0, 255, 200), self.small_rect_left)
        # pygame.draw.rect(surface, (0, 255, 200), self.small_rect_rigth)
        # pygame.draw.rect(surface, (150, 100, 100), self.small_rect_middle)