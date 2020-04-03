import pygame , random
from pygame.locals import *
from maze_gen import *
'''
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
'''
grid = maze_gen(10, 10)

resolution = (700, 700)

cell_margin = 1

cell_colors = (255, 255, 255), (255, 192, 203)

current_position = [0, 1]

#icon
icon = pygame.image.load('img/icon.png')
star = pygame.image.load('img/star.png')
star = pygame.transform.scale(star,(30,30))
pygame.display.set_icon(icon)
#score
score = 0

def main():
    global score,BASICFONT,FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode(resolution)
    screen.fill(cell_colors[1])
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    playerImg = pygame.image.load('img/mushroom.png')
    pygame.display.set_caption("Amazing Maze")
    star_store = (random_grid(grid))
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                key = event.key
                if key == K_UP:
                    move(0, -1)
                elif key == K_RIGHT:
                    move(1, 0)
                elif key == K_DOWN:
                    move(0, 1)
                elif key == K_LEFT:
                    move(-1, 0)
            elif event.type == QUIT:
                return
        if current_position==star_store:
            star_store = (random_grid(grid))
            score+=1

        draw_maze(screen)
        draw_player(playerImg, screen)
        draw_star(star,screen,star_store)
        drawScore(score,screen)
        pygame.display.update()
        FPSCLOCK.tick(30)

def random_grid(listGrid):
    s = []
    for i in range(len(listGrid)):
        for j in range(len(listGrid[0])):
            if listGrid[i][j] == 1:
                s.append([j,i])
    random.shuffle(s)
    return s[0]

def draw_maze(screen):
   for row in range(len(grid)):
       for column in range(len(grid[0])):
           screen.fill(cell_colors[grid[column][row]], get_cell_rect((row, column), screen))
           if (grid[row][column] == 'x'):
               score_value += 10

def get_cell_rect(coordinates, screen):
   row, column = coordinates
   cell_width = screen.get_width() / len(grid)
   adjusted_width = cell_width - cell_margin
   return pygame.Rect(row * cell_width + cell_margin / 2, column * cell_width + cell_margin / 2, adjusted_width, adjusted_width)

def draw_player(playerImg, screen):
   rect = playerImg.get_rect()
   rect.center = get_cell_rect(current_position, screen).center
   screen.blit(playerImg, rect)

def draw_star(star,screen,position):
    rect = star.get_rect()
    rect.center = get_cell_rect(position,screen).center
    screen.blit(star,rect)

def drawScore(score, screen):
    scoreSurf = BASICFONT.render('score: %s'%(score),True,(0,0,0))
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (700-120,10)
    screen.blit(scoreSurf,scoreRect)

def move(dx, dy):
   x, y = current_position
   nx, ny = x + dx, y + dy
   if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[ny][nx]:
       current_position[0] = nx
       current_position[1] = ny

if __name__ == "__main__":
   main()
   pygame.quit()
