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
font = pygame.font.Font('..\graphics\Pixeltype.ttf', 50)
fontSurface = font.render(f'{fruit.score}', False, 'white')
fontRect = fontSurface.get_rect(center = (480, 32))

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
        fontSurface = font.render(f'{fruit.score}', False, 'white')
        screen.blit(fontSurface, fontRect)
    else:
        screen.blit(snake.headSurface, (snake.partsList['body1'][0] * 64, snake.partsList['body1'][1] * 64))

    pygame.display.update()
    clock.tick(60) # Caps framerate at 60
