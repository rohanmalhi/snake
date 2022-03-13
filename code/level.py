import pygame
class Background():
    def __init__(self, screen):
        self.screen = screen
        self.tileSize = 64
        self.levelMap = [
'X X X X X X X X',
' X X X X X X X ',
'X X X X X X X X',
' X X X X X X X ',
'X X X X X X X X',
' X X X X X X X ',
'X X X X X X X X',
' X X X X X X X ',
'X X X X X X X X',
' X X X X X X X ',
'X X X X X X X X',
' X X X X X X X ',
'X X X X X X X X',
' X X X X X X X ',
'X X X X X X X X',
]
    def generate(self):
        for rowIndex, row in enumerate(self.levelMap): # For each row in the level map
            for columnIndex, cell in enumerate(row): # For each column in the level map
                if cell == 'X': # 'X' cell indicates a ground tile
                    pygame.draw.rect(self.screen, (157, 216, 89), (columnIndex * self.tileSize, rowIndex * self.tileSize, self.tileSize, self.tileSize))
                elif cell == ' ':
                    pygame.draw.rect(self.screen, (148, 210, 82), (columnIndex * self.tileSize, rowIndex * self.tileSize, self.tileSize, self.tileSize))