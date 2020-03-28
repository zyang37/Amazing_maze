import pygame , random
from pygame.locals import *

def config_ui():
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    resolution = (700, 700)

    cell_margin = 1

    cell_colors = (255, 255, 255), (255, 192, 203)

    current_position = [0, 1]

    #icon
    icon = pygame.image.load('icon.png')
    star = pygame.image.load('star.png')
    star = pygame.transform.scale(star,(40,40))
    pygame.display.set_icon(icon)
    #score
    score = 0

    # global score,BASICFONT,FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode(resolution)
    screen.fill(cell_colors[1])
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    playerImg = pygame.image.load('mushroom.png')
    pygame.display.set_caption("Amazing Maze")
    star_store = (random_grid(grid))

if __name__ == "__main__":
    config_ui()
