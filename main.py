import pygame
import time
import sys

from cls_block import Block
from cls_player import Player

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

prev_time = time.time()

#game variables
move_player_left = False
move_player_right = False


rect = pygame.Rect(100, 100, 100, 20)

while True:
    #delta time |alternative: dt = clock.tick(60) / 1000
    dt = time.time() - prev_time
    prev_time = time.time()
    
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player_left = True
            elif event.key == pygame.K_RIGHT:
                move_player_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_player_left = False
            elif event.key == pygame.K_RIGHT:
                move_player_right = False


    if move_player_right:
        rect.right += 5
        if rect.right >= SCREEN_WIDTH:
            rect.right = SCREEN_WIDTH
    elif move_player_left:
        rect.left -= 5
        if rect.left <= 0:
            rect.left = 0

    
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0, 0, 0), rect)
    

    #update display
    pygame.display.update()

    #set max FPS to 60
    clock.tick(60)