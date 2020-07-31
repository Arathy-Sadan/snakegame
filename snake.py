import pygame
import random
import math

# initialize pygame
pygame.init()

# create window
screen = pygame.display.set_mode((800, 600))

# tittle & logo
title = pygame.display.set_caption("Snake Game")
logo = pygame.image.load('snake.png')
pygame.display.set_icon(logo)

# Snake figure
snakeImg = pygame.image.load('snakeplayer.png')
snakeX = 370
snakeY = 450
snakeX_change = 0
snakeY_change = 0

# food figure
foodImg = pygame.image.load('fruit.png')
foodX = random.randint(10, 735)
foodY = random.randint(10, 545)


# score
score = 0


# collision
def is_collision(snakeX, snakeY, foodX, foodY):
    distance = math.sqrt((math.pow(snakeX - foodX, 2)) + (math.pow(snakeY - foodY, 2)))
    if distance < 47:
        return True
    else:
        return False


def snake(x, y):
    screen.blit(snakeImg, (x, y))


def food(x, y):
    screen.blit(foodImg, (x, y))


# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snakeX_change = -.1
            if event.key == pygame.K_RIGHT:
                snakeX_change = .1
            if event.key == pygame.K_UP:
                snakeY_change = -.1
            if event.key == pygame.K_DOWN:
                snakeY_change = .1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                snakeX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                snakeY_change = 0
        # collision
        collision = is_collision(snakeX, snakeY, foodX, foodY)
        if collision:
            score += 1
            print(score)
            foodX = random.randint(10, 735)
            foodY = random.randint(10, 545)

    snakeX += snakeX_change
    snakeY += snakeY_change
    snake(snakeX, snakeY)
    food(foodX, foodY)
    pygame.display.update()
