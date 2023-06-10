import pygame
import constants as constants

class Pieces():
    def __init__(self, player, x, y):
        self.imageskey = self.getImagekey()
        self.image = constants.pieces_images[self.imageskey]
        self.x = x
        self.y = y
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.left = x * constants.square_size + 10
        self.rect.top = y * constants.square_size + 10

    def displayPieces(self, screen):
        self.rect.left = self.x * constants.square_size + 10
        self.rect.top = self.y * constants.square_size + 10
        screen.blit(self.image, self.rect)

    def getImagekey(self):
        return None
    
class King(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_king'
        else:
            return 'w_king'
        
class Prince(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_prince'
        else:
            return 'w_prince'