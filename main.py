import pygame
import time
import sys

from cls_block import Block
from cls_paddle import Paddle
from cls_ball import Ball

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

prev_time = time.time()

#game variables
paddle = Paddle()
paddle.rect.centerx = SCREEN_WIDTH // 2
paddle.rect.bottom = SCREEN_HEIGHT - 2 * paddle.rect.height

ball = Ball



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
                paddle.move_left = True
            elif event.key == pygame.K_RIGHT:
                paddle.move_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle.move_left = False
            elif event.key == pygame.K_RIGHT:
                paddle.move_right = False


    if paddle.move_right:
        paddle.rect.move_ip(5, 0)
        if paddle.rect.right >= SCREEN_WIDTH:
            paddle.rect.right = SCREEN_WIDTH
    elif paddle.move_left:
        paddle.rect.move_ip(-5, 0)
        if paddle.rect.left <= 0:
            paddle.rect.left = 0

    
    screen.fill((255,255,255))
    paddle.draw(screen)
    

    #update display
    pygame.display.update()

    #set max FPS to 60
    clock.tick(60)