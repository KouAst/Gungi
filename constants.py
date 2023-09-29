import pygame

screen_width = 1200
screen_height = 720

p1Color = 1
p2Color = 2

row_size = 9
col_size = 15
square_size = 80

r1 = 1 * square_size
r2 = 2 * square_size
r3 = 3 * square_size

board_color = (186, 135, 48)
table_color = (239, 186, 97)
choose_color = (15, 242, 15)
range_color = (170, 74, 68)
line_color = (0, 0, 0)

pieces_images = {
    'w_king': pygame.image.load("pieceImg/King_W.png"),
    'w_prince': pygame.image.load("pieceImg/Prince_W.png"),
    'w_duke': pygame.image.load("pieceImg/Duke_W.png"),
    'w_captain': pygame.image.load("pieceImg/Captain_W.png"),
    'w_spear': pygame.image.load("pieceImg/Spear_W.png"),
    'w_cavalry': pygame.image.load("pieceImg/Cavalry_W.png"),
    'w_shinobi': pygame.image.load("pieceImg/Shinobi_W.png"),
    'w_samurai': pygame.image.load("pieceImg/Samurai_W.png"),
    'w_fort': pygame.image.load("pieceImg/Fort_W.png"),
    'w_soldier': pygame.image.load("pieceImg/Soldier_W.png"),

    'b_king': pygame.image.load("pieceImg/King_B.png"),
    'b_prince': pygame.image.load("pieceImg/Prince_B.png"),
    'b_duke': pygame.image.load("pieceImg/Duke_B.png"),
    'b_captain': pygame.image.load("pieceImg/Captain_B.png"),
    'b_spear': pygame.image.load("pieceImg/Spear_B.png"),
    'b_cavalry': pygame.image.load("pieceImg/Cavalry_B.png"),
    'b_shinobi': pygame.image.load("pieceImg/Shinobi_B.png"),
    'b_samurai': pygame.image.load("pieceImg/Samurai_B.png"),
    'b_fort': pygame.image.load("pieceImg/Fort_B.png"),
    'b_soldier': pygame.image.load("pieceImg/Soldier_B.png"),
}