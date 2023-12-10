import pygame
import constants as constants

class Pieces():
    def __init__(self, piececode, player, x, y, z):
        self.imageskey = self.getImagekey()
        self.image = constants.pieces_images[self.imageskey]
        self.x = x
        self.y = y
        self.z = z
        self.piececode = piececode
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.left = x * constants.square_size + 10
        self.rect.top = y * constants.square_size + 10
        self.Allrange = []
        

    def displayPieces(self, screen):
        self.rect.left = self.x * constants.square_size + 10
        if self.z == 0:
            self.rect.top = self.y * constants.square_size + 10
        else:
            self.rect.top = self.y * constants.square_size + 5
        screen.blit(self.image, self.rect)

    def getImagekey(self):
        return None
    
    def canMove(self, arr, movex, movey, movez):
        pass

    def moveRange(self, screen):
        pass
    
    def bestMove(self):
        pass

class King(Pieces):
    def __init__(self, piececode, player, x, y, z):
        self.player = player
        super().__init__(piececode, player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_king'
        else:
            return 'w_king'

    def canMove(self, arr, movex, movey, movez):
        if movex < 3 or movex > 12: return False
        if self.x == movex and self.y == movey:
            return False
        #if arr[movex][movey][movez] == self.player:
            #return True
        x = movex - self.x
        y = movey - self.y
        
        if abs(x) + abs(y) == 1: return True
        elif (x == 1) and (y == -1): return True
        elif (x == -1) and (y == -1): return True
        elif (x == -1) and (y == 1): return True
        elif (x == 1) and (y == 1): return True 
    
        if (self.z==1):
            if (abs(x)==2 and abs (y) == 0) or (abs(x)==0 and abs (y) == 2): return True
            elif (x == 2) and (y == -2): return True
            elif (x == -2) and (y == -2): return True
            elif (x == -2) and (y == 2): return True
            elif (x == 2) and (y == 2): return True 

    def moveRange(self, screen):
        x = self.x * constants.square_size
        y = self.y * constants.square_size
        if(x+constants.r1 < 12*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
        pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
        pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
        if(x-constants.r1 > 2*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
        if(self.z == 1):
            if(x+constants.r2 <= 12*constants.square_size):
                if(self.x>4):
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
                if(self.x<10):
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)        
                pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y, constants.square_size, constants.square_size),5)
                if(x-constants.r2 > 2*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)
    
    
    def bestMove(self, arr):
        self.Allrange.clear()

        for i in range(3,13):
            for j in range(0,9):
                for k in range(0,2):
                    if self.canMove(arr,i,j,k)==True:
                        temp = (i,j)
                        if temp not in self.Allrange:
                            self.Allrange.append((i,j))
                        

