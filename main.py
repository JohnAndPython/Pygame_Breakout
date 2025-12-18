import pygame
import time
import sys
from math import sin, cos, radians
import random

from cls_block import Block
from cls_paddle import Paddle
from cls_ball import Ball

pygame.init()


def random_angle_between(min_degree, max_degree, x_value, y_value) -> tuple:
    angle = radians(random.randint(min_degree, max_degree))

    x_value *= cos(angle)
    y_value *= sin(angle)

    return (x_value, y_value)



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

prev_time = time.time()

#game variables
paddle = Paddle()
paddle.rect.centerx = SCREEN_WIDTH // 2
paddle.rect.bottom = SCREEN_HEIGHT - 2 * paddle.rect.height
paddle.speed = 500

vector = pygame.Vector2()


ball = Ball()
ball.rect.centerx = paddle.rect.centerx
ball.rect.bottom = paddle.rect.top
ball.speed_x = 100
ball.speed_y = 100
ball.direction_x = -1
ball.direction_y = -1

ball_angle = radians(random.randint(30, 60))

ball.speed_x *= cos(ball_angle)
ball.speed_y *= sin(ball_angle)

print(ball.speed_x, ball.speed_y)


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

    # Game Logic
    if paddle.move_right:
        paddle.rect.move_ip(paddle.speed * dt, 0)
        if paddle.rect.right >= SCREEN_WIDTH:
            paddle.rect.right = SCREEN_WIDTH
    elif paddle.move_left:
        paddle.rect.move_ip(-paddle.speed * dt, 0)
        if paddle.rect.left <= 0:
            paddle.rect.left = 0

    ball.rect.move_ip(ball.speed_x * ball.direction_x * dt, ball.speed_y * ball.direction_y * dt)

    if ball.rect.right >= SCREEN_WIDTH or ball.rect.left <= 0:
        ball.direction_x *= -1

        ball_angle = radians(random.randint(30, 60))

        ball.speed_x = abs(ball.speed_x) * cos(ball_angle) * (1 if ball.direction_x > 0 else -1)
        ball.speed_y = abs(ball.speed_y) * sin(ball_angle) * (1 if ball.direction_y > 0 else -1)

        print(ball.speed_x, ball.speed_y, ball_angle)
    if ball.rect.top <= 0 or ball.rect.bottom >= SCREEN_HEIGHT:
        ball.direction_y *= -1

        ball_angle = radians(random.randint(30, 60))

        ball.speed_x = abs(ball.speed_x) * cos(ball_angle) * (1 if ball.direction_x > 0 else -1)
        ball.speed_y = abs(ball.speed_y) * sin(ball_angle) * (1 if ball.direction_y > 0 else -1)

        print(ball.speed_x, ball.speed_y, ball_angle)


    # Draw objects on screen
    screen.fill((255,255,255))
    paddle.draw(screen)
    ball.draw(screen)
    

    #update display
    pygame.display.update()

    #set max FPS to 60
    clock.tick(60)