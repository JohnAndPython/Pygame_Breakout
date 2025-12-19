import pygame
import time
import sys
from math import sin, cos, radians, sqrt
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
ball.speed = 600
ball.direction_x = -1
ball.direction_y = -1
ball_can_collide = True

ball_angle = radians(random.randint(30, 150))
print(ball_angle, ball.rect.centerx, ball.rect.centery)


x = (ball.speed * abs(cos(ball_angle)))
y = (ball.speed * sin(ball_angle))
length = sqrt(x**2 + y**2)
new_x = x / length
new_y = y / length



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
    

    if ball.rect.right >= SCREEN_WIDTH or ball.rect.left <= 0:
        ball.direction_x *= -1
        ball_angle = radians(random.randint(30, 60))

        x = (ball.speed * abs(cos(ball_angle)))
        y = (ball.speed * sin(ball_angle))
        new_x = x / ball.speed
        new_y = y / ball.speed

        if ball.rect.right >= SCREEN_WIDTH:
            ball.rect.right = SCREEN_WIDTH - 1

        elif ball.rect.left <= 0:
            ball.rect.left = 1

    if ball.rect.top <= 0 or ball.rect.bottom >= SCREEN_HEIGHT:
        ball.direction_y *= -1
        ball_angle = radians(random.randint(30, 60))

        x = (ball.speed * abs(cos(ball_angle)))
        y = (ball.speed * sin(ball_angle))
        new_x = x / ball.speed
        new_y = y / ball.speed

        if ball.rect.top <= 0:
            ball.rect.top = 1
        
        elif ball.rect.bottom >= SCREEN_HEIGHT:
            ball.rect.bottom = SCREEN_HEIGHT - 1

    if ball.rect.colliderect(paddle.rect):
        ball.direction_y *= -1
        ball_angle = radians(random.randint(30, 60))
        

        x = (ball.speed * abs(cos(ball_angle)))
        y = (ball.speed * sin(ball_angle))
        new_x = x / ball.speed
        new_y = y / ball.speed

    

    

    #print(ball.rect.bottom, paddle.rect.bottom)
    #print(ball.rect.colliderect(paddle.rect), ball.rect.bottom <= paddle.rect.top)

    paddle.update(dt, 0, SCREEN_WIDTH)
    ball.rect.move_ip(ball.speed * abs(cos(ball_angle)) * ball.direction_x * dt, ball.speed * sin(ball_angle) * ball.direction_y * dt)

    


    
    


    # Draw objects on screen
    screen.fill((255,255,255))
    paddle.draw(screen)
    ball.draw(screen)
    pygame.draw.line(screen, (0, 0, 200), (ball.rect.centerx, ball.rect.centery), (ball.rect.centerx + new_x * 100 * ball.direction_x, ball.rect.centery + new_y * 100 * ball.direction_y))
    

    #update display
    pygame.display.update()

    #set max FPS to 60
    clock.tick(60)