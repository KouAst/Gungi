import sys
import pygame
import time
import math
import threading
import constants as constants
import pieces as pieces

class gungi():
    window = None

    p1Color = constants.p1Color
    p2Color = constants.p2Color
    Start_X = constants.start_X
    Start_Y = constants.start_Y
    Max_X = 1440
    Max_Y = 880
    putDownFlag = p2Color
    piecesSelected = None
    choose_piece = None
    piece_moved = False
    #button_go = None
    p1_time_set = 6
    p2_time_set = 6
    sceond_time = 3
    start_time = pygame.time.get_ticks()
    time_end = False
    p1_time_count = 0
    p2_time_count = 0

    piece_prepare = False

    piecesList = []

    


    def startGame(self):
        pygame.init()
        gungi.window = pygame.display.set_mode((constants.screen_width,constants.screen_height))#,pygame.FULLSCREEN)
        pygame.display.set_caption('Gungi')        
        self.pieceInit()
        #while self.piece_prepare==False:
        print("佈陣階段")
        self.prepare_time()
        
        print("白棋先攻")   
        
        

        while self.piece_prepare == True:         
            while True:
                time.sleep(0.1)
                self.window.fill((100,100,100))
        

                self.drawBoard()
                self.drawpieceTable()
                self.pieceDisplay()
                self.Select_rect()
                #self.victoryDecision()
                #self.computerPlay()
                self.getEvent()
                self.wingame()
                pygame.display.update()
                pygame.display.flip()
            
            

    def drawBoard(self):
        for row in range(constants.board_size):
            for col in range(constants.board_size-2):
                if row == 0:
                    x = col * constants.square_size +320
                    y = row * constants.square_size
                    pygame.draw.rect(self.window, constants.board_color, (x, y, constants.square_size, constants.square_size))
                elif row == 10:
                    x = col * constants.square_size +320
                    y = row * constants.square_size
                    pygame.draw.rect(self.window, constants.board_color, (x, y, constants.square_size, constants.square_size))
                else:
                    x = col * constants.square_size +320
                    y = row * constants.square_size
                    pygame.draw.rect(self.window, constants.board_color, (x, y, constants.square_size, constants.square_size))
                    pygame.draw.rect(self.window, constants.line_color, (x, y, constants.square_size, constants.square_size), 1)
                    
    def drawpieceTable(self):
        pygame.draw.rect(self.window, constants.table_color, (0,0,320,480))
        pygame.draw.rect(self.window, constants.table_color, (1040,400,320,480))

    def Select_rect(self):
        if(gungi.choose_piece)!=None:
                pygame.draw.rect(self.window, constants.choose_color, gungi.choose_piece, 5)
        
    def pieceInit(self):
        '''
        測試用 King(帥),Prince(大),Duke(中),Spear(槍),Shinobi(忍),Soldier(兵),Fort(砦),Samurai(侍),Captain(小),Cavalry(馬)
        '''
        #gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 4, 2))
        '''
        gungi.piecesList.append(pieces.King(gungi.p1Color, 8, 1))
        gungi.piecesList.append(pieces.Prince(gungi.p1Color, 13, 0))
        gungi.piecesList.append(pieces.Duke(gungi.p1Color, 14, 0))
        gungi.piecesList.append(pieces.Spear(gungi.p1Color, 15, 0))
        gungi.piecesList.append(pieces.Shinobi(gungi.p1Color, 16, 0))
        gungi.piecesList.append(pieces.Shinobi(gungi.p1Color, 13, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 14, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 15, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 16, 1))
        gungi.piecesList.append(pieces.Fort(gungi.p1Color, 13, 2))
        gungi.piecesList.append(pieces.Fort(gungi.p1Color, 14, 2))
        gungi.piecesList.append(pieces.Samurai(gungi.p1Color, 15, 2))
        gungi.piecesList.append(pieces.Samurai(gungi.p1Color, 16, 2))
        gungi.piecesList.append(pieces.Captain(gungi.p1Color, 13, 3))
        gungi.piecesList.append(pieces.Captain(gungi.p1Color, 14, 3))
        gungi.piecesList.append(pieces.Spear(gungi.p1Color, 15, 3))
        gungi.piecesList.append(pieces.Spear(gungi.p1Color, 16, 3))
        gungi.piecesList.append(pieces.Cavalry(gungi.p1Color, 13, 4))
        gungi.piecesList.append(pieces.Cavalry(gungi.p1Color, 14, 4))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 15, 4))
        '''
        #p2
        gungi.piecesList.append(pieces.King(gungi.p2Color, 8, 9))
        gungi.piecesList.append(pieces.Prince(gungi.p2Color, 0, 10))
        gungi.piecesList.append(pieces.Duke(gungi.p2Color, 1, 10))
        gungi.piecesList.append(pieces.Spear(gungi.p2Color, 2, 10))
        gungi.piecesList.append(pieces.Shinobi(gungi.p2Color, 3, 10))
        gungi.piecesList.append(pieces.Shinobi(gungi.p2Color, 0, 9))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 1, 9))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 2,9))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 3, 9))
        gungi.piecesList.append(pieces.Fort(gungi.p2Color, 0, 8))
        gungi.piecesList.append(pieces.Fort(gungi.p2Color, 1, 8))
        gungi.piecesList.append(pieces.Samurai(gungi.p2Color, 2, 8))
        gungi.piecesList.append(pieces.Samurai(gungi.p2Color, 3, 8))
        gungi.piecesList.append(pieces.Captain(gungi.p2Color, 0, 7))
        gungi.piecesList.append(pieces.Captain(gungi.p2Color, 1, 7))
        gungi.piecesList.append(pieces.Spear(gungi.p2Color, 2, 7))
        gungi.piecesList.append(pieces.Spear(gungi.p2Color, 3, 7))
        gungi.piecesList.append(pieces.Cavalry(gungi.p2Color, 0, 6))
        gungi.piecesList.append(pieces.Cavalry(gungi.p2Color, 1, 6))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 2, 6))
        
        #棋盤座標範圍: X:4~12 Y:1~9
        gungi.piecesList.append(pieces.King(gungi.p1Color, 8, 1))
        gungi.piecesList.append(pieces.Prince(gungi.p1Color, 7, 1))
        gungi.piecesList.append(pieces.Duke(gungi.p1Color, 9, 1))
        gungi.piecesList.append(pieces.Spear(gungi.p1Color, 8, 2))
        gungi.piecesList.append(pieces.Shinobi(gungi.p1Color, 5, 2))
        gungi.piecesList.append(pieces.Shinobi(gungi.p1Color, 11, 2))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 4, 3))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 8, 3))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 12, 3))
        gungi.piecesList.append(pieces.Fort(gungi.p1Color, 6, 3))
        gungi.piecesList.append(pieces.Fort(gungi.p1Color, 10, 3))
        gungi.piecesList.append(pieces.Samurai(gungi.p1Color, 7, 3))
        gungi.piecesList.append(pieces.Samurai(gungi.p1Color, 9, 3))
        #p1備戰區 座標:X:0~3 Y:0~5
        gungi.piecesList.append(pieces.Captain(gungi.p1Color, 0, 0))
        gungi.piecesList.append(pieces.Captain(gungi.p1Color, 1, 0))
        gungi.piecesList.append(pieces.Spear(gungi.p1Color, 2, 0))
        gungi.piecesList.append(pieces.Spear(gungi.p1Color, 3, 0))
        gungi.piecesList.append(pieces.Cavalry(gungi.p1Color, 0, 1))
        gungi.piecesList.append(pieces.Cavalry(gungi.p1Color, 1, 1))
        gungi.piecesList.append(pieces.Soldier(gungi.p1Color, 2, 1))
        '''
        gungi.piecesList.append(pieces.King(gungi.p2Color, 8, 9))
        gungi.piecesList.append(pieces.Prince(gungi.p2Color, 7, 9))
        gungi.piecesList.append(pieces.Duke(gungi.p2Color, 9, 9))
        gungi.piecesList.append(pieces.Spear(gungi.p2Color, 8, 8))
        gungi.piecesList.append(pieces.Shinobi(gungi.p2Color, 5, 8))
        gungi.piecesList.append(pieces.Shinobi(gungi.p2Color, 11, 8))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 4, 7))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 8, 7))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 12, 7))
        gungi.piecesList.append(pieces.Fort(gungi.p2Color, 6, 7))
        gungi.piecesList.append(pieces.Fort(gungi.p2Color, 10, 7))
        gungi.piecesList.append(pieces.Samurai(gungi.p2Color, 7, 7))
        gungi.piecesList.append(pieces.Samurai(gungi.p2Color, 9, 7))
        #p2備戰區 座標:X:13~16 Y:5~10
        gungi.piecesList.append(pieces.Captain(gungi.p2Color, 13, 10))
        gungi.piecesList.append(pieces.Captain(gungi.p2Color, 14, 10))
        gungi.piecesList.append(pieces.Spear(gungi.p2Color, 15, 10))
        gungi.piecesList.append(pieces.Spear(gungi.p2Color, 16, 10))
        gungi.piecesList.append(pieces.Cavalry(gungi.p2Color, 13, 9))
        gungi.piecesList.append(pieces.Cavalry(gungi.p2Color, 14, 9))
        gungi.piecesList.append(pieces.Soldier(gungi.p2Color, 15, 9))
        '''
    def pieceDisplay(self):
        for item in gungi.piecesList:
            item.displayPieces(gungi.window)

    def getEvent(self):
        eventList = pygame.event.get()
        #self.countdown_change()       #倒數計時函式
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                if (
                    mouse_x > gungi.Start_X  and mouse_x < gungi.Max_X ) and (
                    mouse_y > gungi.Start_Y  and mouse_y < gungi.Max_Y ):
                    #if gungi.putDownFlag != gungi.p1Color:
                    #    return
                    click_x = math.floor((mouse_x-gungi.Start_X) /80)
                    click_y = math.floor((mouse_y-gungi.Start_Y) /80)
                    self.test_x = click_x
                    self.test_y = click_y 
                    click_mod_x = (mouse_x-gungi.Start_X) % 80
                    click_mod_y = (mouse_y-gungi.Start_Y) % 80
                    if abs(click_mod_x)>=0 and abs(click_mod_y)>=0:
                        print("原始座標:x="+str(mouse_x)+" y="+str(mouse_y))
                        print("該點為:x="+str(click_x - 3)+" y="+str(click_y))
                    #if gungi.putDownFlag == gungi.p1Color:
                        gungi.choose_piece = None
                        self.putDownPieces(gungi.putDownFlag, click_x, click_y)
                        
                    #else:
                     #   self.putDownPieces(gungi.p2Color, click_x, click_y)
                else:
                    
                    print("out")
                #if gungi.button_go.is_click():
                #    print("button_go click")
                #else:
                #    print("button_go click out")                      

    def putDownPieces(self, t, x, y):
        selectfilter=list(filter(lambda cm: cm.x == x  and cm.y == y and cm.player == gungi.putDownFlag,gungi.piecesList))
        

        if len(selectfilter):
            gungi.piecesSelected = selectfilter[0]
            print("該棋為:" + str(gungi.piecesSelected))
            gungi.choose_piece = pygame.Rect(x*80,y*80,constants.square_size,constants.square_size)
            return
        
        
        if gungi.piecesSelected:
            arr = pieces.listPiecestoArr(gungi.piecesList)
            if gungi.piecesSelected.canMove(arr, x, y):
                    self.piecesMove(gungi.piecesSelected, x, y)
                    gungi.piecesSelected = None
            else:
                    gungi.piecesSelected = None
        
        else:
            fi = filter(lambda p: p.x == x and p.y == y, gungi.piecesList)
            listfi = list(fi)
            if len(listfi) != 0:
                gungi.piecesSelected = listfi[0]
        
    def ready_button(self):
        button_x = 580
        button_y = 360
        button_width = 200
        button_height = 100
        #按鈕
        pygame.draw.rect(self.window, constants.table_color, (button_x,button_y,button_width,button_height))
        #按鈕文字
        font = pygame.font.Font(None, 36)
        text = font.render("Ready", True, constants.line_color)
        text_rect = text.get_rect(center=(580 + 200 // 2, 360 + 100 // 2))
        self.window.blit(text, text_rect)        
        
        def is_mouse_over_button():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            return button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_over_button():
                    print("Button clicked!")
                    self.piece_prepare = True

    def piecesMove(self, pieces, x, y):
        if self.piece_prepare == True:
            for item in gungi.piecesList:
                if pieces.player == gungi.putDownFlag:
                    if item.x == x and item.y == y:
                        gungi.piecesList.remove(item)
                else:
                    print("這不是你的棋子")
                    return False
        else:
            for item in gungi.piecesList:
                    if item.x == x and item.y == y:
                        gungi.piecesList.remove(item)
        pieces.x = x
        pieces.y = y

        print(str(pieces)+"移動到:" +"x="+str(x - 3)  + " y=" + str(y))
        self.piece_moved = True
        #print(str(pieces.player) + str(gungi.putDownFlag))
        if self.piece_prepare == True:
            if gungi.putDownFlag == gungi.p1Color:
                gungi.putDownFlag = gungi.p2Color
                print("白方的回合")
                # self.piece_moved = False
            else:
                gungi.putDownFlag = gungi.p1Color
                print("黑方的回合")
                #self.piece_moved = False
            

        return True

    def prepare_time(self):
        
        #self.window.fill((100,100,100))
        #self.pieceInit()
        def Piece_sorting():
            new_x_W = 13
            new_y_W = 10
            new_x_B = 0
            new_y_B = 0
            for piece in gungi.piecesList:
                #白棋
                if piece.x <= 3 and piece.y >= 6:
                    piece.x = new_x_W
                    piece.y = new_y_W
                    if new_x_W <= 16:
                        new_x_W +=1
                    if new_x_W > 16:
                        new_x_W = 13
                        new_y_W -=1
                #黑棋    
                if piece.x >=13  and piece.y <= 5:
                    piece.x = new_x_B
                    piece.y = new_y_B
                    if new_x_B <= 3:
                        new_x_B +=1
                    if new_x_B > 3:
                        new_x_B = 0
                        new_y_B +=1

        while self.piece_prepare !=True:
            
            self.window.fill((100,100,100))
            self.drawBoard()
            self.drawpieceTable()
            self.pieceDisplay()
            self.Select_rect()                       
            self.getEvent()
            self.ready_button()

            pygame.display.update()
            pygame.display.flip()
            
        Piece_sorting()
    

    def countdown_change(self):
        time_elapsed = pygame.time.get_ticks() - self.start_time
        if self.putDownFlag == self.p1Color:
            time_left = math.floor(self.p1_time_set - time_elapsed/1000%self.p1_time_set)
        else:
            time_left = math.floor(self.p2_time_set - time_elapsed/1000%self.p2_time_set)
        self.font = pygame.font.Font(None, 44)
        self.text_surface = self.font.render("Time: "+str(time_left), True, (255, 255, 255))
        self.window.blit(self.text_surface, (180, 720))
        
            

        if time_left == 0:
            self.time_end = True

        if gungi.putDownFlag == gungi.p1Color:
            if self.piece_moved == True:                   
                self.piece_moved = False
                self.start_time = None
                self.start_time = pygame.time.get_ticks()
                self.change_player()
                
                
        elif gungi.putDownFlag == gungi.p2Color:
            if self.piece_moved == True:
                self.piece_moved = False
                self.start_time = None
                self.start_time = pygame.time.get_ticks()
                self.change_player()


        if gungi.putDownFlag == gungi.p1Color:
            if self.time_end == True:
                print("思考時間到!")
                self.p1_time_set = self.sceond_time
                self.p1_time_count +=1
                if self.p1_time_count == 1:
                    print("警告! 你尚未下子!")
                    print("你之後的思考時間將減少為"+str(self.p1_time_set)+"秒")
                    print("若在思考時間到後仍未下子，將自動判定認輸")
                self.time_end = False
                
                time.sleep(1)       
        else:
            if self.time_end == True:
                print("思考時間到!")
                self.p2_time_set = self.sceond_time
                self.p2_time_count +=1
                if self.p2_time_count == 1:
                    print("警告! 你尚未下子!")
                    print("你之後的思考時間將減少為"+str(self.p2_time_set)+"秒")
                    print("若在思考時間到後仍未下子，將自動判定認輸")
                self.time_end = False
                
                time.sleep(1)

    def wingame(self):
        p1_King = False
        p2_King = False

        if self.p1_time_count == 2:
            print("白方勝利")
            return self.endGame()
        elif self.p2_time_count == 2:
            print("黑方勝利")
            return self.endGame()

        for piece in self.piecesList:
            if isinstance(piece, pieces.King):
                if piece.player == constants.p1Color:
                    p1_King = True
                elif piece.player == constants.p2Color:
                    p2_King = True
        if p1_King == p2_King:
            return 
        elif (p1_King == True) and (p2_King == False):
            print("黑方勝利")
            return self.endGame()
        else:
            print("白方勝利")
            return self.endGame()
        
        


    def endGame(self):
        print("關閉")
        exit()


if __name__ == '__main__':
    gungi().startGame()
    
    
                  
    