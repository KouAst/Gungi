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
    
    def canMove(self, arr, moveto_x, moveto_y):
        pass
    
class King(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_king'
        else:
            return 'w_king'
        
    def canmove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if abs(move_x) + abs(move_y) == 1:
            return True
        
class Prince(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_prince'
        else:
            return 'w_prince'
        
def listPiecestoArr(piecesList):
    arr = [[0 for i in range(9)] for j in range(9)]
    for i in range(0,9):
        for j in range(0,9):
            if len(list(filter(lambda cm: cm.x == i and cm.y == j and cm.player == constants.p1Color,piecesList))):
                arr[i][j] = constants.p1Color
            elif len(list(filter(lambda cm: cm.x == i and cm.y == j and cm.player == constants.p2Color,piecesList))):
                arr[i][j] = constants.p2Color
    return arr