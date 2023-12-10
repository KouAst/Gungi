import sys
import pygame
from tkinter import messagebox
import time
import math
import random
import threading
import constants as constants
import pieces as pieces
#import computer as computer

class gungi():
    window = None

    
    p1Color = constants.p1Color #Black 預設電腦
    p2Color = constants.p2Color #White 預設玩家

    selectedPiece = None
    turnFlag = p2Color
    newpieceFlag = 0
    chooseFlag = 0
    tempZFlag = 0
    moveFlag = 0
    attackFlag = 0
    selectCode = 0
    checkFlag = None
    piece = None
    z_axis = 0
    sound = []
    piecesList = []
    clock = 0
    
    

    def startGame(self):
        pygame.init()
        pygame.mixer.init()
        gungi.window = pygame.display.set_mode((constants.screen_width,constants.screen_height)) # ,pygame.RESIZABLE)
        pygame.display.set_caption('Gungi')        
        self.pieceInit()
        self.soundInit()
        print("玩家回合")

        while True:
            time.sleep(0.2)
            self.drawBoard()
            self.pieceDisplay()
            self.wingame() 
            #self.Instructions()
            if self.turnFlag == self.p1Color:
                self.AI_move()
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
        gungi.piecesList.sort(key=lambda item: item.z)
        for item in gungi.piecesList:
            item.displayPieces(gungi.window)
    
    def rangeDisplay(self):
        if gungi.selectedPiece != None:
            if gungi.newpieceFlag == 0:
                gungi.selectedPiece.moveRange(self.window)
            pygame.draw.rect(self.window, constants.choose_color,(gungi.selectedPiece.x*80, gungi.selectedPiece.y*80, constants.square_size, constants.square_size),5)
            
    
    '''
    def Instructions(self):
        
        font = pygame.font.Font(None, 60)
        text = font.render("?", True, (0, 0, 0))
        pygame.draw.circle(self.window,(255,255,255), (1160,40), 30)
        self.window.blit(text, (1148, 22))
    ''' 

    def soundInit(self):
        for i in range(0,6):
            self.sound.append(pygame.mixer.Sound("sound/"+str(i+1)+".wav"))
        print("以載入"+str(len(self.sound))+"種音效")

    def getEvent(self):
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #if not self.wingame() and self.turnFlag==constants.p2Color:
                    pos = pygame.mouse.get_pos()
                    posx = pos[0]
                    posy = pos[1]
                    #print("posx:",posx,";","posy:",posy)
                    x = math.floor(posx / 80)
                    y = math.floor(posy / 80)
                    print("x:",x,";","y:",y)
                    self.select_piece(gungi.turnFlag,x,y)
            
                

    def exchangeTurn(self,t):
        gungi.newpieceFlag, gungi.z_axis, gungi.chooseFlag, gungi.tempZFlag, gungi.moveFlag, gungi.attackFlag, gungi.selectCode= 0, 0, 0, 0, 0, 0, 0
        gungi.selectedPiece = None
        gungi.checkFlag = None
        gungi.piece = None

        if t == 1:
            gungi.turnFlag = 2
            print("玩家回合")
        elif t == 2:
            gungi.turnFlag = 1
            print("電腦回合")      

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
            elif len(selectFilter) == 0 and gungi.newpieceFlag == 1:
                pass
            else: return
        

        if gungi.selectedPiece:
            if(0 <= gungi.selectedPiece.x < 3 and turn == 1 ) or (12 <= gungi.selectedPiece.x < 15 and turn == 2):
                if gungi.newpieceFlag == 0:
                    gungi.newpieceFlag = 1
                    gungi.piece = gungi.selectedPiece
                elif gungi.newpieceFlag == 1:
                    gungi.piece = gungi.selectedPiece
        
        '''
        else:
            fi = filter(lambda p: p.x == x and p.y == y, gungi.piecesList)
            listfi = list(fi)
            if len(listfi) != 0:
                gungi.selectedPiece = listfi[0]
        '''

        if x >= 3 and x <= 11 and y >=0:
            if gungi.newpieceFlag == 1:
                gungi.chooseFlag = 1
            elif gungi.moveFlag < 2:
                gungi.moveFlag += 1
        
        if gungi.newpieceFlag == 1 and gungi.chooseFlag == 1:
                if len(selectFilter) == 1:
                    gungi.checkFlag = selectFilter[0]
                    selectFilter.sort(key=lambda piece: piece.z)
                    gungi.z_axis = selectFilter[0].z
                    gungi.selectCode = gungi.checkFlag.piececode
                    print("pieceCode:",gungi.selectCode)
                    #return
                else: 
                    gungi.selectCode = 0
                    print("pieceCode:","0")
                self.placement_newpiece(gungi.piece,x,y,arr,gungi.selectCode)
        elif gungi.newpieceFlag == 0 and gungi.moveFlag == 2:
            if len(selectFilter) == 1:
                gungi.checkFlag = selectFilter[0]
                selectFilter.sort(key=lambda piece: piece.z)
                gungi.z_axis = selectFilter[0].z
                gungi.selectCode = gungi.checkFlag.piececode
                print("pieceCode:",gungi.selectCode)
                #return
            elif len(selectFilter) == 2:
                gungi.checkFlag = selectFilter[1]
                selectFilter.sort(key=lambda piece: piece.z)
                gungi.z_axis = selectFilter[1].z
                gungi.selectCode = gungi.checkFlag.piececode
                print("pieceCode:",gungi.selectCode)
                #return
            else: 
                gungi.selectCode = 0
                print("pieceCode:","0")

            if gungi.z_axis == 0 and arr[x][y][gungi.z_axis] == 0:
                print("action:moving")
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.z_axis)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
            elif gungi.z_axis == 1 and arr[x][y][0] == 0:
                print("action:unstack moving(lower)")
                gungi.tempZFlag = 0
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.tempZFlag)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
            elif gungi.z_axis == 1 and arr[x][y][0] == gungi.turnFlag:
                print("action:stack moving")
                gungi.tempZFlag = 1
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.tempZFlag)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
            elif gungi.z_axis == 0 and arr[x][y][0] == gungi.turnFlag and arr[x][y][1]==0 and ((gungi.selectCode != 1 and gungi.turnFlag == 1) or (gungi.selectCode != 11 and gungi.turnFlag == 2)):
                print("action:stack moving(upper)")
                gungi.tempZFlag = 1
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.tempZFlag)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
            elif gungi.z_axis == 0 and arr[x][y][0] != gungi.turnFlag and arr[x][y][1] == 0:
                print("action:attack(0>0)")
                gungi.attackFlag = 1
                gungi.tempZFlag = 0
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.tempZFlag)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
            elif gungi.z_axis == 1 and arr[x][y][0] != gungi.turnFlag and arr[x][y][1] == 0:
                print("action:attack(1>0)")
                gungi.attackFlag = 1
                gungi.tempZFlag = 0
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.tempZFlag)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
                '''        
            elif gungi.z_axis == 0 and arr[x][y][0] != 0 and arr[x][y][1] != gungi.turnFlag:
                print("action:attack(0>1)")
                gungi.attackFlag = 1
                gungi.tempZFlag = 1
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.tempZFlag)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
                '''        
            elif gungi.z_axis == 1 and arr[x][y][0] != 0 and arr[x][y][1] != gungi.turnFlag:
                print("action:attack(1>1)")
                gungi.attackFlag = 1
                gungi.tempZFlag = 1
                if gungi.selectedPiece.canMove(arr, x, y, gungi.z_axis):
                    self.move_piece(gungi.selectedPiece, x, y, gungi.tempZFlag)
                    #gungi.selectedPiece = None
                else:
                    gungi.selectedPiece = None
                    gungi.moveFlag = 0
                    

    def placement_newpiece(self, piece, x, y, arr, selectcode):
        if arr[x][y][0] == 0 and (x>2 and x<12):
            piece.x, piece.y, piece.z = x, y, 0
            self.sound[random.randint(0,5)].play()
            print(str(x)+"-"+str(y)+"-"+str(piece.z)+" "+ str(piece.__class__.__name__)+" new")
            
            self.exchangeTurn(self.turnFlag)
        elif arr[x][y][0] == self.turnFlag and arr[x][y][1] == 0 and (x>2 and x<12) and ((selectcode != 1 and gungi.turnFlag == 1) or (selectcode != 11 and gungi.turnFlag == 2)):
            piece.x, piece.y, piece.z = x, y, 1
            self.sound[random.randint(0,5)].play()
            print(str(x)+"-"+str(y)+"-"+str(piece.z)+" "+ str(piece.__class__.__name__)+" new")
            
            self.exchangeTurn(self.turnFlag)
        

    def move_piece(self, piece, x, y, z):
        for item in gungi.piecesList:
            if piece.player == gungi.turnFlag:
                if item.x == x and item.y == y and item.z == z and gungi.attackFlag == 1:
                    gungi.piecesList.remove(item)
                    
            else:
                print("Not Your Piece")
                return False
        
        piece.x, piece.y, piece.z = x, y, z

        self.sound[random.randint(0,5)].play()
        print(str(x)+"-"+str(y)+"-"+str(z)+" "+ piece.__class__.__name__)
        
        self.exchangeTurn(gungi.turnFlag)
        
        return True

    def AI_move(self):
        availd_piece=[]
        emnemy_piece=[]
        move_piece=None
        if self.turnFlag == self.p2Color:
            return 
        if self.turnFlag == self.p1Color:
            for piece in self.piecesList:
                if piece.player == self.p1Color:
                    availd_piece.append(piece)
            print("可移動旗子數量: "+str(len(availd_piece)))
            if len(availd_piece)>0:
                for i in range(len(availd_piece)):
                    availd_piece[i].bestMove(self.piecesList)
                emnemy_piece = [(enemy.x, enemy.y) for enemy in self.piecesList if enemy.player == self.p2Color]

                for enemy_x, enemy_y in emnemy_piece:
                    for piece in availd_piece:
                        if (enemy_x, enemy_y) in piece.Allrange:
                            move_piece = piece
                            self.select_piece(self.turnFlag, move_piece.x, move_piece.y)
                            self.select_piece(self.turnFlag, enemy_x, enemy_y)
                            break
                '''
                for enemy in self.piecesList:
                    if enemy.player==self.p2Color:
                        emnemy_piece.append((enemy.x,enemy.y))
                
                for i in range(len(emnemy_piece)):          #進到攻擊範圍便吃棋
                    for j in range(len(availd_piece)):
                        if emnemy_piece[i] in availd_piece[j].Allrange:
                            #print("進入吃棋範圍")
                            move_piece = availd_piece[j]
                            enemy_x , enemy_y = emnemy_piece[i]
                            self.select_piece(self.turnFlag,move_piece.x,move_piece.y)                  
                            self.select_piece(self.turnFlag,enemy_x,enemy_y)
                            break
                '''    
                if not move_piece:
                    print("隨機選擇移動")        
                    move_piece = random.choice(availd_piece)
                    print(move_piece.__class__.__name__)
                    if move_piece.x < 3 or move_piece.x > 11:
                        arr = pieces.listPiecestoArr(self.piecesList)
                        self.select_piece(self.turnFlag,move_piece.x,move_piece.y)
                        self.placement_newpiece(move_piece,random.randint(3,11),random.randint(0,8),arr,self.selectCode)
                    else:
                        move_piece.bestMove(self.piecesList)
                        
                print("move_piece: "+str(move_piece.Allrange))
                if move_piece.Allrange:
                    AI_x,AI_y = random.choice(move_piece.Allrange)
                    self.select_piece(self.turnFlag,move_piece.x,move_piece.y)
                    self.select_piece(self.turnFlag,AI_x,AI_y)  
                                

    def resetGame(self):

        self.selectedPiece = None
        self.turnFlag = self.p2Color
        self.newpieceFlag = 0
        self.chooseFlag = 0
        self.tempZFlag = 0
        self.moveFlag = 0
        self.attackFlag = 0
        self.selectCode = 0
        self.checkFlag = None
        self.piece = None
        self.z_axis = 0
        self.sound.clear()
        
        self.piecesList.clear()
          

    def wingame(self):
        p1_King = False
        p2_King = False
        

        

        for piece in self.piecesList:
            if isinstance(piece, pieces.King):
                if piece.player == self.p1Color:
                    p1_King = True
                elif piece.player == self.p2Color:
                    p2_King = True
        

        if p1_King == p2_King:
            return 
        elif (p1_King == True) and (p2_King == False):                      
            print("電腦勝利")
            messagebox.showinfo("Game Over", "黑方勝利")
            result = messagebox.askquestion("Restart", "是否要重新開始遊戲？")
            if result == 'yes':
                # 在这里添加重新开始游戏的逻辑
                print("重新开始游戏")
                self.resetGame()
                gungi().startGame()
            else:
                print("退出遊戲")
                exit()
            
        else:
            print("玩家勝利")
            messagebox.showinfo("Game Over", "白方勝利")
            result = messagebox.askquestion("Restart", "是否要重新開始遊戲？")
            if result == 'yes':
                pass
                # 在这里添加重新开始游戏的逻辑
                print("重新开始游戏")
                self.resetGame()
                gungi().startGame()
            else:
                print("退出遊戲")
                exit()
            
        

    def endGame(self):
        result = messagebox.askquestion("", "確定要離開遊戲？")
        if result == 'yes':
            exit()
        else:
            return


if __name__ == '__main__':
    gungi().startGame()  