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
    chooseFlag = 0
    tempZFlag = 0
    moveFlag = 0
    piece = None
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
            self.rangeDisplay()
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
        gungi.piecesList.append(pieces.King(1,gungi.p1Color, 7, 0, 0))
        gungi.piecesList.append(pieces.Prince(2,gungi.p1Color, 6, 0, 0))
        gungi.piecesList.append(pieces.Duke(3,gungi.p1Color, 8, 0, 0))
        gungi.piecesList.append(pieces.Spear(4,gungi.p1Color, 7, 1, 0))
        gungi.piecesList.append(pieces.Shinobi(5,gungi.p1Color, 4, 1, 0))
        gungi.piecesList.append(pieces.Shinobi(5,gungi.p1Color, 10, 1, 0))
        gungi.piecesList.append(pieces.Soldier(6,gungi.p1Color, 3, 2, 0))
        gungi.piecesList.append(pieces.Soldier(6,gungi.p1Color, 7, 2, 0))
        gungi.piecesList.append(pieces.Soldier(6,gungi.p1Color, 11, 2, 0))
        gungi.piecesList.append(pieces.Fort(7,gungi.p1Color, 5, 2, 0))
        gungi.piecesList.append(pieces.Fort(7,gungi.p1Color, 9, 2, 0))
        gungi.piecesList.append(pieces.Samurai(8,gungi.p1Color, 6, 2, 0))
        gungi.piecesList.append(pieces.Samurai(8,gungi.p1Color, 8, 2, 0))
        #p1備戰區
        gungi.piecesList.append(pieces.Captain(9,gungi.p1Color, 0, 0, 0))
        gungi.piecesList.append(pieces.Captain(9,gungi.p1Color, 0, 1, 0))
        gungi.piecesList.append(pieces.Spear(4,gungi.p1Color, 1, 0, 0))
        gungi.piecesList.append(pieces.Spear(4,gungi.p1Color, 1, 1, 0))
        gungi.piecesList.append(pieces.Cavalry(10,gungi.p1Color, 2, 0, 0))
        gungi.piecesList.append(pieces.Cavalry(10,gungi.p1Color, 2, 1, 0))
        gungi.piecesList.append(pieces.Soldier(6,gungi.p1Color, 1, 2, 0))
        
        #p2
        gungi.piecesList.append(pieces.King(11,gungi.p2Color, 7, 8, 0))
        gungi.piecesList.append(pieces.Prince(12,gungi.p2Color, 6, 8, 0))
        gungi.piecesList.append(pieces.Duke(13,gungi.p2Color, 8, 8, 0))
        gungi.piecesList.append(pieces.Spear(14,gungi.p2Color, 7, 7, 0))
        gungi.piecesList.append(pieces.Shinobi(15,gungi.p2Color, 4, 7, 0))
        gungi.piecesList.append(pieces.Shinobi(15,gungi.p2Color, 10, 7, 0))
        gungi.piecesList.append(pieces.Soldier(16,gungi.p2Color, 3, 6, 0))
        gungi.piecesList.append(pieces.Soldier(16,gungi.p2Color, 7, 6, 0))
        gungi.piecesList.append(pieces.Soldier(16,gungi.p2Color, 11, 6, 0))
        gungi.piecesList.append(pieces.Fort(17,gungi.p2Color, 5, 6, 0))
        gungi.piecesList.append(pieces.Fort(17,gungi.p2Color, 9, 6, 0))
        gungi.piecesList.append(pieces.Samurai(18,gungi.p2Color, 6, 6, 0))
        gungi.piecesList.append(pieces.Samurai(18,gungi.p2Color, 8, 6, 0))
        #p2備戰區
        gungi.piecesList.append(pieces.Captain(19,gungi.p2Color, 12, 8, 0))
        gungi.piecesList.append(pieces.Captain(19,gungi.p2Color, 12, 7, 0))
        gungi.piecesList.append(pieces.Spear(14,gungi.p2Color, 13, 8, 0))
        gungi.piecesList.append(pieces.Spear(14,gungi.p2Color, 13, 7, 0))
        gungi.piecesList.append(pieces.Cavalry(20,gungi.p2Color, 14, 8, 0))
        gungi.piecesList.append(pieces.Cavalry(20,gungi.p2Color, 14, 7, 0))
        gungi.piecesList.append(pieces.Soldier(16,gungi.p2Color, 13, 6, 0))    
    
    def pieceDisplay(self):
        for item in gungi.piecesList:
            item.displayPieces(gungi.window)
    
    def rangeDisplay(self):
        if gungi.selectedPiece != None:
            pygame.draw.rect(self.window, constants.choose_color,(gungi.selectedPiece.x*80, gungi.selectedPiece.y*80, constants.square_size, constants.square_size),5)
            if gungi.newpieceFlag == 0:
                gungi.selectedPiece.moveRange(self.window)

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
        gungi.newpieceFlag, gungi.z_axis, gungi.chooseFlag, gungi.tempZFlag, gungi.moveFlag= 0, 0, 0, 0, 0
        gungi.selectedPiece = None

        if t == 1:
            gungi.turnFlag = 2
        elif t == 2:
            gungi.turnFlag = 1       

    def select_piece(self, turn, x, y):
        selectFilter = list(filter(lambda piece: piece.x == x and piece.y == y and piece.player == turn , gungi.piecesList))
        arr = pieces.listPiecestoArr(gungi.piecesList)

        if gungi.moveFlag == 0:
            if len(selectFilter) == 1:
                gungi.selectedPiece = selectFilter[0]
                selectFilter.sort(key=lambda piece: piece.z)
                gungi.z_axis = selectFilter[0].z

                pieceName = gungi.selectedPiece.__class__.__name__
                print("Piece:"+ pieceName,";","z_axis:",gungi.z_axis)
                #return
            elif len(selectFilter) == 2:
                gungi.selectedPiece = selectFilter[1]
                selectFilter.sort(key=lambda piece: piece.z)
                gungi.z_axis = selectFilter[1].z

                pieceName = gungi.selectedPiece.__class__.__name__
                print("Piece:"+ pieceName,";","z_axis:",gungi.z_axis)
                #return

        if gungi.selectedPiece:
            if(0 <= gungi.selectedPiece.x < 3 and turn == 1 ) or (12 <= gungi.selectedPiece.x < 15 and turn == 2):
                if gungi.newpieceFlag == 0:
                    gungi.newpieceFlag = 1
                    gungi.piece = gungi.selectedPiece
        '''
        else:
            fi = filter(lambda p: p.x == x and p.y == y, gungi.piecesList)
            listfi = list(fi)
            if len(listfi) != 0:
                gungi.selectedPiece = listfi[0]
        '''

        if x >= 3 and x <= 11:
            if gungi.newpieceFlag == 1:
                gungi.chooseFlag = 1
            elif gungi.moveFlag < 2: 
                gungi.moveFlag += 1
        
        if (gungi.newpieceFlag == 1 and gungi.chooseFlag == 1):
                self.placement_newpiece(gungi.piece,x,y,arr)
        elif gungi.newpieceFlag == 0 and gungi.moveFlag == 2:
            if gungi.z_axis == 0 and arr[x][y][gungi.z_axis] == 0:
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.z_axis)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
            elif gungi.z_axis == 1 and arr[x][y][0] == 0:
                gungi.tempZFlag = 0
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.tempZFlag)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
            elif gungi.z_axis == 0 and arr[x][y][0] == gungi.turnFlag:
                gungi.tempZFlag = 1
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.tempZFlag)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
            '''
            elif gungi.z_axis == 0 and arr[x][y][0] != gungi.turnFlag:
                gungi.tempZFlag = 0
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.tempZFlag)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
            '''

    def placement_newpiece(self, piece, x, y, arr):
        if arr[x][y][0] == 0:
            piece.x, piece.y, piece.z = x, y, 0
            self.exchangeTurn(gungi.turnFlag)
        elif arr[x][y][0] == gungi.turnFlag and arr[x][y][1] == 0:
            piece.x, piece.y, piece.z = x, y, 1
            self.exchangeTurn(gungi.turnFlag)

    def move_piece(self, piece, x, y, z):
        '''
        for item in gungi.piecesList:
            if piece.player == gungi.turnFlag:
                if item.x == x and item.y == y:
                    gungi.piecesList.remove(item)
            else:
                print("Not Your Piece")
                return False
        '''
        
        piece.x, piece.y, piece.z = x, y, z

        print(piece.__class__.__name__+" move to " +"x:"+str(x) +" y:"+str(y) +" z:"+str(z))
        self.exchangeTurn(gungi.turnFlag)
        return True

    def endGame(self):
        print("關閉")
        exit()


if __name__ == '__main__':
    gungi().startGame()  