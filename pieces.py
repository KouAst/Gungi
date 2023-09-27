import pygame
import constants as constants

class Pieces():
    def __init__(self, player, x, y, z):
        self.imageskey = self.getImagekey()
        self.image = constants.pieces_images[self.imageskey]
        self.x = x
        self.y = y
        self.z = z
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.left = x * constants.square_size + 10
        self.rect.top = y * constants.square_size + 10

    def displayPieces(self, screen):
        self.rect.left = self.x * constants.square_size + 10
        self.rect.top = self.y * constants.square_size + 10 - (self.z-1)*5
        screen.blit(self.image, self.rect)

    def getImagekey(self):
        return None
    
    def canMove(self, arr, movex, movey, movez):
        pass
    
class King(Pieces):
    def __init__(self, player, x, y, z):
        self.player = player
        super().__init__(player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_king'
        else:
            return 'w_king'

    def canMove(self, arr, movex, movey, movez):
        if self.x == movex and self.y == movey:
            return False
        if arr[movex][movey][movez] == self.player:
            return False
        x = movex - self.x
        y = movey - self.y
        if abs(x) + abs(y) == 1: return True
        elif (x == 1) and (y == -1): return True
        elif (x == -1) and (y == -1): return True
        elif (x == -1) and (y == 1): return True
        elif (x == 1) and (y == 1): return True
        
class Prince(Pieces):
    def __init__(self, player, x, y, z):
        self.player = player
        super().__init__(player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_prince'
        else:
            return 'w_prince'

class Duke(Pieces):
    def __init__(self, player, x, y, z):
        self.player = player
        super().__init__(player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_duke'
        else:
            return 'w_duke'

class Spear(Pieces):
    def __init__(self, player, x, y, z):
        self.player = player
        super().__init__(player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_spear'
        else:
            return 'w_spear'  

class Shinobi(Pieces):
    def __init__(self, player, x, y, z):
        self.player = player
        super().__init__(player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_shinobi'
        else:
            return 'w_shinobi'

class Soldier(Pieces):
    def __init__(self, player, x, y, z):
        self.player = player
        super().__init__(player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_soldier'
        else:
            return 'w_soldier' 
        
class Fort(Pieces):
    def __init__(self, player, x, y, z):
        self.player = player
        super().__init__(player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_fort'
        else:
            return 'w_fort'
        
class Samurai(Pieces):
    def __init__(self, player, x, y, z):
        self.player = player
        super().__init__(player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_samurai'
        else:
            return 'w_samurai'

class Captain(Pieces):
    def __init__(self, player, x, y, z):
        self.player = player
        super().__init__(player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_captain'
        else:
            return 'w_captain' 

class Cavalry(Pieces):
    def __init__(self, player, x, y, z):
        self.player = player
        super().__init__(player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_cavalry'
        else:
            return 'w_cavalry'

def listPiecestoArr(piecesList):
    arr = [[[1 for k in range(3)] for i in range(9)] for j in range(15)]
    for i in range(0,15):
        for j in range(0,9):
            for k in range(1,3):
                if len(list(filter(lambda piece: piece.x == i and piece.y == j and piece.z == k and piece.player == constants.p1Color, piecesList))):
                    arr[i][j][k] = constants.p1Color
                elif len(list(filter(lambda piece: piece.x == i and piece.y == j and piece.z == k and piece.player == constants.p2Color, piecesList))):
                    arr[i][j][k] = constants.p2Color
                else:
                    arr[i][j][k] = 0
    return arr