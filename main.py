import pygame
from sys import exit

import level
from snake import Snake
from fruit import Fruit

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((960, 960))
pygame.display.set_caption('Pygame Game')
clock = pygame.time.Clock()

background = level.Background(screen)
snake = Snake(screen)
fruit = Fruit(screen, snake)

# Event Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break

    if snake.gameOver != True:
        screen.fill((210, 180, 140))
        background.generate()
        snake.loop()
        fruit.loop()

    pygame.display.update()
    clock.tick(60) # Caps framerate at 60

# TODO Fruit
# TODO Snake