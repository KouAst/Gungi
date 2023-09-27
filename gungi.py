import sys
import pygame
import time
import math
import threading
import constants as constants
import pieces as pieces

class gungi():
    window = None

    p1Color = constants.p1Color #Black
    p2Color = constants.p2Color #White

    selectedPiece = None
    turnFlag = p2Color
    newpieceFlag = 0
    z_axis = 0

    piecesList = []

    

    def startGame(self):
        pygame.init()
        gungi.window = pygame.display.set_mode((constants.screen_width,constants.screen_height))#,pygame.FULLSCREEN)
        pygame.display.set_caption('Gungi')        
        self.pieceInit()
        
        while True:
            time.sleep(0.1)
            self.drawBoard()
            self.pieceDisplay()
            self.getEvent()
            pygame.display.update()
            pygame.display.flip()      

    def drawBoard(self):
        for row in range(constants.row_size):
            for col in range(constants.col_size):
                if 0 <= col < 3:
                    x = col * constants.square_size
                    y = row * constants.square_size
                    pygame.draw.rect(self.window, constants.table_color, (x, y, constants.square_size, constants.square_size))
                elif 12 <= col < 15:
                    x = col * constants.square_size
                    y = row * constants.square_size
                    pygame.draw.rect(self.window, constants.table_color, (x, y, constants.square_size, constants.square_size))
                else:
                    x = col * constants.square_size
                    y = row * constants.square_size
                    pygame.draw.rect(self.window, constants.board_color, (x, y, constants.square_size, constants.square_size))
                    pygame.draw.rect(self.window, constants.line_color, (x, y, constants.square_size, constants.square_size), 1)
        
    def pieceInit(self):
        #p1
        gungi.piecesList.append(pieces.King(gungi.p1Color, 7, 0, 1))
        gungi.piecesList.append(pieces.Prince(gungi.p1Color, 6, 0, 1))
        gungi.piecesList.append(pieces.Duke(gungi.p1Color, 8, 0, 1))
        gungi.piecesList.append(pieces.Spear(gungi.p1Color, 7, 1, 1))
        gungi.piecesList.append(pieces.Shinobi(gungi.p1Color, 4, 1, 1))
        gungi.piecesList.append(pieces.Shinobi(gungi.p1Color, 10, 1, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 3, 2, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 7, 2, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 11, 2, 1))
        gungi.piecesList.append(pieces.Fort(gungi.p1Color, 5, 2, 1))
        gungi.piecesList.append(pieces.Fort(gungi.p1Color, 9, 2, 1))
        gungi.piecesList.append(pieces.Samurai(gungi.p1Color, 6, 2, 1))
        gungi.piecesList.append(pieces.Samurai(gungi.p1Color, 8, 2, 1))
        #p1備戰區
        gungi.piecesList.append(pieces.Captain(gungi.p1Color, 0, 0, 1))
        gungi.piecesList.append(pieces.Captain(gungi.p1Color, 0, 1, 1))
        gungi.piecesList.append(pieces.Spear(gungi.p1Color, 1, 0, 1))
        gungi.piecesList.append(pieces.Spear(gungi.p1Color, 1, 1, 1))
        gungi.piecesList.append(pieces.Cavalry(gungi.p1Color, 2, 0, 1))
        gungi.piecesList.append(pieces.Cavalry(gungi.p1Color, 2, 1, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 1, 2, 1))
        
        #p2
        gungi.piecesList.append(pieces.King(gungi.p2Color, 7, 8, 1))
        gungi.piecesList.append(pieces.Prince(gungi.p2Color, 6, 8, 1))
        gungi.piecesList.append(pieces.Duke(gungi.p2Color, 8, 8, 1))
        gungi.piecesList.append(pieces.Spear(gungi.p2Color, 7, 7, 1))
        gungi.piecesList.append(pieces.Shinobi(gungi.p2Color, 4, 7, 1))
        gungi.piecesList.append(pieces.Shinobi(gungi.p2Color, 10, 7, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 3, 6, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 7, 6, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 11, 6, 1))
        gungi.piecesList.append(pieces.Fort(gungi.p2Color, 5, 6, 1))
        gungi.piecesList.append(pieces.Fort(gungi.p2Color, 9, 6, 1))
        gungi.piecesList.append(pieces.Samurai(gungi.p2Color, 6, 6, 1))
        gungi.piecesList.append(pieces.Samurai(gungi.p2Color, 8, 6, 1))
        #p2備戰區
        gungi.piecesList.append(pieces.Captain(gungi.p2Color, 12, 8, 1))
        gungi.piecesList.append(pieces.Captain(gungi.p2Color, 12, 7, 1))
        gungi.piecesList.append(pieces.Spear(gungi.p2Color, 13, 8, 1))
        gungi.piecesList.append(pieces.Spear(gungi.p2Color, 13, 7, 1))
        gungi.piecesList.append(pieces.Cavalry(gungi.p2Color, 14, 8, 1))
        gungi.piecesList.append(pieces.Cavalry(gungi.p2Color, 14, 7, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 13, 6, 1))
        
    
    def pieceDisplay(self):
        for item in gungi.piecesList:
            item.displayPieces(gungi.window)

    def getEvent(self):
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                posx = pos[0]
                posy = pos[1]
                #print("posx:",posx,";","posy:",posy)
                x = math.floor(posx / 80)
                y = math.floor(posy / 80)
                print("x:",x,";","y:",y)
                self.select_piece(gungi.turnFlag,x,y)

    def exchangeTurn(self,t):
        gungi.newpieceFlag = 0

        if t == 1:
            gungi.turnFlag = 2
        elif t == 2:
            gungi.turnFlag = 1       

    def select_piece(self, turn, x, y):
        selectFilter = list(filter(lambda piece: piece.x == x and piece.y == y and piece.player == turn , gungi.piecesList))

        if len(selectFilter):
            gungi.selectedPiece = selectFilter[0]

            selectFilter.sort(key=lambda piece: piece.z, reverse=True)
            gungi.z_axis = selectFilter[0].z
            if(0 <= selectFilter[0].x < 3 and turn == 1 or 12 <= selectFilter[0].x < 15 and turn == 2):
                gungi.newpieceFlag = 1

            pieceName = gungi.selectedPiece.__class__.__name__
            print("Piece:"+ pieceName,";","z_axis:",gungi.z_axis)
            print("NewpieceFlag:",gungi.newpieceFlag)
            return

        if gungi.selectedPiece:
            arr = pieces.listPiecestoArr(gungi.piecesList)
            if gungi.newpieceFlag == 1:
                gungi.piece = gungi.selectedPiece
                self.placement_newpiece(turn,x,y,arr)
            
            else:
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.z_axis)
                    gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
        else:
            fi = filter(lambda p: p.x == x and p.y == y, gungi.piecesList)
            listfi = list(fi)
            if len(listfi) != 0:
                gungi.selectedPiece = listfi[0]  

    def placement_newpiece(self,turn,x,y,arr):
        if arr[x][y][0] == 0:
            gungi.piece.x, gungi.piece.y, gungi.piece.z = x, y, 0
            self.exchangeTurn(turn)
        elif arr[x][y][1] == 0:
            gungi.piece.x, gungi.piece.y, gungi.piece.z = x, y, 1
            self.exchangeTurn(turn)

    def move_piece(self, piece, x, y, z):
        for item in gungi.piecesList:
            if piece.player == gungi.turnFlag:
                if item.x == x and item.y == y:
                    gungi.piecesList.remove(item)
            else:
                print("Not Your Piece")
                return False
        
        piece.x, piece.y, piece.z = x, y, z

        print(str(piece)+" move to " +"x:"+str(x) +" y:"+str(y) +" z:"+str(z))
        print(str(piece.player) + str(gungi.turnFlag))
        self.exchangeTurn(gungi.turnFlag)
        return True

    def endGame(self):
        print("關閉")
        exit()


if __name__ == '__main__':
    gungi().startGame()  