class Prince(Pieces):
    def __init__(self, piececode, player, x, y, z):
        self.player = player
        super().__init__(piececode, player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_prince'
        else:
            return 'w_prince'
    
    def canMove(self, arr, movex, movey, movez):
        if movex < 3 or movex > 12: return False
        if self.x == movex and self.y == movey:
            return False
        #if arr[movex][movey][movez] == self.player:
            #return True
        x = movex - self.x
        y = movey - self.y
        min_Xrange = 3
        max_Xrange = 11
        min_Yrange = 0
        max_Yrange = 8
        if any(isinstance(piece, Pieces) for piece in arr): #若listPiecestoArr未運作
            arr = listPiecestoArr(arr)
        
        for piece in range(3,12):
            if arr[piece][movey][0]:
                if (piece  < self.x) and (piece > min_Xrange):
                    min_Xrange = piece            
                if (piece  > self.x) and (piece < max_Xrange):
                    max_Xrange = piece  
        for piece in range(0,9):            
            if arr[movex][piece][0]:
                if (piece  < self.y) and (piece > min_Yrange):
                    min_Yrange = piece
                if (piece  > self.y) and (piece < max_Yrange):
                    max_Yrange = piece
            
        if ((movex>=min_Xrange and movex<=max_Xrange) and y==0):     #無限制
            return True  
        elif (x==0 and (movey>=min_Yrange and movey<=max_Yrange)): return True
        elif (abs(x) == 1 and abs(y) == 1): return True
        if (self.z == 1):
            if(abs(x) == 2 and abs(y) == 2 and arr[int((self.x+movex)/2)][int((self.y+movey)/2)][0]==0): return True

    def moveRange(self, screen):
        x = self.x * constants.square_size
        y = self.y * constants.square_size
        temp=1
        if(x+constants.r1 <= 12*constants.square_size):
            if(x+constants.r1 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
            #pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
            #pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
            #pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y, constants.square_size, constants.square_size),5)
            for temp in range(9-self.y):
                pygame.draw.rect(screen, constants.range_color, (x, y+temp*constants.r1, constants.square_size, constants.square_size),5)
            for temp in range(abs(0-self.y-1)):
                pygame.draw.rect(screen, constants.range_color, (x, y-temp*constants.r1, constants.square_size, constants.square_size),5)
            for temp in range(12-self.x):
                pygame.draw.rect(screen, constants.range_color, (x+temp*constants.r1, y, constants.square_size, constants.square_size),5)
        if(x-constants.r1 > 2*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
            #pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y, constants.square_size, constants.square_size),5)
            for temp in range(abs(2-self.x)):
                pygame.draw.rect(screen, constants.range_color, (x-temp*constants.r1, y, constants.square_size, constants.square_size),5)

        if(self.z == 1):
            if(x+constants.r2 <= 12*constants.square_size):
                if(self.x>4):
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
                if(self.x<10):
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)

    def bestMove(self, arr):
        self.Allrange.clear()

        for i in range(3,13):
            for j in range(0,9):
                for k in range(0,2):
                    if self.canMove(arr,i,j,k)==True:
                        temp = (i,j)
                        if temp not in self.Allrange:
                            self.Allrange.append((i,j))

class Duke(Pieces):
    def __init__(self, piececode, player, x, y, z):
        self.player = player
        super().__init__(piececode, player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_duke'
        else:
            return 'w_duke'

    def canMove(self, arr, movex, movey, movez):
        if movex < 3 or movex > 12: return False
        if self.x == movex and self.y == movey:
            return False
        #if arr[movex][movey][movez] == self.player:
            #return True
        x = movex - self.x
        y = movey - self.y
        min_Xrange = 3  
        max_Xrange = 11  
        min_Yrange = 0
        max_Yrange = 9
        if any(isinstance(piece, Pieces) for piece in arr): #若listPiecestoArr未運作
            arr = listPiecestoArr(arr)

        for piece in range(3,12):
            if arr[piece][movey][0]:
                if (piece  < self.x) and (piece > min_Xrange):
                    min_Xrange = piece            
                if (piece  > self.x) and (piece < max_Xrange):
                    max_Xrange = piece  
        for piece in range(0,9):            
            if arr[movex][piece][0]:
                if (piece  < self.y) and (piece > min_Yrange):
                    min_Yrange = piece
                if (piece  > self.y) and (piece < max_Yrange):
                    max_Yrange = piece    
        if((abs(x) == 1 and abs(y) == 0) or abs(x) == 0 and abs(y) == 1): return True
        
        elif (abs(x) == abs(y)):
            for i in range(1, abs(x)):
                if arr[self.x + i * (x//abs(x))][self.y + i * (y//abs(y))][0] != 0:
                    return False
            return True
    
        if (self.z == 1):
            if(abs(x) == 2 and abs(y) == 0) and arr[int((self.x+movex)/2)][self.y][0]==0:
                return True
            elif(abs(x)==0 and abs(y)==2) and arr[self.x][int((self.y+movey)/2)][0]==0: 
                return True
        
    def moveRange(self, screen):
        x = self.x * constants.square_size
        y = self.y * constants.square_size
        temp=1
        if(x+constants.r1 < 12*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y, constants.square_size, constants.square_size),5)
            for temp in range(12-self.x):
                pygame.draw.rect(screen, constants.range_color, (x+temp*constants.r1, y+temp*constants.r1, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x+temp*constants.r1, y-temp*constants.r1, constants.square_size, constants.square_size),5)
        pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
        pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
        if(x-constants.r1 > 2*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y, constants.square_size, constants.square_size),5)
            for temp in range(abs(2-self.x)):
                pygame.draw.rect(screen, constants.range_color, (x-temp*constants.r1, y+temp*constants.r1, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x-temp*constants.r1, y-temp*constants.r1, constants.square_size, constants.square_size),5)
        if(self.z == 1):
            if(x+constants.r2 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y, constants.square_size, constants.square_size),5)
            if(x-constants.r2 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)

    def bestMove(self, arr):
        self.Allrange.clear()

        for i in range(3,13):
            for j in range(0,9):
                for k in range(0,2):
                    if self.canMove(arr,i,j,k)==True:
                        temp = (i,j)
                        if temp not in self.Allrange:
                            self.Allrange.append((i,j))

class Spear(Pieces):
    def __init__(self, piececode, player, x, y, z):
        self.player = player
        super().__init__(piececode, player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_spear'
        else:
            return 'w_spear'

    def canMove(self, arr, movex, movey, movez):
        if movex < 3 or movex > 12: return False
        if self.x == movex and self.y == movey:
            return False
        #if arr[movex][movey][movez] == self.player:
            #return True
        x = movex - self.x
        y = movey - self.y
        if any(isinstance(piece, Pieces) for piece in arr): #若listPiecestoArr未運作
            arr = listPiecestoArr(arr)

        if(self.player == constants.p1Color):
            if(x == 0) and (abs(y) == 1): return True
            if(x == 0) and (y == 2) and arr[movex][(self.y+movey)//2][0]==0: return True
            if(x == 1) and (y == 1): return True
            if(x == -1) and (y == 1): return True
            if(self.z == 1):
                if(x == 0) and (y == -2) and arr[movex][(self.y+movey)//2][0]==0: return True
                if(x == 0) and (y == 3) and (arr[movex][(self.y+movey)//2][0]==0 or arr[movex][(self.y+movey)//2+1][0]==0): return True
                if(x == 2) and (y == 2) and arr[(self.x+movex)//2][(self.y+movey)//2][0]==0: return True
                if(x == -2) and (y == 2) and arr[(self.x+movex)//2][(self.y+movey)//2][0]==0: return True
        if(self.player == constants.p2Color):
            if(x == 0) and (abs(y) == 1): return True
            if(x == 0) and (y == -2) and arr[movex][(self.y+movey)//2][0]==0: return True
            if(x == 1) and (y == -1): return True
            if(x == -1) and (y == -1): return True
            if(self.z == 1):
                if(x == 0) and (y == 2) and arr[movex][(self.y+movey)//2][0]==0: return True
                if(x == 0) and (y == -3) and arr[movex][(self.y+movey)//2][0]==0 and arr[movex][(self.y+movey)//2+1][0]==0: return True
                if(x == 2) and (y == -2) and arr[(movex+self.x)//2][(self.y+movey)//2][0]==0: return True
                if(x == -2) and (y == -2) and arr[(movex+self.x)//2][(self.y+movey)//2][0]==0: return True
    
        
    def moveRange(self, screen):
        x = self.x * constants.square_size
        y = self.y * constants.square_size
        if(self.player == constants.p1Color):
            if(x+constants.r1 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            if(x-constants.r1 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
            if(self.z == 1):
                pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)
                if(x+constants.r2 < 12*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
                if(x-constants.r2 > 2*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
        if(self.player == constants.p2Color):
            if(x+constants.r1 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
            if(x-constants.r1 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
            if(self.z == 1):
                pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x, y-constants.r3, constants.square_size, constants.square_size),5)
                if(x+constants.r2 < 12*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)
                if(x-constants.r2 > 2*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)

    def bestMove(self, arr):
        self.Allrange.clear()

        for i in range(3,13):
            for j in range(0,9):
                for k in range(0,2):
                    if self.canMove(arr,i,j,k)==True:
                        temp = (i,j)
                        if temp not in self.Allrange:
                            self.Allrange.append((i,j))

class Shinobi(Pieces):
    def __init__(self, piececode, player, x, y, z):
        self.player = player
        super().__init__(piececode, player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_shinobi'
        else:
            return 'w_shinobi'
        
    def canMove(self, arr, movex, movey, movez):
        if movex < 3 or movex > 12: return False
        if self.x == movex and self.y == movey:
            return False
        #if arr[movex][movey][movez] == self.player:
            #return True
        x = movex - self.x
        y = movey - self.y
        if any(isinstance(piece, Pieces) for piece in arr): #若listPiecestoArr未運作
            arr = listPiecestoArr(arr)

        if(abs(x)==1 and abs(y)==1): return True
        if(abs(x)==2 and abs(y)==2) and arr[(self.x+movex)//2][(self.y+movey)//2][0]==0: return True
        if(self.z == 1):
            if(abs(x)==3 and abs(y)==3):
                if(arr[(self.x+movex)//2][(self.y+movey)//2][0]==0 and arr[(self.x+movex)//2+1][(self.y+movey)//2+1][0]==0 and self.x > movex and self.y > movey): return True #斜左上
                elif(arr[(self.x+movex)//2+1][(self.y+movey)//2][0]==0 and arr[(self.x+movex)//2][(self.y+movey)//2+1][0]==0 and self.x > movex and self.y < movey): return True #斜左下
                elif(arr[(self.x+movex)//2][(self.y+movey)//2+1][0]==0 and arr[(self.x+movex)//2+1][(self.y+movey)//2][0]==0 and self.x < movex and self.y > movey): return True #右上
                elif(arr[(self.x+movex)//2][(self.y+movey)//2][0]==0 and arr[(self.x+movex)//2+1][(self.y+movey)//2+1][0]==0 and self.x < movex and self.y < movey): return True #右下
    
    def moveRange(self, screen):
        x = self.x * constants.square_size
        y = self.y * constants.square_size
        if(x+constants.r1 < 12*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
        if(x+constants.r2 < 12*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)
        if(x-constants.r1 > 2*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
        if(x-constants.r2 > 2*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)
        if(self.z == 1):
            if(x+constants.r3 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x+constants.r3, y+constants.r3, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x+constants.r3, y-constants.r3, constants.square_size, constants.square_size),5)
            if(x-constants.r3 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x-constants.r3, y+constants.r3, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x-constants.r3, y-constants.r3, constants.square_size, constants.square_size),5)

    def bestMove(self, arr):
        self.Allrange.clear()

        for i in range(3,13):
            for j in range(0,9):
                for k in range(0,2):
                    if self.canMove(arr,i,j,k)==True:
                        temp = (i,j)
                        if temp not in self.Allrange:
                            self.Allrange.append((i,j))

class Soldier(Pieces):
    def __init__(self, piececode, player, x, y, z):
        self.player = player
        super().__init__(piececode, player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_soldier'
        else:
            return 'w_soldier'
        
    def canMove(self, arr, movex, movey, movez):
        if movex < 3 or movex > 12: return False
        if self.x == movex and self.y == movey:
            return False
        #if arr[movex][movey][movez] == self.player:
            #return True
        x = movex - self.x
        y = movey - self.y
        if any(isinstance(piece, Pieces) for piece in arr): #若listPiecestoArr未運作
            arr = listPiecestoArr(arr)
        if (abs(x)== 0 and abs(y)==1): return True
        if (self.z ==1):
            if(abs(x)== 0 and abs(y)==2) and arr[movex][(self.y+movey)//2][0]==0: return True
    
    def moveRange(self, screen):
        x = self.x * constants.square_size
        y = self.y * constants.square_size
        pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
        pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
        if(self.z== 1):
            pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)

    def bestMove(self, arr):
        self.Allrange.clear()

        for i in range(3,13):
            for j in range(0,9):
                for k in range(0,2):
                    if self.canMove(arr,i,j,k)==True:
                        temp = (i,j)
                        if temp not in self.Allrange:
                            self.Allrange.append((i,j))

class Fort(Pieces):
    def __init__(self, piececode, player, x, y, z):
        self.player = player
        super().__init__(piececode, player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_fort'
        else:
            return 'w_fort'
        
    def canMove(self, arr, movex, movey, movez):
        if movex < 3 or movex > 12: return False
        if self.x == movex and self.y == movey:
            return False
        #if arr[movex][movey][movez] == self.player:
            #return True
        x = movex - self.x
        y = movey - self.y
        if any(isinstance(piece, Pieces) for piece in arr): #若listPiecestoArr未運作
            arr = listPiecestoArr(arr)

        if(self.player == constants.p1Color):
            if(x == 0 and y == 1): return True
            if(abs(x) == 1 and y == 0): return True
            if(abs(x) == 1 and y == -1): return True
            if(self.z == 1):
                if(x == 0 and y == 2) and arr[movex][(self.y+movey)//2][0]==0: return True
                if(abs(x) == 2 and y == 0): return True
                if(abs(x) == 2 and y == -2) and arr[(self.x+movex)//2][(self.y+movey)//2][0]==0: return True
        if(self.player == constants.p2Color):
            if(x == 0 and y == -1): return True
            if(abs(x) == 1 and y == 0): return True
            if(abs(x) == 1 and y == 1): return True
            if(self.z == 1):
                if(x == 0 and y == -2): return True
                if(abs(x) == 2 and y == 0) and arr[(self.x+movex)//2][movey][0]==0: return True
                if(abs(x) == 2 and y == 2) and arr[(self.x+movex)//2][(self.y+movey)//2][0]==0: return True  

    def moveRange(self, screen):
        x = self.x * constants.square_size
        y = self.y * constants.square_size
        if(self.player == constants.p1Color):
            if(x+constants.r1 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
            if(x-constants.r1 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
            if(self.z == 1):
                if(x+constants.r2 < 12*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)
                if(x-constants.r2 > 2*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)
        if(self.player == constants.p2Color):
            if(x+constants.r1 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            if(x-constants.r1 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            if(self.z == 1):
                if(x+constants.r2 < 12*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
                if(x-constants.r2 > 2*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)

    def bestMove(self, arr):
        self.Allrange.clear()

        for i in range(3,13):
            for j in range(0,9):
                for k in range(0,2):
                    if self.canMove(arr,i,j,k)==True:
                        temp = (i,j)
                        if temp not in self.Allrange:
                            self.Allrange.append((i,j))

class Samurai(Pieces):
    def __init__(self, piececode, player, x, y, z):
        self.player = player
        super().__init__(piececode, player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_samurai'
        else:
            return 'w_samurai'

    def canMove(self, arr, movex, movey, movez):
        if movex < 3 or movex > 12: return False
        if self.x == movex and self.y == movey:
            return False
        #if arr[movex][movey][movez] == self.player:
            #return True
        x = movex - self.x
        y = movey - self.y
        if any(isinstance(piece, Pieces) for piece in arr): #若listPiecestoArr未運作
            arr = listPiecestoArr(arr)

        if(self.player == constants.p1Color):
            if(x == 0 and abs(y) == 1): return True
            if(abs(x) == 1 and y == 1): return True
            if(self.z == 1):
                if(x == 0 and abs(y) == 2) and arr[movex][(self.y+movey)//2][0]==0: return True
                if(abs(x) == 2 and y == 2) and arr[(self.x+movex)//2][(self.y+movey)//2][0]==0: return True
        if(self.player == constants.p2Color):
            if(x == 0 and abs(y) == 1): return True
            if(abs(x) == 1 and y == -1): return True
            if(self.z == 1):
                if(x == 0 and abs(y) == 2) and arr[movex][(self.y+movey)//2][0]==0: return True
                if(abs(x) == 2 and y == -2) and arr[(self.x+movex)//2][(self.y+movey)//2][0]==0: return True        
 
    def moveRange(self, screen):
        x = self.x * constants.square_size
        y = self.y * constants.square_size
        if(self.player == constants.p1Color):
            pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
            if(x+constants.r1 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            if(x-constants.r1 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
            if(self.z == 1):
                pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)
                if(x+constants.r2 < 12*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
                if(x-constants.r2 > 2*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
        if(self.player == constants.p2Color):
            pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
            if(x+constants.r1 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
            if(x-constants.r1 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
            if(self.z == 1):
                pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)
                if(x+constants.r2 < 12*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)
                if(x-constants.r2 > 2*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)

    def bestMove(self, arr):
        self.Allrange.clear()

        for i in range(3,13):
            for j in range(0,9):
                for k in range(0,2):
                    if self.canMove(arr,i,j,k)==True:
                        temp = (i,j)
                        if temp not in self.Allrange:
                            self.Allrange.append((i,j))

class Captain(Pieces):
    def __init__(self, piececode, player, x, y, z):
        self.player = player
        super().__init__(piececode, player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_captain'
        else:
            return 'w_captain' 

    def canMove(self, arr, movex, movey, movez):
        if movex < 3 or movex > 12: return False
        if self.x == movex and self.y == movey:
            return False
        #if arr[movex][movey][movez] == self.player:
            #return True
        x = movex - self.x
        y = movey - self.y
        if any(isinstance(piece, Pieces) for piece in arr): #若listPiecestoArr未運作
            arr = listPiecestoArr(arr)

        if(self.player == constants.p1Color):
            if(x == 0 and abs(y) == 1): return True
            if(abs(x) == 1 and y == 1): return True
            if(abs(x) == 1 and y == 0): return True
            if(self.z == 1):
                if(x == 0 and abs(y) == 2) and arr[movex][(self.y+movey)//2][0]==0: return True
                if(abs(x) == 2 and y == 2) and arr[(self.x+movex)//2][(self.y+movey)//2][0]==0: return True
                if(abs(x) == 2 and y == 0) and arr[(self.x+movex)//2][movey][0]==0: return True
        if(self.player == constants.p2Color):
            if(x == 0 and abs(y) == 1): return True
            if(abs(x) == 1 and y == -1): return True
            if(abs(x) == 1 and y == 0): return True
            if(self.z == 1):
                if(x == 0 and abs(y) == 2) and arr[movex][(self.y+movey)//2][0]==0: return True
                if(abs(x) == 2 and y == -2) and arr[(self.x+movex)//2][(self.y+movey)//2][0]==0: return True
                if(abs(x) == 2 and y == 0) and arr[(self.x+movex)//2][movey][0]==0: return True

    def moveRange(self, screen):
        x = self.x * constants.square_size
        y = self.y * constants.square_size
        if(self.player == constants.p1Color):
            pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
            if(x+constants.r1 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y, constants.square_size, constants.square_size),5)
            if(x-constants.r1 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y+constants.r1, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y, constants.square_size, constants.square_size),5)
            if(self.z == 1):
                pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)
                if(x+constants.r2 < 12*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y, constants.square_size, constants.square_size),5)
                if(x-constants.r2 > 2*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y+constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y, constants.square_size, constants.square_size),5)
        if(self.player == constants.p2Color):
            pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
            if(x+constants.r1 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y, constants.square_size, constants.square_size),5)
            if(x-constants.r1 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y-constants.r1, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y, constants.square_size, constants.square_size),5)
            if(self.z == 1):
                pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
                pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)
                if(x+constants.r2 < 12*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y, constants.square_size, constants.square_size),5)
                if(x-constants.r2 > 2*constants.square_size):
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y-constants.r2, constants.square_size, constants.square_size),5)
                    pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y, constants.square_size, constants.square_size),5)

    def bestMove(self, arr):
        self.Allrange.clear()

        for i in range(3,13):
            for j in range(0,9):
                for k in range(0,2):
                    if self.canMove(arr,i,j,k)==True:
                        temp = (i,j)
                        if temp not in self.Allrange:
                            self.Allrange.append((i,j))

class Cavalry(Pieces):
    def __init__(self, piececode, player, x, y, z):
        self.player = player
        super().__init__(piececode, player, x, y, z)

    def getImagekey(self):
        if self.player == constants.p1Color:
            return 'b_cavalry'
        else:
            return 'w_cavalry'

    def canMove(self, arr, movex, movey, movez):
        if movex < 3 or movex > 12: return False
        if self.x == movex and self.y == movey:
            return False
        #if arr[movex][movey][movez] == self.player:
            #return True
        x = movex - self.x
        y = movey - self.y
        if any(isinstance(piece, Pieces) for piece in arr): #若listPiecestoArr未運作
            arr = listPiecestoArr(arr)
        if(x == 0 and abs(y) == 1): return True
        if(x == 0 and abs(y) == 2) and arr[movex][(self.y+movey)//2][0]==0: return True
        if(abs(x) == 1 and y == 0): return True
        if(self.z == 1):
            if(x == 0 and abs(y) == 3) and arr[movex][(self.y+movey)//2][0]==0 and arr[movex][(self.y+movey)//2+1][0]==0: return True
            if(abs(x) == 2 and y == 0) and arr[(self.x+movex)//2][movey][0]==0: return True

    def moveRange(self, screen):
        x = self.x * constants.square_size
        y = self.y * constants.square_size
        pygame.draw.rect(screen, constants.range_color, (x, y+constants.r1, constants.square_size, constants.square_size),5)
        pygame.draw.rect(screen, constants.range_color, (x, y+constants.r2, constants.square_size, constants.square_size),5)
        pygame.draw.rect(screen, constants.range_color, (x, y-constants.r1, constants.square_size, constants.square_size),5)
        pygame.draw.rect(screen, constants.range_color, (x, y-constants.r2, constants.square_size, constants.square_size),5)
        if(x+constants.r1 < 12*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x+constants.r1, y, constants.square_size, constants.square_size),5)
        if(x-constants.r1 > 2*constants.square_size):
            pygame.draw.rect(screen, constants.range_color, (x-constants.r1, y, constants.square_size, constants.square_size),5)
        if(self.z == 1):
            pygame.draw.rect(screen, constants.range_color, (x, y+constants.r3, constants.square_size, constants.square_size),5)
            pygame.draw.rect(screen, constants.range_color, (x, y-constants.r3, constants.square_size, constants.square_size),5)
            if(x+constants.r2 < 12*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x+constants.r2, y, constants.square_size, constants.square_size),5)
            if(x-constants.r2 > 2*constants.square_size):
                pygame.draw.rect(screen, constants.range_color, (x-constants.r2, y, constants.square_size, constants.square_size),5)

    def bestMove(self, arr):
        self.Allrange.clear()

        for i in range(3,13):
            for j in range(0,9):
                for k in range(0,2):
                    if self.canMove(arr,i,j,k)==True:
                        temp = (i,j)
                        if temp not in self.Allrange:
                            self.Allrange.append((i,j))

def listPiecestoArr(piecesList):
    arr = [[[0 for k in range(2)] for i in range(9)] for j in range(15)]
    for i in range(0,15):
        for j in range(0,9):
            for k in range(0,2):
                if len(list(filter(lambda piece: piece.x == i and piece.y == j and piece.z == k and piece.player == constants.p1Color, piecesList))):
                    arr[i][j][k] = constants.p1Color
                elif len(list(filter(lambda piece: piece.x == i and piece.y == j and piece.z == k and piece.player == constants.p2Color, piecesList))):
                    arr[i][j][k] = constants.p2Color
                else:
                    arr[i][j][k] = 0
    return arr