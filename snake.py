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
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

# game over
over_font = pygame.font.Font("freesansbold.ttf", 64)


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


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    game_over = over_font.render("Game Over ", True, (0, 255, 0))
    screen.blit(game_over, (200, 250))


# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snakeX_change = -.5
            if event.key == pygame.K_RIGHT:
                snakeX_change = .5
            if event.key == pygame.K_UP:
                snakeY_change = -.5
            if event.key == pygame.K_DOWN:
                snakeY_change = .5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                snakeX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                snakeY_change = 0
        # collision
        collision = is_collision(snakeX, snakeY, foodX, foodY)
        if collision:
            score_value += 1
            foodX = random.randint(10, 735)
            foodY = random.randint(10, 545)
    snakeX += snakeX_change
    snakeY += snakeY_change
    if snakeY > 550 or snakeY < 5 or snakeX > 735 or snakeX < 10:
        snakeX = 2000
        game_over_text()

    snake(snakeX, snakeY)
    food(foodX, foodY)
    show_score(10, 10)
    pygame.display.update()
