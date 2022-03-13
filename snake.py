from tkinter import RIGHT
import pygame

# TODO Movement
# TODO Collision

class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.partsList = {'head' : [5, 8], 'body1' : [4, 8], 'body2' : [3, 8], 'body3' : [2, 8], 'body4' : [1, 8]}
        self.oldPartsList = self.partsList


        self.headSurface = pygame.transform.rotate(pygame.image.load('head.png'), -90)
        self.headRect = self.headSurface.get_rect(topleft = (self.partsList['head'][0] * 64, self.partsList['head'][1] * 64))
        self.bodySurface = pygame.image.load('body.png')
        self.bodyRect = self.bodySurface.get_rect(topleft = (0, 0))
        self.tailSurface = pygame.image.load('tail.png')
        self.direction = 'right'

    def render(self):
        for item in self.partsList.keys():
            if item == 'head':
                self.screen.blit(self.headSurface, self.headRect)
            if item.index == len(self.partsList):
                self.bodyRect.topleft = (self.partsList[item][0] * 64, self.partsList[item][1] * 64)
                self.screen.blit(self.tailSurface, self.bodyRect)
            elif item[0] == 'b' and item.index != len(self.partsList):
                self.bodyRect.topleft = (self.partsList[item][0] * 64, self.partsList[item][1] * 64)
                self.screen.blit(self.bodySurface, self.bodyRect)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction = 'right'
        elif keys[pygame.K_a]:
            self.direction = 'left'
        elif keys[pygame.K_w]:
            self.direction = 'up'
        elif keys[pygame.K_s]:
            self.direction = 'down'

    def move(self):
        self.oldPartsList = self.partsList
        for item in self.partsList.keys():
            pass

    def loop(self):
        self.render()
        self.input()


    