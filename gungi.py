import sys
import pygame
import time
import constants as constants
import pieces as pieces

class gungi():
    window = None

    p1Color = constants.p1Color
    p2Color = constants.p2Color
    
    piecesList = []

    def startGame(self):
        pygame.init()
        gungi.window = pygame.display.set_mode((constants.screen_width,constants.screen_height))
        pygame.display.set_caption('Gungi')
        self.pieceInit()

        while True:
            time.sleep(0.1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.drawBoard()
            self.pieceDisplay()
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

    def pieceDisplay(self):
        for item in gungi.piecesList:
            item.displayPieces(gungi.window)

if __name__ == '__main__':
    gungi().startGame()