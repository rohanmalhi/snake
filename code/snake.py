import pygame
from copy import deepcopy

from leng import leng

class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.partsList = {'head' : [5, 8], 'body1' : [4, 8], 'body2' : [3, 8], 'body3' : [2, 8], 'body4' : [1, 8]}
        self.oldPartsList = self.partsList
        self.snakeLength = 4

        self.deathSound = pygame.mixer.Sound('..\sounds\death.wav')

        self.gameOver = False

        self.moveIndex = 0
        self.direction = 'right'

        self.headSurface = pygame.transform.rotate(pygame.image.load('../graphics\head.png'), -90)
        self.headRect = self.headSurface.get_rect(topleft = (self.partsList['head'][0] * 64, self.partsList['head'][1] * 64))
        self.bodySurface = pygame.image.load(r'../graphics\body.png')
        self.bodyRect = self.bodySurface.get_rect(topleft = (0, 0))
        self.tailSurface = pygame.image.load('../graphics/tail.png')
        

    def render(self):
        for item in self.partsList.keys():
            if item == 'head':
                self.screen.blit(self.headSurface, self.headRect)
            # if item == self.partsList[f'body{self.snakeLength}']:
            #     self.bodyRect.topleft = (self.partsList[item][0] * 64, self.partsList[item][1] * 64)
            #     self.screen.blit(self.tailSurface, self.bodyRect)
            elif item[0] == 'b' and item.index != self.snakeLength:
                if self.direction == 'down' or self.direction =='up':
                    if self.partsList[item][0] == self.partsList['head'][0]:
                        self.bodyRect.topleft = (self.partsList[item][0] * 64, self.partsList[item][1] * 64)
                        self.screen.blit(pygame.transform.rotate(self.bodySurface, 90), self.bodyRect)
                    else:
                        self.bodyRect.topleft = (self.partsList[item][0] * 64, self.partsList[item][1] * 64)
                        self.screen.blit(self.bodySurface, self.bodyRect)
                elif self.direction =='right' or self.direction == 'left':
                    if self.partsList[item][1] == self.partsList['head'][1]:
                        self.bodyRect.topleft = (self.partsList[item][0] * 64, self.partsList[item][1] * 64)
                        self.screen.blit(self.bodySurface, self.bodyRect)
                    else:
                        self.bodyRect.topleft = (self.partsList[item][0] * 64, self.partsList[item][1] * 64)
                        self.screen.blit(pygame.transform.rotate(self.bodySurface, 90), self.bodyRect)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if self.direction != 'left':
                self.direction = 'right'
        elif keys[pygame.K_a]:
            if self.direction != 'right':
                self.direction = 'left'
        elif keys[pygame.K_w]:
            if self.direction != 'down':
                self.direction = 'up'
        elif keys[pygame.K_s]:
            if self.direction != 'up':
                self.direction = 'down'

    def move(self):
        self.moveIndex += 0.2
        if int(self.moveIndex) == 1:
            self.moveIndex = 0
            self.oldPartsList = deepcopy(self.partsList)
            for item in self.partsList.keys():
                if item == 'head':
                    if self.direction == 'right':
                        self.partsList['head'][0] += 1
                        self.headSurface = pygame.transform.rotate(pygame.image.load('../graphics\head.png'), -90)
                        self.headRect = self.headSurface.get_rect(topleft = (self.partsList['head'][0] * 64, self.partsList['head'][1] * 64))
                    elif self.direction == 'up':
                        self.partsList['head'][1] -= 1
                        self.headSurface = pygame.image.load('../graphics/head.png')
                        self.headRect = self.headSurface.get_rect(topleft = (self.partsList['head'][0] * 64, self.partsList['head'][1] * 64))
                    elif self.direction == 'down':
                        self.partsList['head'][1] += 1
                        self.headSurface = pygame.transform.rotate(pygame.image.load('..\graphics\head.png'), 180)
                        self.headRect = self.headSurface.get_rect(topleft = (self.partsList['head'][0] * 64, self.partsList['head'][1] * 64))
                    else:
                        self.partsList['head'][0] -= 1
                        self.headSurface = pygame.transform.rotate(pygame.image.load('..\graphics\head.png'), 90)
                        self.headRect = self.headSurface.get_rect(topleft = (self.partsList['head'][0] * 64, self.partsList['head'][1] * 64))
                if item[0] == 'b':
                    if item[4] == '1' and leng(item) == 5:
                        self.partsList[item] = self.oldPartsList['head']
                    else:
                        if leng(item) == 5:
                            self.partsList[item] = self.oldPartsList[f'body{int(item[4]) - 1}']
                        elif leng(item) == 6:
                             self.partsList[item] = self.oldPartsList[f'body{int(item[4] + item[5]) - 1}']
                        elif leng(item) == 7:
                             self.partsList[item] = self.oldPartsList[f'body{int(item[4] + item[5] + item[6]) - 1}']

    def collision(self):
        for body in self.partsList:
            if self.partsList[body] == self.partsList['head'] and body != 'head':
                self.gameOver = True
                self.deathSound.play()
        if (self.partsList['head'][0] < 0 or self.partsList['head'][0] > 14) or (self.partsList['head'][1] < 0 or self.partsList['head'][1] > 15):
            self.gameOver = True
            self.deathSound.play()
                        


    def loop(self):
        self.input()
        self.move()
        self.render()
        self.collision()


    