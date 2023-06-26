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
        
    def canMove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if abs(move_x) + abs(move_y) == 1: return True
        elif (move_x == 1) and (move_y == -1): return True
        elif (move_x == -1) and (move_y == -1): return True
        elif (move_x == -1) and (move_y == 1): return True
        elif (move_x == 1) and (move_y == 1): return True
        
class Prince(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_prince'
        else:
            return 'w_prince'
    
    def canMove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if (move_x != 0) and (move_y == 0): return True
        elif (move_x == 0) and (move_y != 0): return True
        elif (move_x == 1) and (move_y == -1): return True
        elif (move_x == -1) and (move_y == -1): return True
        elif (move_x == -1) and (move_y == 1): return True
        elif (move_x == 1) and (move_y == 1): return True

class Duke(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_duke'
        else:
            return 'w_duke'

    def canMove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if abs(move_x) + abs(move_y) == 1: return True
        elif abs(move_x) == abs(move_y): return True   

class Spear(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_spear'
        else:
            return 'w_spear'  

    def canMove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if self.player == constants.p1Color:
            if (move_x == 0) and (abs(move_y) == 1): return True
            elif (move_x == 0) and (move_y == 2): return True
            elif (move_x == 1) and (move_y == 1): return True
            elif (move_x == -1) and (move_y == 1): return True
        elif self.player == constants.p2Color:
            if (move_x == 0) and (abs(move_y) == 1): return True
            elif (move_x == 0) and (move_y == -2): return True
            elif (move_x == 1) and (move_y == -1): return True
            elif (move_x == -1) and (move_y == -1): return True   

class Shinobi(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_shinobi'
        else:
            return 'w_shinobi'
        
    def canMove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if abs(move_x) == abs(move_y):
            if (abs(move_x) <= 2) and (abs(move_y) <= 2): return True

class Soldier(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_soldier'
        else:
            return 'w_soldier' 

    def canMove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if (move_x == 0) and (abs(move_y) == 1): return True
        
class Fort(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_fort'
        else:
            return 'w_fort'
        
    def canMove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if self.player == constants.p1Color:
            if (move_x == 0) and (move_y == 1): return True
            elif (abs(move_x) == 1) and (move_y == 0): return True
            elif (abs(move_x) == 1) and (move_y == -1): return True
        elif self.player == constants.p2Color:
            if (move_x == 0) and (move_y == -1): return True
            elif (abs(move_x) == 1) and (move_y == 0): return True
            elif (abs(move_x) == 1) and (move_y == 1): return True  
        
class Samurai(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_samurai'
        else:
            return 'w_samurai'
    
    def canMove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if self.player == constants.p1Color:
            if (move_x == 0) and (abs(move_y) == 1): return True
            elif (move_x == 1) and (move_y == 1): return True
            elif (move_x == -1) and (move_y == 1): return True
        elif self.player == constants.p2Color:
            if (move_x == 0) and (abs(move_y) == 1): return True
            elif (move_x == 1) and (move_y == -1): return True
            elif (move_x == -1) and (move_y == -1): return True   

class Captain(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_captain'
        else:
            return 'w_captain' 

    def canMove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if self.player == constants.p1Color:
            if abs(move_x) + abs(move_y) == 1: return True
            elif (move_x == 1) and (move_y == 1): return True
            elif (move_x == -1) and (move_y == 1): return True
        elif self.player == constants.p2Color:
            if abs(move_x) + abs(move_y) == 1: return True
            elif (move_x == 1) and (move_y == -1): return True
            elif (move_x == -1) and (move_y == -1): return True       

class Cavalry(Pieces):
    def __init__(self, player, x, y):
        self.player = player
        super().__init__(player, x, y)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_cavalry'
        else:
            return 'w_cavalry'
    
    def canMove(self, arr, moveto_x, moveto_y):
        if self.x == moveto_x and self.y == moveto_y:
            return False
        if arr[moveto_x][moveto_y] == self.player:
            return False
        move_x = moveto_x - self.x
        move_y = moveto_y - self.y
        if self.player == constants.p1Color:
            if abs(move_x) + abs(move_y) == 1: return True
            elif (move_x == 0) and (abs(move_y) == 2): return True
        elif self.player == constants.p2Color:
            if abs(move_x) + abs(move_y) == 1: return True
            elif (move_x == 0) and (abs(move_y) == 2): return True

def listPiecestoArr(piecesList):
    arr = [[0 for i in range(11)] for j in range(9)]
    for i in range(0,9):
        for j in range(0,11):
            if len(list(filter(lambda cm: cm.x == i and cm.y == j and cm.player == constants.p1Color,piecesList))):
                arr[i][j] = constants.p1Color
            elif len(list(filter(lambda cm: cm.x == i and cm.y == j and cm.player == constants.p2Color,piecesList))):
                arr[i][j] = constants.p2Color
    return arr