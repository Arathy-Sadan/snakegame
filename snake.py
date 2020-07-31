import pygame
import random

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

# food figure
foodImg = pygame.image.load('fruit.png')
foodX = random.randint(10, 735)
foodY = random.randint(10, 545)


def snake(x, y):
    screen.blit(snakeImg, (x, y))


def food(x, y):
    screen.blit(foodImg, (x, y))


# game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    snake(snakeX, snakeY)
    food(foodX, foodY)
    pygame.display.update()