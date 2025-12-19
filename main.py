import pygame
import time
import sys
from math import sin, cos, radians, sqrt
import random

from cls_block import Block
from cls_paddle import Paddle
from cls_ball import Ball
import levels

pygame.init()


def random_angle_between(min_degree: int, max_degree: int) -> float:
    angle = radians(random.randint(min_degree, max_degree))

    return angle

def x_and_y_components(length, angle) -> tuple[float]:
    x_length = (ball.speed * cos(ball_angle))
    y_length = (ball.speed * sin(ball_angle))

    return (x_length, y_length)




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

#-----------------------------------------------------------
ball = Ball()
ball.rect.centerx = paddle.rect.centerx
ball.rect.bottom = paddle.rect.top - 20
ball.speed = 600
ball.direction_x = -1
ball.direction_y = -1
ball_can_collide = True

ball_angle = random_angle_between(30, 150)
x, y = x_and_y_components(ball.speed, ball_angle) 
new_x, new_y = abs(x) / ball.speed, y / ball.speed

#-----------------------------------------------------------
cur_level = levels.level_001
row_elements = len(cur_level[0])
offset = 4

width_brick = SCREEN_WIDTH // row_elements - offset * 2
height_brick = 20

left_brick = offset
top_brick = 50

level_group = pygame.sprite.Group()


for row in cur_level:
    rand_color = tuple(random.randint(0, 255) for _ in range(3))

    for item in row:
        if item != 0:
            block = Block(left_brick, top_brick, width_brick, height_brick, rand_color)
            level_group.add(block)
            left_brick += width_brick + offset
        else:
            left_brick += width_brick + offset


    left_brick = offset
    top_brick += height_brick + offset




while True:
    #delta time |alternative: dt = clock.tick(60) / 1000
    dt = time.time() - prev_time
    prev_time = time.time()
    
    pygame.display.set_caption(f"{clock.get_fps():.2f}")

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
    
    # Ball collision with walls
    if ball.rect.right >= SCREEN_WIDTH or ball.rect.left <= 0:
        ball.direction_x *= -1
        ball_angle = random_angle_between(30, 60)
        x, y = x_and_y_components(ball.speed, ball_angle) 
        new_x, new_y = abs(x) / ball.speed, y / ball.speed

        if ball.rect.right >= SCREEN_WIDTH:
            ball.rect.right = SCREEN_WIDTH - 1

        elif ball.rect.left <= 0:
            ball.rect.left = 1

    if ball.rect.top <= 0 or ball.rect.bottom >= SCREEN_HEIGHT:
        ball.direction_y *= -1
        ball_angle = random_angle_between(30, 60)
        x, y = x_and_y_components(ball.speed, ball_angle) 
        new_x, new_y = abs(x) / ball.speed, y / ball.speed

        if ball.rect.top <= 0:
            ball.rect.top = 1
        
        elif ball.rect.bottom >= SCREEN_HEIGHT:
            ball.rect.bottom = SCREEN_HEIGHT - 1

    # Ball collision with paddle
    if ball.rect.colliderect(paddle.small_rect_middle):
        ball.direction_y = -1

        ball_angle = random_angle_between(60, 120)
        x, y = x_and_y_components(ball.speed, ball_angle) 
        new_x, new_y = abs(x) / ball.speed, y / ball.speed

    elif ball.rect.colliderect(paddle.small_rect_left):
        ball.direction_x = -1
        ball.direction_y = -1

        ball_angle = random_angle_between(30, 60)
        x, y = x_and_y_components(ball.speed, ball_angle) 
        new_x, new_y = abs(x) / ball.speed, y / ball.speed

    elif ball.rect.colliderect(paddle.small_rect_rigth):
        ball.direction_x = 1
        ball.direction_y = -1

        ball_angle = random_angle_between(30, 60)
        x, y = x_and_y_components(ball.speed, ball_angle) 
        new_x, new_y = abs(x) / ball.speed, y / ball.speed


    # Update
    paddle.update(dt, 0, SCREEN_WIDTH)
    ball.rect.move_ip(ball.speed * abs(cos(ball_angle)) * ball.direction_x * dt, ball.speed * sin(ball_angle) * ball.direction_y * dt)

    
    # Draw objects on screen
    screen.fill((255,255,255))
    paddle.draw(screen)
    ball.draw(screen)
    pygame.draw.line(screen, (0, 0, 200), (ball.rect.centerx, ball.rect.centery), (ball.rect.centerx + new_x * 500 * ball.direction_x, ball.rect.centery + new_y * 500 * ball.direction_y))

    
    
    level_group.draw(screen)
            


    


    #update display
    pygame.display.update()

    #set max FPS to 60
    clock.tick(60)