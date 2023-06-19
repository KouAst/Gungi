import sys
import pygame
import time
import constants as constants
import pieces as pieces

class gungi():
    window = None

    p1Color = constants.p1Color
    p2Color = constants.p2Color
    Start_X = constants.start_X
    Start_Y = constants.start_Y
    Max_X = 720
    Max_Y = 880
    putDownFlag = p1Color
    piecesSelected = None
    #button_go = None
    
    piecesList = []

    def startGame(self):
        pygame.init()
        gungi.window = pygame.display.set_mode((constants.screen_width,constants.screen_height))
        pygame.display.set_caption('Gungi')
        self.pieceInit()

        while True:
            time.sleep(0.1)
            self.drawBoard()
            self.pieceDisplay()
            #self.victoryDecision()
            #self.computerPlay()
            self.getEvent()
            pygame.display.update()
            pygame.display.flip()
    
    def drawBoard(self):
        for row in range(constants.board_size):
            for col in range(constants.board_size):
                if row == 0:
                    x = col * constants.square_size
                    y = row * constants.square_size
                    pygame.draw.rect(self.window, constants.board_color, (x, y, constants.square_size, constants.square_size))
                elif row == 10:
                    x = col * constants.square_size
                    y = row * constants.square_size
                    pygame.draw.rect(self.window, constants.board_color, (x, y, constants.square_size, constants.square_size))
                else:
                    x = col * constants.square_size
                    y = row * constants.square_size
                    pygame.draw.rect(self.window, constants.board_color, (x, y, constants.square_size, constants.square_size))
                    pygame.draw.rect(self.window, constants.line_color, (x, y, constants.square_size, constants.square_size), 1)

    def pieceInit(self):
        gungi.piecesList.append(pieces.King(gungi.p1Color, 4, 1))
        gungi.piecesList.append(pieces.King(gungi.p2Color, 4, 9))
        gungi.piecesList.append(pieces.Prince(gungi.p1Color, 3, 1))
        gungi.piecesList.append(pieces.Prince(gungi.p2Color, 3, 9))
        gungi.piecesList.append(pieces.Duke(gungi.p1Color, 5, 1))
        gungi.piecesList.append(pieces.Duke(gungi.p2Color, 5, 9))
        #gungi.piecesList.append(pieces.Spear(gungi.p1Color, 4, 2))
        #gungi.piecesList.append(pieces.Spear(gungi.p2Color, 4, 8))
        gungi.piecesList.append(pieces.Shinobi(gungi.p1Color, 1, 2))
        gungi.piecesList.append(pieces.Shinobi(gungi.p2Color, 1, 8))
        gungi.piecesList.append(pieces.Shinobi(gungi.p1Color, 7, 2))
        gungi.piecesList.append(pieces.Shinobi(gungi.p2Color, 7, 8))

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
                mouse_x = pos[0]
                mouse_y = pos[1]
                if (
                    mouse_x > gungi.Start_X  and mouse_x < gungi.Max_X ) and (
                    mouse_y > gungi.Start_Y  and mouse_y < gungi.Max_Y ):
                    if gungi.putDownFlag != gungi.p1Color:
                        return
                    click_x = round((mouse_x-gungi.Start_X) /72) - 1
                    click_y = round((mouse_y-gungi.Start_Y) /60) - 1
                    click_mod_x = (mouse_x-gungi.Start_X) % 72 - 1
                    click_mod_y = (mouse_y-gungi.Start_Y) % 60 - 1
                    if abs(click_mod_x)>=0 and abs(click_mod_y)>=0:
                        print("Success:x="+str(click_x)+" y="+str(click_y))
                        self.putDownPieces(gungi.p1Color, click_x, click_y)
                else:
                    print("out")
                #if gungi.button_go.is_click():
                #    print("button_go click")
                #else:
                #    print("button_go click out")

    def putDownPieces(self, t, x, y):
        selectfilter=list(filter(lambda cm: cm.x == x and cm.y == y and cm.player == gungi.p1Color,gungi.piecesList))
        print(gungi.piecesList)
        print(selectfilter)

        if len(selectfilter):
            gungi.piecesSelected = selectfilter[0]
            return
        
        if gungi.piecesSelected:
            print("Selected")
            arr = pieces.listPiecestoArr(gungi.piecesList)
            if gungi.piecesSelected.canMove(arr, x, y):
                self.piecesMove(gungi.piecesSelected, x, y)
                gungi.putDownFlag = gungi.p2Color
        else:
            fi = filter(lambda p: p.x == x and p.y == y, gungi.piecesList)
            listfi = list(fi)
            if len(listfi) != 0:
                gungi.piecesSelected = listfi[0]

    def piecesMove(self, pieces, x, y):
        for item in gungi.piecesList:
            if item.x == x and item.y == y:
                gungi.piecesList.remove(item)
        pieces.x = x
        pieces.y = y
        print("move to " + str(x) + " " + str(y))
        return True

    def endGame(self):
        print("exit")
        exit()

if __name__ == '__main__':
    gungi().startGame()